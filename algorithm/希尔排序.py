'''
1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。

算法描述
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：

选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
按增量序列个数k，对序列进行k 趟排序；
每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度
'''


def shellSort(array):
    length = len(array)
    increse = length
    while increse >= 2:                                           # 希尔排序每次增量减半
        increse = increse//2
        for i in range(increse, length):                          # 要对每个子序列进行插入排序
            j = i
            current = array[i]
            while j >= increse and current < array[j-increse]:    # 从后往前插入
                array[j] = array[j-increse]
                j = j-increse
            array[j] = current


if __name__ == '__main__':
    array = [2, 4, 6, 3, 7, 0, 9, 43, 56, 35, 5]
    print(f'输入对数组为：{array}')
    print(sorted(array))
    print('+++++++++++++++++++++++++')
    shellSort(array)
    print(f'排序后的结果为：{array}')
