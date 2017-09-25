'''
 non-negative integer(非负整数) represented as a non-empty array of digits(位), plus one to the integer.（加一）

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
'''
#  大数加法

#自己的代码
class Solution(object):
    def plusOne(self, digits):
        c=1
        for i in range(len(digits)-1,-1,-1):
            temporary = digits[i]+c
            digits[i] = temporary%10
            c = temporary//10    
        if c==1:
            digits.insert(0,1)
        return digits
        
            
            
        """
        :type digits: List[int]
        :rtype: List[int]
        """
#  //整除    %取余数  %range逆序

#优秀代码1

def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]

'''
pow():
Python中pow()，里面可以有两个或三个参数，它们的意义是完全不同的。
1、pow(x,y):这个是表示x的y次幂。

      >>> pow(2,4)
             16
      >>> 

2、pow(x,y,z)：这个是表示x的y次幂后除以z的余数。

    >>> pow(2,4,5)
           1
意义：对于python  对于int float型数字并没有位数的限制（可以无限大，但计算很慢），所以其实这种大数加法在python语言上是没有意义的
'''


#优秀代码2
def plusOne(self, digits):
        num=reduce(lambda x,y:x*10+y,nums)+1
        return [int(i) for i in str(num)]
'''
python中的reduce
   python中的reduce内建函数是一个二元操作函数，他用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，得到的结果再与第三个数据用func()函数运算，最后得到一个结果。
如：
    def myadd(x,y):  
        return x+y  
    sum=reduce(myadd,(1,2,3,4,5,6,7))  
    print sum  

#结果就是输出1+2+3+4+5+6+7的结果即28
当然，也可以用lambda的方法，更为简单：
    sum=reduce(lambda x,y:x+y,(1,2,3,4,5,6,7))  
    print sum 
!!!!在python 3.0.0.0以后, reduce已经不在built-in function里了, 要用它就得from functools import reduce.

问题：
return [int(i) for i in str(num)]  和    return num 的区别