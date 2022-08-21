
def select_sort(li):
    for i in range(len(li)-1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
    print(li)
li = [3, 2, 5, 4, 7, 8, 1, 6]
print(li)
select_sort(li)

