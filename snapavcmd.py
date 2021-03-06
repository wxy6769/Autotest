import telnetlib
import time as t
import os
import socket
import logging

logging.basicConfig(
    # filename='logs\\sample.log',
    format='%(asctime)s [line:%(lineno)d] - %(levelname)s: %(message)s',
    level=logging.DEBUG)


def getVersion(model, host, user, pswd):
    tn = telnetlib.Telnet()

    try:
        tn.open(host, timeout=10)
        logging.info(host + ': ' + model + ' Connected')
    except socket.timeout:
        logging.error(host + ': ' + model + ' Timeout')
        # 這個替代方案需要被謹慎完善
        os.system('\\cmd' + host + '.cmd')
        tn.open(host)
        logging.info(host + ':' + model + 'Connecting again...')

    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    tn.read_until(b'Password: ')
    tn.write(pswd.encode('ascii') + b'\n')
    tn.read_until(b'#')

    tn.write(b'sh version\n')
    logging.info(host + ': ' + model + ' Log in finish.')

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
        logging.info(host + ': ' + model + ' Connected')
    except socket.timeout:
        logging.error(host + ': ' + model + ' Timeout')
        # 這個替代方案需要被謹慎完善
        os.system('\\cmd' + host + '.cmd')
        tn.open(host)
        logging.info(host + ':' + model + 'Connecting again...')

    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    tn.read_until(b'Password: ')
    tn.write(pswd.encode('ascii') + b'\n')
    tn.read_until(b'#')

    logging.info(host + ': ' + model + ' Log in finish.')

    tn.write(cmd.encode('ascii') + b'\n')
    logging.info(host + ': ' + model + ' Downloading the file...')

    # Are you sure you want to proceed?
    tn.read_until(b'Are you sure you want to proceed ?(y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')
    logging.info(host + ': ' + model + ' Upgrading firmware now...')

    # Upgrade firmware success. Do you want to reboot now?
    tn.read_until(
        b'Upgrade firmware success. Do you want to reboot now? (y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')
    logging.info(host + ': ' + model + ' Now reboot...')
    tn.close()


def cmdReset(model, host, user, pswd):
    tn = telnetlib.Telnet()

    try:
        tn.open(host, timeout=10)
        logging.info(host + ': ' + model + ' Connected')
    except socket.timeout:
        logging.error(host + ': ' + model + ' Timeout')
        # 這個替代方案需要被謹慎完善
        os.system('\\cmd' + host + '.cmd')
        tn.open(host)
        logging.info(host + ':' + model + 'Connecting again...')

    tn.read_until(b'Username: ')
    tn.write(user.encode('ascii') + b'\n')
    tn.read_until(b'Password: ')
    tn.write(pswd.encode('ascii') + b'\n')
    tn.read_until(b'#')

    logging.info(host + ': ' + model + ' Log in finish.')

    tn.write(b'restore-defaults\n')
    tn.read_until(
        b'After restore to default, system will be rebooted. Do you want to continue? (y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')

    tn.close()
    logging.info(host + ': ' + model + ' Finish restore to defaults.')


# Test segment is at the bottom.
if __name__ == '__main__':

    # Dim log format

    host = "172.20.1.168"
    user = "araknis"
    pswd = "aaaaaaaa"
    model = "310-R-8-POE"
    ver = getVersion(model, host, user, pswd)
    print(host + ':', model, ver)
