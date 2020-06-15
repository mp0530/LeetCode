# You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of node i. The root of the tree is node 0.

# Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no such ancestor, return -1.

# The k-th ancestor of a tree node is the k-th node in the path from that node to the root.



class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        d = collections.defaultdict(list)
        for i in range(1,n):
            x = parent[i]
            d[i].append(x)
            level = 0
            while x and len(d[x]) > level:
                d[i].append(d[x][level])
                x = d[x][level]
                level += 1
        self.d = d

    def getKthAncestor(self, node: int, k: int) -> int:
        while True:
            power = 1
            while k >> power:
                power += 1
            else:
                power -= 1
                if power >= len(self.d[node]):
                    return -1
                k -= 2 ** power
                node = self.d[node][power]
                if k == 0:
                    return node
