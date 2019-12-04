def getLease():
    with open('dhcpd.leases.txt', 'r') as file_ob:
        lease = file_ob.read().split('lease ')

    # 刪掉文件前段註解
    del(lease[:2])

    all_sets = []

    for i in range(len(lease)):
        innerlines = lease[i].split(';\n  ')

        for j in range(len(innerlines)):
            try:
                if 'client-hostname' in innerlines[j]:

                    # 先針對IP字串進行處理
                    place_ne = innerlines[0].find(' {')
                    innerlines[0] = innerlines[0][:place_ne]
                    # 再對Model Name進行處理
                    place_ne = innerlines[j].find(';')
                    innerlines[j] = innerlines[j][:place_ne]
                    innerlines[j] = innerlines[j].replace('client-hostname ', '').replace('"', '')

                    settings = {'host': innerlines[0], 'model': innerlines[j]}
                    all_sets.append(settings)
            except IndexError:
                continue

    for i in all_sets:
        counter = all_sets.count(i)
        if counter > 1:
            del(all_sets[all_sets.index(i)])

    return(all_sets)


if __name__ == '__main__':
    a = getLease()
    print(a)
