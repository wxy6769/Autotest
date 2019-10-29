# #coding=utf-8
# import threading


# def thread_job():

#     # 把目前的 thread 顯示出來看看
#     print("This is an added Thread, number is {}\n"
#         .format(threading.current_thread()))


# def main():
#     # 添加一個 thread
#     added_thread = threading.Thread(target=thread_job)
#     # 執行 thread
#     # This is an added Thread,
#     # number is <Thread(Thread-1, started 123145466363904)>
#     added_thread.start()
#     # 看目前有幾個 thread
#     print(threading.active_count())
#     # 把所有的 thread 顯示出來看看
#     # [<_MainThread(MainThread, started 140736627270592)>,
#     # <Thread(Thread-1, started 123145466363904)>]
#     print(threading.enumerate())
#     # 把目前的 thread 顯示出來看看
#     # <_MainThread(MainThread, started 140736627270592)>
#     print(threading.current_thread())


# if __name__ == '__main__':
#     main()

'''
這是分隔區間
'''
# ↓↓↓↓↓↓↓↓↓↓動態產生執行緒↓↓↓↓↓↓↓↓↓↓
import threading
import time


def work(n):
    for i in range(n):
        print('Working!', i)
        time.sleep(1)


threads = []
for i in range(5):
        threads.append(threading.Thread(target=work, args=(i,)))
        threads[i].start()


for i in range(4):
    print('Main:', i)
    time.sleep(1)

for i in range(5):
        threads[i].join()
print('All Done!')
