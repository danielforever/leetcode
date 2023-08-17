# 23:18
# 00:53
# 01:35

class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        # word1Pointer = 0
        # word2Pointer = 0
        # merge = ""

        # while word1Pointer < len(word1) or word2Pointer < len(word2):
        #     if word1Pointer < len(word1) and word2Pointer < len(word2):
        #         if word1[word1Pointer:] > word2[word2Pointer:]:
        #             merge += word1[word1Pointer]
        #             word1Pointer += 1
        #         else:
        #             merge += word2[word2Pointer]
        #             word2Pointer += 1
        #     elif word1Pointer < len(word1):
        #         merge += word1[word1Pointer]
        #         word1Pointer += 1
        #     else:
        #         merge += word2[word2Pointer]
        #         word2Pointer += 1

        # return merge




        # w1, w2, ans = list(word1), list(word2), ''      
        # while w1 and w2:                               
        #     ans+= w1.pop(0) if w1 > w2 else w2.pop(0)   
        # return  ans + ''.join(w1) + ''.join(w2)  



        word1Pointer = 0
        word2Pointer = 0
        merge = ""

        while word1Pointer < len(word1) and word2Pointer < len(word2):
            if word1[word1Pointer] > word2[word2Pointer]:
                merge += word1[word1Pointer]
                word1Pointer += 1
            elif word1[word1Pointer] < word2[word2Pointer]:
                merge += word2[word2Pointer]
                word2Pointer += 1
            else:
                i, j = word1Pointer, word2Pointer
                while i < len(word1) and j < len(word2) and word1[i] == word2[j]:
                    i += 1
                    j += 1
                if i == len(word1) or (j < len(word2) and word1[i] < word2[j]):
                    merge += word2[word2Pointer]
                    word2Pointer += 1
                else:
                    merge += word1[word1Pointer]
                    word1Pointer += 1

        while word1Pointer < len(word1):
            merge += word1[word1Pointer]
            word1Pointer += 1

        while word2Pointer < len(word2):
            merge += word2[word2Pointer]
            word2Pointer += 1

        return merge