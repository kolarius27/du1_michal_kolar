import random
import time


def random_list_num(n):
    return [random.randrange(0, 1000) for _ in range(n)]


def select_sort(xlist):
    for i in range(len(xlist)):
        idx = i
        xmin = xlist[i]
        for j in range(i, len(xlist)):
            if xlist[j] < xmin:
                xmin = xlist[j]
                idx = j
        temp = xlist[i]
        xlist[i] = xlist[idx]
        xlist[idx] = temp
    return xlist


def insert_sort(xlist):
    ylist = []
    while len(xlist) != 0:
        ylist.append(xlist[-1])
        xlist.pop()
        if len(ylist) > 1:
            for i in range(len(ylist)):
                if ylist[-i] < ylist[-(i+1)]:
                    temp = ylist[-i]
                    ylist[-i] = ylist[-(i+1)]
                    xlist[-(i+1)] = temp
                if ylist[-i] > ylist[-(i + 1)]:
                    break
    return ylist


def quick_sort(xlist, left, right):
    pivot = xlist[(left + right) // 2]
    leftb = left
    rightb = right
    while left <= right:
        while xlist[left] < pivot:
            left += 1
        while pivot < xlist[right]:
            right -= 1
        if left <= right:
            temp = xlist[left]
            xlist[left] = xlist[right]
            xlist[right] = temp
            left += 1
            right -= 1
    if leftb < right:
        quick_sort(xlist, leftb, right)
    if rightb > left:
        quick_sort(xlist, left, rightb)


def q_sort(xlist):
    quick_sort(xlist, 0, len(xlist)-1)
    return xlist


def int_list_generating(k):
    alist = random_list_num(4 ** k)
    blist = alist
    blist.sort()
    clist = alist
    for _ in range(len(alist) // 100):
        i = random.randint(0, len(alist))
        print(i)
        j = random.randint(0, len(alist))
        while i == j:
            j = random.randint(0, len(alist))
        print(j)
        temp = clist[i]
        clist[i] = clist[j]
        clist[j] = temp
    return alist, blist, clist


def time_sort_measuring(k, xlist, function):
    time_xlist_k = []
    if k < 7:
        val = 100
    else:
        val = 10
    for l in range(val):
        if function is None:
            before = time.time_ns()
            xlist = xlist.sort()
            interval = time.time_ns() - before
        else:
            before = time.time_ns()
            xlist = function(xlist)
            interval = time.time_ns() - before
        time_xlist_k.append(interval)
    return time_xlist_k


sort_full = []
insert_sort_full = []
select_sort_full = []
quick_sort_full = []

full_list = [(None, sort_full), (insert_sort, insert_sort_full),
             (select_sort, select_sort_full), (quick_sort, quick_sort_full)]

for k in range(3, 11, 1):
    a_list, b_list, c_list = int_list_generating(k)
    print(a_list)
    print(b_list)
    print(c_list)
    for function, array in full_list:
        print(function, array)
        sort_a_list_k = time_sort_measuring(k, a_list, function)
        sort_b_list_k = time_sort_measuring(k, b_list, function)
        sort_c_list_k = time_sort_measuring(k, c_list, function)
        array.append(sort_a_list_k, sort_b_list_k, sort_c_list_k)

print(full_list)











print(alist)
print(q_sort(alist))







