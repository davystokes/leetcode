'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
'''
#策略  1动态规划（学习）   2扫描法    3分治策略类似二分法   4暴力膜（遍历）
#   http://blog.csdn.net/sunnyyoona/article/details/26288943

#1 自写
class Solution(object):
    def maxSubArray(self, nums):
        Maxsum=nums[0]
        sum=0
        for i in range(len(nums)):
            sum = max(sum+nums[i],nums[i])
            if sum > Maxsum:
                Maxsum = sum
        return Maxsum
        """
        :type nums: List[int]
        :rtype: int
        """
#2  扫描法  
'''
class Solution {  
public:  
    int maxSubArray(int A[], int n) {  
        if(n <= 0){  
            return 0;  
        }//if  
        // 最大和  
        int max = A[0];  
        // 当前最大和  
        int cur = 0;  
        for(int i = 0;i < n;++i){  
            // 一旦当前最大和小于0就重置为0,一个负数只能使最大和变小  
            if(cur < 0){  
                cur = 0;  
            }//if  
            cur += A[i];  
            if(cur > max){  
                max = cur;  
            }//if  
        }//for  
        return max;  
'''
