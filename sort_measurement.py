

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



def quick_sort(xlist):
    pivot = 



