def binarySearch(a, N, key):
    start = 0
    end = N-1
    while start <= end:
        middle = (start + end)//2
        print(start, middle, end)
        if a[middle] == key:    # 검색 성공
            return True
        elif a[middle] > key:
            end = middle
        else:
            start = middle
    print(start, middle, end)
    return False    # 검색 실패

binarySearch([0,1,2,3,4,5,6,7,8,9,10], 11, 10)
