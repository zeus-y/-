'''
基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。
有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。

算法描述
取得数组中的最大数，并取得位数；
arr为原始数组，从最低位开始取每个位组成radix数组；
对radix进行计数排序（利用计数排序适用于小范围数的特点）；
'''


def radixSort(array):
    # 首先计算出数组当中所有分为数最多的，找到最大的元素，判断其分为数
    maxValue = max(array)
    maxDigit = len(str(maxValue))
    Digit = 1

    # 定义一个空的列表用来操作
    counter = []
    for i in range(10):
        counter.append([])
    while Digit <= maxDigit:
        dev = pow(10, Digit-1)  # 除
        mod = pow(10, Digit)  # %
        # 计算出分为数。
        for i in range(len(array)):
            value = array[i]
            value = array[i]//dev % mod
            counter[value].append(array[i])
        k = 0
        for i in range(len(counter)):
            if len(counter[i]) > 0:
                for j in range(len(counter[i])):
                    array[k] = counter[i][j]
                    k += 1
        Digit += 1

        counter = []
        for i in range(10):
            counter.append([])


if __name__ == '__main__':
    array = [2, 4, 6, 3, 7, 0, 9, 43, 56, 35, 5]
    print(f'输入对数组为：{array}')
    print(sorted(array))
    print('+++++++++++++++++++++++++')
    radixSort(array)
    print(f'排序后的结果为：{array}')
