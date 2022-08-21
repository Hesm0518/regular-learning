def insert_sort(li):
    for i in range(1, len(li)):
        j = i-1
        tmp = li[i]
        while j >= 0 and tmp < li[j]:
            li[j+1] = li[j]
            j -= 1
            li[j+1] = tmp


li = [3, 4, 2, 7, 8, 6, 1, 5]

insert_sort(li)
print(li)