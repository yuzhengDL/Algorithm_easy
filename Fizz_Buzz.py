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
