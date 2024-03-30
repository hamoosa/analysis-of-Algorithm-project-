import time
import random
import matplotlib.pyplot as plt

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    M = [0] * n2
    for i in range(n1):
        L[i] = arr[l + i]
    for j in range(n2):
        M[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= M[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = M[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = M[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        merge(arr, l, m, r)

def plot_sorting_time(): 
    sizes =[10,100,200,500,600,700,800,900,1000,2000]
    n=len(sizes)
    insertion_sort_times = []
    merge_sort_times = []

    for size in sizes:
        arr_insertion =random.sample(range(size * 10), size)
        arr_merge = arr_insertion.copy()

        in_start_time = time.time()
        insertion_sort(arr_insertion)
        in_end_time=time.time()
        insertion_sort_times.append(in_end_time - in_start_time)

        me_start_time = time.time()
        merge_sort(arr_merge,0,n-1)
        me_end_time=time.time()
        merge_sort_times.append(me_end_time- me_start_time)
        

    plt.plot(sizes, insertion_sort_times, label='Insertion Sort',color="blue")
    plt.plot(sizes, merge_sort_times, label='Merge Sort',color="orange")

    for i in range(len(sizes)):
        if insertion_sort_times[i] > merge_sort_times[i]:
            plt.scatter(sizes[i], insertion_sort_times[i], color='red', marker='o')
            plt.text(sizes[i], insertion_sort_times[i], f'{sizes[i]}', color='black', fontsize=8, ha='right', va='bottom')
            break

  
    plt.xlabel('Array Size',color="green")
    plt.ylabel('Time (seconds)',color="blue")
    plt.title('insertion sort VS merge sort')
    plt.legend()
    plt.show()

plot_sorting_time()