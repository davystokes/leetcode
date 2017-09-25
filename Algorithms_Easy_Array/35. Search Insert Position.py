'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
'''

#最短时间解法：   用了二分法 速度加快：
class Solution(object):
    def searchInsert(self, nums, key):
    if key > nums[len(nums) - 1]:
        return len(nums)

    if key < nums[0]:
        return 0

    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r)/2
        if nums[m] > key:
            r = m - 1
            if r >= 0:
                if nums[r] < key:
                    return r + 1
            else:
                return 0

        elif nums[m] < key:
            l = m + 1
            if l < len(nums):
                if nums[l] > key:
                    return l
            else:
                return len(nums)
        else:
            return m


#  1行最简洁解法：
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """       
        return len([x for x in nums if x<target])
#  使用二分法排序模块  记住！

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return bisect.bisect_left(nums, target)


'''
bisect模块
Bisect模块提供的函数有：
(1)查找
bisect.bisect_left(a,x, lo=0, hi=len(a)) :
查找在有序列表a中插入x的index。lo和hi用于指定列表的区间，默认是使用整个列表。
bisect.bisect_right(a,x, lo=0, hi=len(a))
bisect.bisect(a, x,lo=0, hi=len(a))
这2个和bisect_left类似，但如果x已经存在，在其右边插入。
（2）插入
bisect.insort_left(a,x, lo=0, hi=len(a))
在有序列表a中插入x。如果x已经存在，在其左边插入。返回值为index。 和a.insert(bisect.bisect_left(a,x, lo, hi), x) 的效果相同。
bisect.insort_right(a,x, lo=0, hi=len(a))
bisect.insort(a, x,lo=0, hi=len(a))
和insort_left类似，但如果x已经存在，在其右边插入。
 
可以函数可以分2类，bisect*，用于查找index。Insort*用于实际插入。默认重复时从右边插入。实际常用的估计是insort。
'''