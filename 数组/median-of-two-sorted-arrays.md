题目描述见[官网](https://leetcode.com/problems/median-of-two-sorted-arrays/)

大概就是两个排好序的数组, 找到这两个数组的中位数.

例如:

- example1

```sh
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
```

- example2

```sh
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
```

那看下中位数的特征: 在一个排好序的数组中, 中位数左边的所有值都不大于中位数, 右边都不小于这个值.

既然是两个排好序的数组, 那么第一反应应该是merge排序, merge排序是递归的将排好序的数组组合成一个大的数组, 实现如下:


```python

# -*- coding: utf-8 -*-

def get_index(la, a):
    if la < a:
        return la + 1
    else:
        return la

def get_value(a, A, b, B):
    if a > len(a) -1:
        return None
    else:
        return  A[a]
def median(A, B):
    a = len(A)
    b = len(B)
    if a > b:
        a, b, A, B = b, a, B, A
    if (a + b ) % 2 == 1:
        mida = (a + b ) // 2
        midb = (a + b ) // 2 + 1
    else:
        mida = midb = (a + b) // 2
    ba=bb=0
    ma= A[0]
    mb= B[0]
    print(mida)
    while ba + bb <= mida:
        # na = ba + 1
        # nb = bb + 1
        if ba == a:
            bb += 1
            ma = B[bb]
            mb = B[bb-1]
            continue
        if bb == b:
            ba += 1
            ma = A[ba-1]
            mb = A[ba ]
            continue
        if A[ba] < B[bb]:
            ma = A[ba]
            ba = get_index(ba, a)

        elif A[ba] > B[bb]:
            mb = B[bb]
            bb = get_index(bb, b)

        else:

            ba = get_index(ba, a)
            bb = get_index(bb, b)
            ma = A[ba]
            mb = B[bb]
        print(ba, bb, ma, mb)
    print(ma, mb, mida)
    print("两个数组总长度是%d" % (a+b))
    if (a+b) % 2 == 0:
        return (ma+mb) / 2
    else:
        return mb

if __name__ == '__main__':
    # a = [1, 3, 4, 5]
    # b = [0]
    a = [1, 3, 4, 5, 7, 9]
    b = [2, 3, 4, 6, 8]
    print(median(a, b))
```