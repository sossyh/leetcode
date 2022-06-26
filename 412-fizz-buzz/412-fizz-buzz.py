class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1):
            var=""
            if(i%3==0):
                var=var+"Fizz"
            if(i%5==0):
                var=var+"Buzz"
            if(i%3!=0 and i%5!=0):
                var=var+str(i)
            result.append(var)
        return result
        