import telnetlib as tn

host = "172.20.1.168"
user = "araknis"
pswd = "aaaa"
modelName = "test"
tftpServer = 'tftp://172.20.1.167/'
newFwPath = 'an-310-sw-8-poe_fw_1.2.07_190712-1823.bix'
oldFwPath = 'an-310-sw-8-poe_fw_1.2.06_190712-1852.bix'
image0 = 'flash://image0'
image1 = 'flash://image1'

cmdNew = 'copy ' + tftpServer + newFwPath + ' ' + image0
cmdOld = 'copy ' + tftpServer + oldFwPath + ' ' + image0

tn.Telnet(host, timeout=10)

print('正在連線至', host)

tn.read_until(b'Username: ')
print('輸入使用者名稱中...')
tn.write(user.encode('ascii') + b'\n')
print('輸入密碼中...')
tn.read_until(b'Password: ')
tn.write(pswd.encode('ascii') + b'\n')
tn.read_until(modelName.encode('ascii') + b'#')

# -------------command----------------

# tn.write(cmdNew.encode('ascii') + b'\n')
tn.write(cmdOld.encode('ascii') + b'\n')
print('下載韌體中...')

# Are you sure you want to proceed?
tn.read_until(b'Are you sure you want to proceed ?(y/n)')
tn.write(b'y')
tn.read_until(b'y')
tn.write(b'\r\n')

# Upgrade firmware success. Do you want to reboot now?
tn.read_until(b'Upgrade firmware success. Do you want to reboot now? (y/n)')
tn.write(b'y')
tn.read_until(b'y')
tn.write(b'\r\n')

tn.close()

print('Upgrade finish')
