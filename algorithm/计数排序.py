'''
计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

算法描述
找出待排序的数组中最大和最小的元素；
统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。


# 以空间换时间对算法。
'''


def countingSort(array):
    # 1. 找出数组中对最大值,加一是为了构造一个足够大大数组
    maxValue = max(array)+1
    # 2. 构造新的数组，并进行计数
    new = [0]*maxValue
    for i in range(len(array)):
        new[array[i]] += 1
    # 从心数组中取元素
    k = 0
    for i in range(maxValue):
        while(new[i] > 0):
            new[i] -= 1  # 取元素，计数减1
            array[k] = i
            k += 1


if __name__ == '__main__':
    array = [2, 4, 6, 3, 7, 0, 9, 43, 56, 35, 5]
    print(f'输入对数组为：{array}')
    print(sorted(array))
    print('+++++++++++++++++++++++++')
    countingSort(array)
    print(f'排序后的结果为：{array}')
