#未成功的代码

def sift(li, low, high):
    '''
    :param li: 堆列表
    :param low: 堆根节点位置
    :param high: 堆最后一个节点位置
    :return:
    '''
    i = low
    j = 2 * i + 1
    tmp = li[low]
    while j <= high:
        if li[j+1] > li[j]:
            j = j + 1
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = i * 2 + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp

def head_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1):
        sift(li, 0, n-1)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)

li = [3, 54, 5, 7, 8, 33, 52]
head_sort(li)
print(li)
'''heapq--自带堆模块'''