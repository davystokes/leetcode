'''
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

# 优秀代码  给你跪了
def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]


'''
深入了解map函数和lambda函数好强大
http://blog.csdn.net/seetheworld518/article/details/46959871

map(func, seq1[, seq2,…]) 
第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。 
Python函数编程中的map()函数是将func作用于seq中的每一个元素，并将所有的调用的结果作为一个list返回。如果func为None，作用同zip()。

1、当seq只有一个时，将函数func作用于这个seq的每个元素上，并得到一个新的seq。 
2、当seq多于一个时，map可以并行（注意是并行）地对每个seq执行如下图所示的过程： 
3.当func函数时None时，这就同zip()函数了，并且zip()开始取代这个了，目的是将多个列表相同位置的元素归并到一个元组。如：
>>> print map(None, [2,4,6],[3,2,1])
[(2, 3), (4, 2), (6, 1)]


总结几点：
1，python3中 map返回的是数组（或者其他的首地址）变成数组要加list（），是某个元素或者
字符串成为一个list 方法是在两端加[]!
2，list+list 是指对两个list取并集，里面的元素不会改变
3,，res[:numRows]是防止numRows = 0的情况，写代码永远要考虑特殊情况
4，python2中的print自动换行，单python3并没有这个功能若要实现 print（xxx，end=“）
5，本解答并没有输出居中且自动换行的格式，这个需要后面学习加以解决