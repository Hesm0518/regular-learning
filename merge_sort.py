import random

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    lmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            lmp.append(li[i])
            i += 1
        else:
            lmp.append(li[j])
            j += 1
    while i <= mid:
        lmp.append(li[i])
        i += 1
    while j <= high:
        lmp.append(li[j])
        j += 1

    li[low:high+1] = lmp

def merge_sort(li, low, high):
    if low < high:
        mid = (low + high)//2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)
li = list(range(16))
random.shuffle(li)
merge_sort(li, 0, len(li)-1)
print(li)

