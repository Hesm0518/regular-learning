def count_sort(li, max_count=100):
    count = [0 for _ in range(max_count+1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)
import random
li = [random.randint(0,20) for _ in range(100)]
print(li)
count_sort(li)
print(li)

