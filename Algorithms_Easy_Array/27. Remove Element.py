'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''

#最快解法
class Solution(object):
  def removeElement(self, nums, val):
        start, end = 0, len(nums) - 1
    while start <= end:
        if nums[start] == val:
            nums[start], nums[end], end = nums[end], nums[start], end - 1 #nums[end]=nums[start]感觉没有意义？我没写这句也过了
        else:
            start +=1
    return start


# 偷懒解法1     只用了一个  remove()函数  虽然通过了验证 骚 但可能在使用remove（）时候已经开辟了新的内存 而且时间很长
class Solution(object):
    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            nums.remove(val)
        return len(nums)

# 偷懒解法2    pop（）
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, total = 0, len(nums)
        while i < total:
            if nums[i] == val:
                nums.pop(i)
                total -= 1
            else:
                i += 1
        return len(nums)

'''
这道题的难点在于有两个要求，第一要移除与val相同的数，保证新数组长度中只有剩下的（但顺序随意）；第二要返回新数组长度，其次是不能使用新的内存
remove（val）  删除list中的val元素，如果有多个，删除第一个，并不是完全删除！  count（val）查询list中val的个数  十分有必要研究 list 元组  字典  类 的内建函数
