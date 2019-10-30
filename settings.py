def getSets():
    with open('switchset_list.txt', 'r') as file_ob:
        lines = file_ob.read().split('\n')

    keys = ['model', 'host', 'user', 'pswd', 'cmd']
    elem = []
    all_sets = []

    for i in range(len(lines)):
        elem = lines[i].split(', ')

        try:
            if len(elem) != 1:
                settings = {'model': '', 'host': '', 'user': '', 'pswd': '', 'cmd': ''}
                all_sets.append(settings)
                for j in range(len(elem)):
                    all_sets[i][keys[j]] = elem[j]
        except IndexError:
            continue

    return(all_sets)


if __name__ == '__main__':
    a = getSets()
    print(a)
    print('目前共有', len(a), '台設定')
    print('\nAll models:')
    for i in range(len(a)):
        print(a[i].get('model'))
