import collections
import heapq
from typing import List, Dict




class Solution:
    def __init__(self):
        self.dict_scores = {}

    def calculate_all_scores(self, mapa: Dict):
        queue = collections.deque()
        for id in mapa:
            if id not in self.dict_scores:
                queue.append(id)
                while len(queue) > 0:
                    qid = queue.pop()
                    if len(mapa[qid]) == 0:
                        self.dict_scores[qid] = 1
                    else:
                        adj_not_found = False
                        for tid in mapa[qid]:
                            if tid in self.dict_scores:
                                self.dict_scores[qid] += self.dict_scores[tid]
                            else:
                                if adj_not_found is False:
                                    self.dict_scores[qid] = 1
                                    queue.append(qid)
                                    adj_not_found = True
                                queue.append(tid)



    def get_score(self, id: str) -> int:
        return self.dict_scores[id]



mapa = {
'123': ['234'], # 5
'234': ['456', '789', '345'], # 4
'345': [], # 1
'456': [], # 1
'789': []  # 1
}



sol = Solution()
sol.calculate_all_scores(mapa)
print(sol.get_score('123'))





