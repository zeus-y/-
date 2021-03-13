'''
桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。

算法描述
设置一个定量的数组当作空桶；
遍历输入数据，并且把数据一个一个放到对应的桶里去；
对每个不是空的桶进行排序；
从不是空的桶里把排好序的数据拼接起来。 
'''

# 桶排序最好情况下使用线性时间O(n)，桶排序的时间复杂度，取决与对各个桶之间数据进行排序的时间复杂度，
# 因为其它部分的时间复杂度都为O(n)。很显然，桶划分的越小，各个桶之间的数据越少，排序所用的时间也会越少。但相应的空间消耗就会增大。

from 插入排序 import insertSort


def bucketSort(array, num):
    # num表示桶的数量
    minValue = min(array)
    maxValue = max(array)

    count = (maxValue-minValue)//num + 1
    buckets = []      # 定义count个空的列表
    for i in range(count):
        buckets.append([])

    # 将数据放入桶中
    for i in range(len(array)):
        buckets[((array[i]-minValue)//num)].append(array[i])

    # 对每个桶进行排序，然后将排好序对桶取出来
    k = 0
    for i in range(len(buckets)):
        print(buckets[i])
        insertSort(buckets[i])
        for j in range(len(buckets[i])):
            array[k] = buckets[i][j]
            k += 1


if __name__ == '__main__':
    array = [2, 4, 6, 3, 7, 0, 9, 43, 56, 35, 5]
    print(f'输入对数组为：{array}')
    print(sorted(array))
    print('+++++++++++++++++++++++++')
    bucketSort(array, 5)
    print(f'排序后的结果为：{array}')
