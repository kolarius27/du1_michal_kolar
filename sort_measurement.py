import random


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


for k in range(3, 11, 1):
    a_list = random_list_num(4 ^ k)
    b_list = a_list.sort
    c_list = a_list
    for p in range(len(a_list) // 100):
        i = random.randint(0, len(a_list))
        j = random.randint(0, len(a_list))
        while i == j:
            j = random.randint(0, len(a_list))
        temp = c_list[i]
        c_list[i] = c_list[j]
        c_list[j] = temp

    
    if k < 7:
        for l in range(100):

    else:
        for l in range(10):



print(alist)
print(q_sort(alist))







