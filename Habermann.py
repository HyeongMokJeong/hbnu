process_num = 5
resouce_num = 4
max_resouce = [8, 5, 9, 7]

pc = [[[2, 0, 1, 1], [3, 2, 1, 4]], [[0, 1, 2, 1], [0, 2, 5, 2]], [[4, 0, 0, 3], [5, 1, 0, 5]], [[0, 2, 1, 0], [1, 5, 3, 0]], [[1, 0, 3, 0], [3, 0, 3, 3]]] # 현재 자원, max 자원

if __name__ == '__main__':
    print(f"number of processes : {process_num}")
    print(f"number of resources : {resouce_num}\n")

    print("-- allocated resources for each process --")
    for i in range(len(pc)):
        print(f"process{i + 1} : ", end='')
        for j in range(len(pc[i][0])):
            print(pc[i][0][j], end=' ')
        print()

    print("\n-- maximum resources for each process --")
    for i in range(len(pc)):
        print(f"process{i + 1} : ", end='')
        for j in range(len(pc[i][0])):
            print(pc[i][1][j], end=' ')
        print()

    print("\ntotal allocated resources : ", end='')
    total_all = []
    for i in range(len(pc) - 1):
        sum = 0
        for j in range(len(pc)):
            sum += pc[j][0][i]
        total_all.append(sum)
    print(total_all)

    print("total available resources : ", end='')
    total_ava = []
    for i in range(len(max_resouce)):
        total_ava.append(max_resouce[i] - total_all[i])
    print(total_ava)

    print("Additional Need : ", end='')
    add_need = []
    for i in range(len(pc)): # i = 0~4
        result = []
        for j in range(resouce_num):
            result.append(pc[i][1][j] - pc[i][0][j])
        add_need.append(result)
    print(add_need)