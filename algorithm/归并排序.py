'''
    归并排序（MERGE-SORT）是利用归并的思想实现的排序方法，该算法采用经典的分治（divide-and-conquer）策略（
    分治法将问题分(divide)成一些小的问题然后递归求解，而治(conquer)的阶段则将分的阶段得到的各答案"修补"在一起，即分而治之).
'''


def sort(array, left, right, temp):
    if left < right:
        mid = (right+left)//2
        sort(array, left, mid, temp)
        sort(array, mid+1, right, temp)
        merge(array, left, mid, right, temp)


def merge(array, left, mid, right, temp):
    # [left,mid] [mid, right]都是已经排好序的, 需要对【left，right】进行排序
    i = left
    j = mid+1
    k = left
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
        k += 1
    right = right+1
    if i <= mid:
        temp[right-(mid+1-i): right] = array[i:mid+1]
    if j <= right:
        temp[j:right] = array[j:right]
    array[left:right] = temp[left:right]


if __name__ == '__main__':
    array = [2, 4, 6, 3, 7, 0, 9, 43, 56, 35, 5]
    print(f'输入对数组为：{array}')
    print(sorted(array))
    temp = [0]*len(array)       # 创造一个额外对数组是为了避免递归过程中额外对空间浪费。
    sort(array, 0, len(array)-1, temp)
    print(f'排序后的结果为：{array}')
