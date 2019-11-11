import telnetlib
import time as t
import os
import socket
import logging


# Dim log format
logging.basicConfig(
    filename='logs\\sample.log',
    format='%(asctime)s [line:%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.DEBUG)


def getVersion(model, host, user, pswd):
    tn = telnetlib.Telnet()

    try:
        tn.open(host, timeout=10)
        logging.info('Connecting to ' + host)
    except socket.timeout:
        logging.error(host + 'Timeout')
        # 這個替代方案需要被謹慎完善
        os.system('\\cmd' + host + '.cmd')
        tn.open(host)
        print('Connecting to', host, 'again...')

    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    tn.read_until(b'Password: ')
    tn.write(pswd.encode('ascii') + b'\n')
    tn.read_until(b'#')
    state = 'Login finished.'

    tn.write(b'sh version\n')
    print(host + ':', model, 'Login finish.')
    logging.info(host + ' : ' + model + ' Login finish.')

    # 配合網路延遲稍作等待
    t.sleep(1)
    # 將指令回傳結果以'\n'和'\r'作為分割的字元，並傳回list
    allinfo = tn.read_very_eager().decode('ascii').splitlines()

    # print('Loading system information...')
    tn.write(b'exit\n')
    tn.write(b'exit\n')
    tn.close()

    for i in range(len(allinfo)):
        if allinfo[i].find('Firmware Version : ') == 0:
            # print('Getting firmware version...\n' + allinfo[i])
            return allinfo[i]
            break


def cmdUpgrade(model, host, user, pswd, cmd):
    tn = telnetlib.Telnet()

    try:
        tn.open(host, timeout=10)
    except socket.timeout:
        print(host, 'timed out.')
        # 這個替代方案需要被謹慎完善
        os.system('ping_cmd.cmd')
        tn.open(host)
        print('Connecting to', host, 'again...')

    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    tn.read_until(b'Password: ')
    tn.write(pswd.encode('ascii') + b'\n')
    tn.read_until(b'#')

    print(host, 'Login finish.')

    tn.write(cmd.encode('ascii') + b'\n')
    print(host, 'Downloading the file...')

    # Are you sure you want to proceed?
    tn.read_until(b'Are you sure you want to proceed ?(y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')
    print(host, ':', model, 'Upgrading firmware now...')

    # Upgrade firmware success. Do you want to reboot now?
    tn.read_until(
        b'Upgrade firmware success. Do you want to reboot now? (y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')
    print(host, 'Now reboot...')
    tn.close()


def cmdReset(model, host, user, pswd):
    tn = telnetlib.Telnet()

    try:
        tn.open(host, timeout=30)
    except socket.timeout:
        print(host, 'timed out.')
        # 這個替代方案需要被謹慎完善
        os.system('ping_cmd.cmd')
        tn.open(host)
        print('Connecting to', host, 'again...')

    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    tn.read_until(b'Password: ')
    tn.write(pswd.encode('ascii') + b'\n')
    tn.read_until(b'#')

    print(host, 'Login finish.')

    tn.write(b'restore-defaults\n')
    tn.read_until(
        b'After restore to default, system will be rebooted. Do you want to continue? (y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')

    tn.close()
    print('Finish restore to defaults.')


# Test segment is at the bottom.
if __name__ == '__main__':
    host = "172.20.1.168"
    user = "araknis"
    pswd = "aaaaaaaa"
    model = "310-R-8-POE"
    ver = getVersion(model, host, user, pswd)
    print(host + ':', model, ver)
