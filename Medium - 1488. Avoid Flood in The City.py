# Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake which is full of water, there will be a flood. Your goal is to avoid the flood in any lake.

# Given an integer array rains where:

# rains[i] > 0 means there will be rains over the rains[i] lake.
# rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
# Return an array ans where:

  # ans.length == rains.length
  # ans[i] == -1 if rains[i] > 0.
  # ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.

# If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.

# Input: rains = [1,2,3,4]
# Output: [-1,-1,-1,-1]
# Explanation: After the first day full lakes are [1]
# After the second day full lakes are [1,2]
# After the third day full lakes are [1,2,3]
# After the fourth day full lakes are [1,2,3,4]
# There's no day to dry any lake and there is no flood in any lake.

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [1000]*len(rains)
        s = {} # pond vs last index
        zeros = []
        for i in range(len(rains)):
            if rains[i] > 0: # >0
                if rains[i] in s:
                    index = s[rains[i]]
                    if not zeros:
                        return []
                    elif index > zeros[-1]:
                        return []
                    elif index < zeros[0]:
                        r = 0   # r is the index of 0 we are going to pop
                    else:
                        l = 0
                        h = len(zeros)-1
                        while True:
                            m = (h+l)//2
                            if zeros[m+1]>index and index>zeros[m]:
                                r = m+1
                                break
                            elif zeros[m] > index:
                                h = m
                            elif zeros[m+1] < index:
                                l = m
                    z = zeros.pop(r) 
                    res[z] = rains[i] # previous 0 assign to new val 
                    res[i] = -1 # dried, assign -1
                    s[rains[i]] = i # record it
                        
                else: # no 0
                    s[rains[i]] = i
                    res[i] = -1
                    
            else:
                zeros.append(i)        
        return res
        
  # This is an interesting question, which requires greedy dynamic programming. We can simply dry the pond if there is zero and
  # with the zero closest to the previous flooded date. So I built a hashtable (dictionary) to store the date that flood the nth lake.
  # Next we have to greedily find the earliest but after the previous flooded date. If we do simple search: the time complexity O(N^2)
  # will TLE. So I modified using binary search to quickly search the earliest dry date; time complexity is thus lowered to O(NlogN).
  # And we beat 90% of the time and 100% of the space. This solution is faster then using heap que, but requires more lines.
  
             
             
             
            
