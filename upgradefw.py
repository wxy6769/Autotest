import telnetlib
import socket
import os
import snapavinfo as info


def upgrade(host, user, pswd, cmd):

    tn = telnetlib.Telnet()

    try:
        tn.open(host, timeout=30)
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

    print(host, 'Login finish.')

    tn.write(cmd.encode('ascii') + b'\n')
    print(host, 'Downloading the file...')

    # Are you sure you want to proceed?
    tn.read_until(b'Are you sure you want to proceed ?(y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')
    print(host, 'Upgrading firmware now...')

    # Upgrade firmware success. Do you want to reboot now?
    tn.read_until(b'Upgrade firmware success. Do you want to reboot now? (y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')
    print(host, 'Now reboot...')
    tn.close()


if __name__ == '__main__':

    ver = info.getVersion('172.20.1.172', 'araknis', 'aaaaaaaa')
    print('Before UP, fw ver. is', ver)
    upgrade('172.20.1.172', 'araknis', 'aaaaaaaa', 'copy tftp://172.20.1.167/an-310-sw-8-poe_fw_1.2.09_190805-1533.bix flash://image0')
    ver = info.getVersion('172.20.1.172', 'araknis', 'aaaaaaaa')
    print('After UP, fw ver. is', ver)
