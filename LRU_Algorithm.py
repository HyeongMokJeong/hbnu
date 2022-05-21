num_page_frame = 4
allocated_pages = [2, 6, 1, 4]
reference_string = [5, 1, 2, 1, 4, 5, 6, 4, 5]

def LRU_replace(n_p_f, a_p, r_s):
    # 6초부터 구현
    time = 6
    result_page = a_p
    for i in r_s:
        if len(result_page) < n_p_f:
            result_page.append(i)
        else:
            if i in result_page:
                del result_page[result_page.index(i)]
                result_page.append(i)
            else:
                del result_page[0]
                result_page.append(i)
        if time < 10: print(f"Time: {time}\t\tRef.string: {i}\t\tMemory state: {result_page}")
        else: print(f"Time: {time}\tRef.string: {i}\t\tMemory state: {result_page}")
        time += 1

    return result_page

result_pages = LRU_replace(num_page_frame, allocated_pages, reference_string)
print(result_pages)