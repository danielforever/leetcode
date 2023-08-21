class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coinFrequencies = collections.Counter(coins)
        coinKeys = sorted(list(coinFrequencies.keys()))
        largest = 0
        for coin in coinKeys : 
            if coin > largest+1 : 
                break
            else : 
                largest += (coinFrequencies[coin] * coin)
        return largest + 1