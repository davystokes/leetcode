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
#2  扫描法  （c语言）
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
#   分治法  无限二分法

'''
#include <stdio.h>

//N是数组长度，num是待计算的数组，放在全局区是因为可以开很大的数组
int N, num[16777216];

int solve(int left, int right)
{
    //序列长度为1时
    if(left == right)
        return num[left];
    
    //划分为两个规模更小的问题
    int mid = left + right >> 1;
    int lans = solve(left, mid);
    int rans = solve(mid + 1, right);
    
    //横跨分割点的情况
    int sum = 0, lmax = num[mid], rmax = num[mid + 1];
    for(int i = mid; i >= left; i--) {
        sum += num[i];
        if(sum > lmax) lmax = sum;
    }
    sum = 0;
    for(int i = mid + 1; i <= right; i++) {
        sum += num[i];
        if(sum > rmax) rmax = sum;
    }

    //答案是三种情况的最大值
    int ans = lmax + rmax;
    if(lans > ans) ans = lans;
    if(rans > ans) ans = rans;

    return ans;
}

int main()
{
    //输入数据
    scanf("%d", &N);
    for(int i = 1; i <= N; i++)
        scanf("%d", &num[i]);

    printf("%d\n", solve(1, N));

    return 0;
}
'''