def getLease():
    with open('dhcpd.leases.txt', 'r') as file_ob:
        lease = file_ob.read().split('lease ')

    # 刪掉文件前段註解
    del(lease[:2])

    # 此變數用於存取每組lease紀錄
    innerlines = []
    # 此變數用於存放所有lease紀錄
    all_sets = []

    # 外圈-走訪文件，分行split存至list
    for i in range(len(lease)):
        innerlines = lease[i].split(';\n  ')

        # 走訪list
        for j in range(len(innerlines)):
            try:
                # 尋找lease紀錄中包含'client-hostname'的元素
                if 'client-hostname' in innerlines[j]:

                    # 先針對IP字串進行處理
                    place_ne = innerlines[0].find(' {')
                    innerlines[0] = innerlines[0][:place_ne]

                    # 再針對Model Name進行處理
                    for x in innerlines:
                        place_ne = innerlines[j].find(';')
                        innerlines[j] = innerlines[j][:place_ne]
                        break

                    settings = {'host': innerlines[0], 'model': innerlines[j]}
                    all_sets.append(settings)

            except IndexError:
                continue

    return(all_sets)


if __name__ == '__main__':
    a = getLease()
    print(a)
