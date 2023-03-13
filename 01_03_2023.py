
class Solution:
    def twoSum(self, ll, target):
        for i in ll:
            for j in ll:
                if self.ll[i] + self.ll[j] == self.target:
                    print(i)
                    print(j)
                    print(" ")

pritam = Solution()
ll = [1,0,5,7,1,6,2,9,8,4,3,5,6,9,8,7,6,5,4,3,2,1]
pritam.twoSum(ll,6)
