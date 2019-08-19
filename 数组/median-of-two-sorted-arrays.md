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

