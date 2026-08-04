class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       if not strs: return ""
       first_word = strs[0]
       letter_count = 0
       for i in range(1, len(strs)):
            # get the current word and start the second iterator
            current_word = strs[i]
            j = 0
            # while the index is not out of bounds for both the prefix and next word, and the prefix current letter matches the current word increment the count of the words that are matching
            while j < len(first_word) and j < len(current_word) and first_word[j] == current_word[j] :
                j+=1
        # update the prfix by splicing 
            first_word = first_word[:j]
            if first_word == "": return ""
       return first_word




        
