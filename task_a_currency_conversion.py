# task_a_currency_conversion.py

import math
import heapq
from collections import defaultdict

class CurrencyGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_rate(self, from_currency, to_currency, rate):
        # Store edge with log(rate) for Dijkstra
        self.graph[from_currency].append((to_currency, math.log(rate)))

    def convert(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1.0

        heap = [(0.0, from_currency)]  # (cost, currency)
        visited = set()

        while heap:
            cost, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            visited.add(curr)
            if curr == to_currency:
                return math.exp(cost)
            for neighbor, rate_log in self.graph[curr]:
                if neighbor not in visited:
                    heapq.heappush(heap, (cost + rate_log, neighbor))

        return None  # No path found

def parse_conversion_rates(rates):
    graph = CurrencyGraph()
    for rate in rates:
        from_cur, to_cur, r = rate.strip().split(',')
        graph.add_rate(from_cur, to_cur, float(r))
    return graph
