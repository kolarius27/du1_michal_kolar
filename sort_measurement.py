import random
import time
import math
import csv
import string
import shutil


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


def q_sort(xlist, left, right):
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
        q_sort(xlist, leftb, right)
    if rightb > left:
        q_sort(xlist, left, rightb)


def quick_sort(xlist):
    q_sort(xlist, 0, len(xlist)-1)
    return xlist


def int_list_generating(k):
    alist = random_list_num(4 ** k)
    blist = quick_sort(alist[:])
    clist = blist[:]
    for _ in range(math.comb(len(clist), 2) // 100):
        i = random.randint(0, len(clist)-1)
        j = random.randint(0, len(clist)-1)
        while i == j:
            j = random.randint(0, len(clist)-1)
        temp = clist[i]
        clist[i] = clist[j]
        clist[j] = temp
    return [alist, blist, clist]


def time_sort_measuring(k, xlist, function, csv_file, new_csv_file, field_name):
    with open(csv_file, 'r', encoding='utf-8', newline='') as csv_read:
        reader1 = csv.reader(csv_read)

        with open(new_csv_file, 'w', newline='') as csv_write:
            writer1 = csv.writer(csv_write)

            if k < 7:
                next(reader1)
                for row in reader1:
                    if function is None:
                        before = time.time_ns()
                        xlist.sort()
                        after = time.time_ns()
                        interval = after - before
                    else:
                        before = time.time_ns()
                        xlist = function(xlist)
                        after = time.time_ns()
                        interval = after - before
                    print(row, field_name, interval)
                    writer1.writerow(row + [interval])
            else:
                for row in reader1[:11]:
                    if function is None:
                        before = time.time_ns()
                        xlist.sort()
                        after = time.time_ns()
                        interval = after - before
                    else:
                        before = time.time_ns()
                        xlist = function(xlist)
                        after = time.time_ns()
                        interval = after - before
                    writer1.writerow(row + [interval])
    shutil.copyfile(new_csv_file, csv_file)


functions = [None, select_sort, quick_sort]

fieldnames_sort = ['iteration']

for k in range(3, 6, 1):
    print(k)
    abc_list = int_list_generating(k)
    for fc in functions:
        for i in range(3):
            if fc is None:
                fieldname = str(k) + "_sort_" + string.ascii_lowercase[i]
            else:
                fieldname = str(k) + "_" + fc.__name__ + "_" + string.ascii_lowercase[i]
            fieldnames_sort.append(fieldname)


with open('sort_alg.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(1,101):
        writer.writerow([i])

with open('sort_alg.csv', 'r', newline='', encoding='utf-8') as csvfile1:
    reader1 = csv.reader(csvfile1)
    with open('new_sort_alg.csv', 'w', newline='', encoding='utf-8') as csvfile2:
        writer2 = csv.writer(csvfile2)
        for line in reader1:
            writer2.writerow([line, [1]])

shutil.copyfile('new_sort_alg.csv', 'sort_alg.csv')




breakpoint()
index = 1
for k in range(3,6,1):
    [a_list, b_list, c_list] = int_list_generating(k)
    for fc in functions:
        for _list in [a_list, b_list, c_list]:
            time_sort_measuring(k, _list, fc, 'sort_alg.csv', 'sort_alg_new.csv', fieldnames_sort[index])
            index += 1