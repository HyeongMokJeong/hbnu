num_page_frame = 4
allocated_pages = []
reference_string = [1, 2, 6, 1, 4, 5, 1, 2, 1, 4, 5, 6, 4, 5]

def LRU_replace(n_p_f, a_p, r_s):
    lists = [] # 참조된 순서 배열
    result_page = a_p
    for time, i in enumerate(r_s):
        page_fault = False
        if i in a_p:
            del lists[lists.index(i)]
            lists.append(i)
        else: # a_p 안에 없다면
            if len(a_p) < n_p_f: # 4개 이하라면
                a_p.append(i)
                lists.append(i)
                page_fault = True
            else: # 4개 이상이라면
                a_p[a_p.index(lists[0])] = i
                del lists[0]
                lists.append(i)
                page_fault = True
        if time < 9: 
            print(f"Time: {time + 1}\t\tRef.string: {i}\t\tMemory state: {a_p}", end='\t')
            if page_fault and len(a_p) < n_p_f: print("\tPage fault")
            elif page_fault: print("Page fault")
            else: print()
        else: 
            print(f"Time: {time + 1}\tRef.string: {i}\t\tMemory state: {a_p}", end='\t')
            if page_fault: print("Page fault")
            else: print()
    
    return result_page

result_pages = LRU_replace(num_page_frame, allocated_pages, reference_string)
print(result_pages)