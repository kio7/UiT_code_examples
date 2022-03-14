import time
from random import randint


def timer(func):
    def wrapper(*args, **kwargs):
        a = time.perf_counter()
        func(*args, **kwargs)
        print(f"Time used: {time.perf_counter() - a:.12f}")
        return func(*args, **kwargs)

    return wrapper

@timer
def insertion_sort(lis):
    for i in range(1, len(lis)):
        current_element = lis[i]
        k = i - 1
        while current_element < lis[k] and k >= 0:
            lis[k+1] = lis[k]
            k -= 1
        lis[k+1] = current_element

    return lis

@timer
def bubble_sort(lis):
    k = len(lis)
    need_new_scan = True

    while k > 0 and need_new_scan:
        need_new_scan = False
        for i in range(k-1):
            if lis[i] > lis[i + 1]:
                lis[i + 1], lis[i] = lis[i], lis[i + 1]
                need_new_scan = True
        k -= 1

    return lis



def merge_sort(lis):
    if len(lis) > 1:
        first_half = lis[:len(lis)//2]
        second_half = lis[len(lis)//2:]

        merge_sort(first_half)
        merge_sort(second_half)

        merge(first_half, second_half, lis)

    return lis


def merge(first, second, target):
    current_1 = 0
    current_2 = 0
    current_3 = 0
    while current_3 < len(target):
        if first[current_1] < second[current_2]:
            target[current_3] = first[current_1]
            current_1 += 1
        else:
            target[current_3] = second[current_2]
            current_2 += 1
        
        current_3 += 1

        if current_1 == len(first) or current_2 == len(second):
            break

    while current_1 < len(first):
        target[current_3] = first[current_1]
        current_1 += 1
        current_3 += 1
    
    while current_2 < len(second):
        target[current_3] = second[current_2]
        current_2 += 1
        current_3 += 1
    
    # return target
@timer
def merge_sort_helper(lis):
    merge_sort(lis)
    return lis


def quick_sort(lis, left, right):
    if left >= right:
        return lis
    
    pivot = lis[(left + right) // 2]
    partition_index = partition(lis, left, right, pivot)
    quick_sort(lis, partition_index, right)

    return lis


def partition(lis, left, right, pivot):
    while left <= right:

        while lis[left] < pivot:
            left += 1

        while lis[right] > pivot:
            right -= 1

        if right >= left:
            lis[right], lis[left] = lis[left], lis[right]
            left += 1
            right -= 1
    
    return left

@timer
def quick_sort_helper(lis):
    quick_sort(lis, 0, len(lis)-1)
    return lis

def make_list():
    lis = []
    for x in range(200000):
        lis.append(randint(-100000000,100000000))
    return lis

@timer
def list_helper():
    lis = make_list()
    return lis

if __name__ == "__main__":
    # lis = [0, 2, 4, -1, 4, -5, 3, 10, 20, 21, 12, 13, 100, -1, -10, 75, -35, 40]

    print("Make List")
    lis = list_helper()

    # print('\nBubble sort')
    # bubble_sort(lis)

    # print('\nInsertion sort')
    # insertion_sort(lis)

    print('\nMerge sort')
    merge_sort_helper(lis)

    print('\nQuick sort')
    quick_sort_helper(lis)
