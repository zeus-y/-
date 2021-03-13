'''
'''


def heapSort(array):
    buildMaxHeap(array)
    length = len(array)
    i = length-1
    while i > 0:
        array[0], array[i] = array[i], array[0]
        length -= 1
        heapify(array, 0, length)


def buildMaxHeap(array):
    # 建立大顶堆
    length = len(array)
    i = length//2
    while i >= 0:
        heapify(array, i, length)


def heapify(array, i, length):
    # 堆调整
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < length and array[left] > array[largest]:
        largest = left

    if right < length and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, largest, length)


if __name__ == '__main__':
    array = [2, 4, 6, 3, 7, 0, 9, 43, 56, 35, 5]
    print(f'输入对数组为：{array}')
    print(sorted(array))
    print('+++++++++++++++++++++++++')
    heapSort(array)
    print(f'排序后的结果为：{array}')
