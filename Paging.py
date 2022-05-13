import random

page_map_table = {}
pageSize = 4

def virtual_address(p, d):
    return page_map_table[p][1] * pageSize + d

if __name__ == '__main__':
    # page map table 제작
    for i in range(0, 40): # i = (pagenumber)p
        re_bit = random.randint(0, 1)
        p_prime = random.randint(0, 255) # page frame number는 0번 ~ 255번까지 (크기 1024 / 4)
        page_map_table[i] = [re_bit, p_prime]

    print("\t residence bit\t page frame number")
    for i in range(0, 40):
        print(f"{i}\t {page_map_table[i][0]}\t\t\t\t {page_map_table[i][1]}")
    print("---------------------------------------")

    main_memory = [random.randint(1, 10000) for i in range(1024)]

    for i in range(40):
        d = random.randint(0, 3)
        print(f"v = ({i}, {d})\n"
        f">> page frame number = { page_map_table[i][1]}\n"
        f">> page size = {pageSize}\n"
        f">> displacement = {d}\n"
        f">> real adress computation = {virtual_address(i, d)}\n"
        f">> main_mamory[{virtual_address(i, d)}] >> {main_memory[virtual_address(i, d)]}")
        print()