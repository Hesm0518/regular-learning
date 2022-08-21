
def insert_sort(li, gap):
    for i in range(gap, len(li)):
        j = i-gap
        tmp = li[i]
        while j >= 0 and tmp < li[j]:
            li[j+gap] = li[j]
            j -= gap
            li[j+gap] = tmp

def shell_sort(li):
    d = len(li)//2
    while d >= 1:
        insert_sort(li, d)
        d = d // 2

li = list(range(50))
import random
random.shuffle(li)
print(li)
shell_sort(li)
print(li)

