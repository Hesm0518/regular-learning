
def partline(li, left, right):
    min = li[left]
    while left < right :
        while left < right and li[right] >= min:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] <= min:
            left += 1
        li[right] = li[left]

    li[left] = min
    return left
def quick_sort(li, left, right):
    if left < right:
        tmp = partline(li, left, right)
        quick_sort(li, left, tmp-1)
        quick_sort(li, tmp+1, right)
li = [2, 3, 6, 9, 5, 0, 1]
quick_sort(li, 0, len(li)-1)
print(li)

