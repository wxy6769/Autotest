import threading as th
import settings as sets
import snapavinfo as info
import upgradefw as up
import time as t

# Get configures
a = sets.getSets()

# Dim keys in dict.
keys = ['model', 'host', 'user', 'pswd', 'cmd']


# Content of one thread.
def upfwtest(model, host, user, pswd, cmd):
    ver = info.getVersion(model, host, user, pswd)
    print(host + ':', model, ver)
    # up.upgrade(host, user, pswd, cmd)
    # t.sleep(80)
    # try:
    #     ver = info.getVersion(model, host, user, pswd)
    # except Exception:
    #     t.sleep(20)
    #     ver = info.getVersion(model, host, user, pswd)
    # print(host + ':', model, ver)


# Dim list os threads.
threads = []

# Dim multi-threads according to list of threads.
for i in range(len(a)):
    get_val = []
    print('這是第', i + 1, '個執行緒設定')
    for k in keys:
        get_val.append(a[i].get(k))

    print(get_val)
    threads.append(th.Thread(target=upfwtest,
        args=(get_val[0], get_val[1], get_val[2], get_val[3], get_val[4],)))
    threads[i].start()

# Main will wait for subs finished.
for i in range(len(a)):
    threads[i].join()
