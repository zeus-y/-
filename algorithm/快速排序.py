'''
快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

6算法描述
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

从数列中挑出一个元素，称为 “基准”（pivot）；
重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
'''


def quickSort(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quickSort(array, left, pivot-1)
        quickSort(array, pivot+1, right)


def partition(arr, left, right):
    i = (left-1)         # 最小元素索引
    pivot = arr[right]
    for j in range(left, right):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[right] = arr[right], arr[i+1]
    return (i+1)


if __name__ == '__main__':
    array = [2, 4, 6, 3, 7, 0, 9, 43, 56, 35, 5]
    print(f'输入对数组为：{array}')
    print(sorted(array))
    print('+++++++++++++++++++++++++')
    quickSort(array, 0, len(array)-1)
    print(f'排序后的结果为：{array}')
