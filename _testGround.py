import os
import threading as th

# host = '127.0.0.1'


def ping(host):
    with open('C:\\Users\\102710.SNGROUP01\\Desktop\\cmd\\' + host + '.cmd', 'w') as file_ob:
        # print(file_ob.readline())
        file_ob.write('ping ' + host + '\n')
    os.system('ping_cmd.cmd')


# Dim list of threads.
threads = []
host = ['127.0.0.1', '8.8.8.8', '172.20.1.169']

# Dim multi-threads according to list of threads.
for i in range(len(host)):
    threads.append(th.Thread(target=ping, args=(host[i],)))
    threads[i].start()
    # print(threads[i])
    # print(host[i])

# Main will wait for subs finished.
for i in range(len(threads)):
    threads[i].join()
