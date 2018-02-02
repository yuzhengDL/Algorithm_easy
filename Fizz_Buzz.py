/*
问题描述：
输入n，输出1到n数字的字符串描述。如果数字是3的倍数，则输出换成'Fizz'；若数字是5的倍数，则输出换成'Buzz'；若数字即是三的倍数也是五的倍数，则输出'FizzBuzz'.

n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
*/

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        res = []
        for i in range(1,n+1):
            if i%3==0 or i%5==0:
                res.append('Fizz'*(not i%3)+'Buzz'*(not i%5))
            else:
                res.append(str(i))
        return res
