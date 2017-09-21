'''
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
'''
#最佳解法
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1

nums = [0,0,1,1,1,3]
a = []
a = Solution.removeDuplicates(a,nums)
print(a)

'''
if not a:
    return 0    这句话的含义是： 一个空 list 本身等同于 False  所如果a不是一个空文件
A[newTail] = A[i]   意义是永远让下一个元素与之前最近不相同的元素比较
比较重要的一点：range(1,1)返回的none  list（range(1,1)）=[] 空列表
任何语句中存在这个东西直接  break 跳到下一逻辑语句 for 循环直接跳出来
return 直接结束函数返回  在try:  后边是个例外

Python 中 a+=b 和 a=a+b 的区别：
问题1.1. 我们通常运行b=a这一语句时，会直觉地认为，b和a已经不一样了。代码为证：
>>> a=[[1],[2],[3],[4]]
>>> b+=a[0:2]
>>> b
[1, 2, 3, 4, [1], [2]]
>>> a=[[1],[2],[3],[4]]
>>> b=[]
>>> b+=a[0:2]
>>> a,b
([[1], [2], [3], [4]], [[1], [2]])
>>> b[0]
[1]
>>> b[0][0]='changed!'
>>> # You don't expect a to change
>>> # However
>>> a, b
([['changed!'], [2], [3], [4]], [['changed!'], [2]])
可以看到，a[0]的[1]和b[0]的[1]是“一样的”，因为改变b[0]就会改变a[0]（注意不是改变b，是改变b[0]。改变b不会对a有任何影响）
问题2. list的情况下，a+=b和a=a+b是不一样的，代码为证：
>>> a=[1,2,3,4]
>>> b=a
>>> a+=[5]
>>> a,b
([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
>>> a=[1,2,3,4]
>>> b=a
>>> a=a+[5]
>>> a,b
([1, 2, 3, 4, 5], [1, 2, 3, 4])
同样通俗地讲，在+=的情况下，a还是原来的a，和b“一样”；在+的情况下，a已经不是原来的a了，和b“不一样”。
问题3. 如果要让+=和+行为一致，应该怎么做？代码为证：
>>> import copy
>>> a=[1,2,3,4]
>>> b=copy.deepcopy(a)
>>> a+=[5]
>>> a,b
([1, 2, 3, 4, 5], [1, 2, 3, 4])
这与问题2中a=a+b的情况结果一致了。当对list进行b=a时，实际上进行的是“引用”操作；只有使用b=copy.deepcopy(a)才是进行我们通常期望的“拷贝”操作。
问题4. 回到问题中的代码，当k=1时，以下代码：
subset += (elements[0:size])
根据问题1.1，subset与elements是“一样的”，因此未来改变subset的元素的操作有可能改变elements的元素。
到这行代码时，注意set就是递归传递过来的subset：
#set[j] += (elements[i]) #Why Elements change here?
set[j] = set[j] + (elements[i]) 
根据问题2，+=中set[j]依然是原来的set[j]，也就可能是elements的元素。因此
set[j] += elements[i]
可能会等价于
elements[*] += elements[i]
一旦改变了elements的元素，结果自然就不对了。
怎么解决这个问题？根据问题3，只要保证set与elements是“不一样的”，就符合程序的逻辑。因此将
subset += (elements[0:size])
改为（记得import copy）
subset += copy.deepcopy(elements[0:size])
就能在+=的情况下正常运行了。
总结：在python中，list类型的赋值b=a进行的引用操作，而非拷贝操作，在需要拷贝操作时，需要加上b=copy.deepcopy(a)。（copy.copy和copy.deepcopy的区别超出问题范畴，有兴趣可以google）