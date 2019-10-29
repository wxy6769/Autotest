import telnetlib
import time as t
import os
import socket


def getVersion(model, host, user, pswd):

    tn = telnetlib.Telnet()

    try:
        tn.open(host, timeout=10)
        print('Connecting to', host)
    except socket.timeout:
        print(host, 'timed out.')
        # 這個替代方案需要被謹慎完善
        os.system('ping_cmd.cmd')
        tn.open(host)
        print('Connecting to', host, 'again...')

    tn.read_until(b'Username: ')
    # print('Inputting username...')
    tn.write(user.encode('ascii') + b'\n')
    # print('Inputting password...')
    tn.read_until(b'Password: ')
    tn.write(pswd.encode('ascii') + b'\n')
    tn.read_until(b'#')
    tn.write(b'sh version\n')

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


# Test segment is at the bottom.
if __name__ == '__main__':
    host = "172.20.1.172"
    user = "araknis"
    pswd = "aaaaaaaa"
    ver = getVersion(host, user, pswd)
    print(ver)
