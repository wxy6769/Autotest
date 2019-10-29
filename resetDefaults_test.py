import telnetlib
import socket
import os


def reset(host, user, pswd):

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
    print('Inputting username...')
    tn.write(user.encode('ascii') + b'\n')
    print('Inputting password...')
    tn.read_until(b'Password: ')
    tn.write(pswd.encode('ascii') + b'\n')
    tn.read_until(b'#')

    tn.write(b'restore-defaults\n')
    tn.read_until(b'After restore to default, system will be rebooted. Do you want to continue? (y/n)')
    tn.write(b'y')
    tn.read_until(b'y')
    tn.write(b'\r\n')

    tn.close()


if __name__ == '__main__':

    host = "172.20.1.168"
    user = "araknis"
    pswd = "aaaa"

    reset(host, user, pswd)
    print('Finish restore to defaults.')
