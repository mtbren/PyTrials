from typing import List


class Solution:
    setA = set();
    setB = set();
    covered = set();

    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodeNo = 0;
        self.setA = set();
        self.setB = set();
        self.covered = set();

        while len(graph) > nodeNo and len(graph[nodeNo]) == 0:
            nodeNo += 1;
        self.setA.add(nodeNo);
        self.covered.add(nodeNo);
        if nodeNo >= len(graph):
            return True;

        for node in graph[nodeNo]:
            self.recurPopulate(node, True, graph);

        return len(self.setA.intersection(self.setB)) == 0;

    def recurPopulate(self, node: int, intoSetB: bool, graph: List[List[int]]) -> None:
        if intoSetB and node in self.setA:
            self.setB.add(node);
            return;
        if not intoSetB and node in self.setB:
            self.setA.add(node);
            return;
        if node not in self.covered:
            if intoSetB:
                self.setB.add(node);
            else:
                self.setA.add(node);
            self.covered.add(node);
            for innerNode in graph[node]:
                self.recurPopulate(innerNode, not intoSetB, graph);


sol = Solution();
'''print(sol.isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]));  # False
print(sol.isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]]));  # True
print(sol.isBipartite([[1], [0, 3], [3], [1, 2]]));  # True
print(sol.isBipartite([[3], [2, 4], [1], [0, 4], [1, 3]]));  # True
print(sol.isBipartite(
    [[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9],
     [2, 4, 5, 6, 7, 8]]));  # False
print(sol.isBipartite([[]])); # True'''
print(sol.isBipartite([[2,4],[2,3,4],[0,1],[1],[0,1],[7],[9],[5],[],[6],[12,14],[],[10],[],[10],[19],[18],[],[16],[15],[23],[23],[],[20,21],[],[],[27],[26],[],[],[34],[33,34],[],[31],[30,31],[38,39],[37,38,39],[36],[35,36],[35,36],[43],[],[],[40],[],[49],[47,48,49],[46,48,49],[46,47,49],[45,46,47,48]]));