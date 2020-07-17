### Leetcode Contest 197 Q3

# You are given an undirected weighted graph of n nodes (0-indexed), 
# represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].
# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.
# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.



from math import log2
from collections import defaultdict
import heapq as hq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        d = collections.defaultdict(list)
        for i in range(len(edges)):
            succProb[i] = math.log2(succProb[i])
            d[edges[i][0]].append((edges[i][1],succProb[i]))
            d[edges[i][1]].append((edges[i][0],succProb[i]))
        
        visited = set()
        distance = [-float("inf")]*n
        distance[start] = 0
        heap = [(0,start)]
        
        while heap:
            prob, node = hq.heappop(heap)
            if node == end:
                return 2 ** (-prob)
            visited.add(node)
            for curnode, curprob in d[node]:
                if curnode not in visited:
                    if distance[curnode] < curprob+distance[node]:
                        distance[curnode] = curprob+distance[node]
                        hq.heappush(heap,(-distance[curnode],curnode))
        return 0

### Idea ###   
# This is a question to find the nearest path. DFS and BFS are the initial thought, but this question is more designed for Dijkstra algorithm as weighted path.
# Also, there will be recursively multiplying probabilities when navigating nodes. To avoid more error and to increase efficiency, log2 is applied to the probabilities.
# Because we have to find the maximum probability everytime in order to get the next nearest node, I use heap to make the search time linear.

### Implement ###
# First, write a dictionary that establish the relationship between each node.
# Then, visited is a hashtable that stores visited node; distance is a list that stores the current probability of each node. 
# Inititalize the heap with a tuple of probability and the "Start" node.
# Finally, run a simple while loop that navigates the nodes, and return the probability if "End" node is met, else return 0 (can't reach to the "End").
