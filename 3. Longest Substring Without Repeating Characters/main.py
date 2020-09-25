class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #ready solution I liked the most
        
        sLength = len(s)
        
        result, i, j = 0,0,0
        uniqueSet = set()
        
        while i < sLength and j < sLength:
            
            if s[j] not in uniqueSet:
                uniqueSet.add(s[j])
                j += 1
                result = max(result, j-i)
            else:
                uniqueSet.remove(s[i])
                i += 1
                
        return result
        
    def myFirstSolution(self, s: str) -> int:
        
        longestSubstr, maxLength = "", 0
        uniqueSubstr = ""
        windowStart = 0
        
        for ch in s:
            print("ch:", ch)
            if ch not in uniqueSubstr:
                uniqueSubstr += ch
                if len(uniqueSubstr) > maxLength:
                    longestSubstr, maxLength = uniqueSubstr, len(uniqueSubstr)
                    
                #print("added char:", uniqueSubstr)
            else:
                charIndex = uniqueSubstr.index(ch)
                
                substrIndex = s.index(uniqueSubstr, windowStart)
                oldSubstrLeng = len(uniqueSubstr)
                
                #print("charIndex {}, substrIndex {} oldSubstrLeng {}:".format(charIndex, substrIndex, oldSubstrLeng))
                windowStart = substrIndex + charIndex + 1
                end = substrIndex + charIndex + 1 + (oldSubstrLeng - charIndex)
                
                #print("windowStart {}, end {}".format(windowStart, end))
                
                uniqueSubstr = s[windowStart:end]
                
                #print("uniqueSubstr, updating:", uniqueSubstr)
                
        print("result:", maxLength, "longestSubstr", longestSubstr)
        return maxLength
            