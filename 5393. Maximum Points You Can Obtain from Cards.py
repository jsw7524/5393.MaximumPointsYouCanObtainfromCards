class Solution:
    def maxScore(self, cardPoints, k):
        prefixSum=[0]
        suffixSum=[0]
        tmp=0
        for c in cardPoints:
            tmp+=c
            prefixSum.append(tmp)
        tmp=0
        for c in cardPoints[::-1]:
            tmp += c
            suffixSum.append(tmp)
        max=0
        for i in range(k+1):
            if prefixSum[i] + suffixSum[k-i] > max:
                max = prefixSum[i] + suffixSum[k-i]
        return max

sln=Solution()
assert 12==sln.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3)
assert 4==sln.maxScore(cardPoints = [2,2,2], k = 2)
assert 55==sln.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7)
assert 1==sln.maxScore(cardPoints = [1,1000,1], k = 1)
assert 202==sln.maxScore(cardPoints = [1,79,80,1,1,1,200,1], k = 3)
