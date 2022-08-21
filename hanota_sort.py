import random
def Hanoi(n, a, b, c):
    if n>0:
        Hanoi(n-1, a, c, b)
        print('moving from %s to %s'%(a,c))
        Hanoi(n-1, b, a, c)
print(Hanoi(3,'A','B','C'))

def bubble_sort(li):
    for i in range(len(li)-1):
        for j in range(len(li)-i-1):
            if li[j] > li[j+1] :
                li[j], li[j+1] = li[j+1], li[j]
li = [random.randint(0,10000) for i in range(50)]
print(li)
bubble_sort(li)
print(li)

