import logging
import telnetlib
import time


class TelnetClient():
    def __init__(self,):
        self.tn = telnetlib.Telnet()

    # 此函數實現telnet登錄主機
    def login_host(self, host_ip, username, password):

        try:
            # self.tn = telnetlib.Telnet(host_ip,port=23)
            self.tn.open(host_ip, port=23)
        except Exception:
            logging.warning('%s網絡連接失敗' % host_ip)
            return False

        # 等待login出現後輸入用戶名，最多等待10秒
        self.tn.read_until(b'Username: ', timeout=10)
        self.tn.write(username.encode('ascii') + b'\n')

        # 等待Password出現後輸入用戶名，最多等待10秒
        self.tn.read_until(b'Password: ', timeout=10)
        self.tn.write(password.encode('ascii') + b'\n')

        # 延時兩秒再收取返回結果，給服務端足夠響應時間
        time.sleep(2)

        # 獲取登錄結果
        # read_very_eager()獲取到的是的是上次獲取之後本次獲取之前的所有輸出
        command_result = self.tn.read_very_eager().decode('ascii')
        if '% Authentication Failed\r\n' not in command_result:
            logging.warning('%s登錄成功' % host_ip)
            return True
        else:
            logging.warning('%s登錄失敗，用戶名或密碼錯誤' % host_ip)
            return False

    # 此函數實現執行傳過來的命令，並輸出其執行結果
    def execute_some_command(self, command):

        # 執行命令
        self.tn.write(command.encode('ascii') + b'\n')
        time.sleep(2)

        # 獲取命令結果
        command_result = self.tn.read_very_eager().decode('ascii')
        logging.warning('命令執行結果：\n%s' % command_result)

    # 退出telnet
    def logout_host(self):
        self.tn.write(b"exit\n")


if __name__ == '__main__':
    host_ip = '172.20.1.168'
    username = 'araknis'
    password = 'aaaa'
    command = 'sh info'
    telnet_client = TelnetClient()

    # 如果登錄結果返加True，則執行命令，然後退出
    if telnet_client.login_host(host_ip, username, password):
        telnet_client.execute_some_command(command)
        telnet_client.logout_host()
