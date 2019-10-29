import threading
import time as t
import snapavinfo as info
import upgradefw as up


# 子執行緒的工作函數
def machine1():
    host = '172.20.1.168'
    user = 'araknis'
    pswd = 'aaaa'
    cmd = 'copy tftp://172.20.1.167/an-310-sw-8-poe_fw_1.2.06_190712-1852.bix flash://image0'

    verBf = info.getVersion(host, user, pswd)
    print('Version is', verBf, 'before upgrade.')
    up.upgrade(host, user, pswd, cmd)
    t.sleep(75)
    verAf = info.getVersion(host, user, pswd)
    print('Version is', verAf, 'after upgrade.')
    if verAf != verBf:
        print('Upgrade test PASS.')
    else:
        print('Upgrade test FAIL.')


def machine2():
    host = '172.20.1.169'
    user = 'araknis'
    pswd = 'aaaa'
    cmd = 'copy tftp://172.20.1.166/an-210-sw-8-poe_fw_1.2.07_190808-1844.bix flash://image0'

    verBf = info.getVersion(host, user, pswd)
    print('Version is', verBf, 'before upgrade.')
    up.upgrade(host, user, pswd, cmd)
    t.sleep(75)
    verAf = info.getVersion(host, user, pswd)
    print('Version is', verAf, 'after upgrade.')
    if verAf != verBf:
        print('Upgrade test PASS.')
    else:
        print('Upgrade test FAIL.')


def main():
    # 建立子執行緒
    t1 = threading.Thread(target=machine1)
    t2 = threading.Thread(target=machine2)

    # 執行子執行緒
    t1.start()
    t2.start()

    # main() calls .join() to waits for both threads to finish.
    t1.join()
    t2.join()
    print("All done.")


if __name__ == '__main__':
    main()
