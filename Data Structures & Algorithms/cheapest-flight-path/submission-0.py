class Solution:
    def process_edges(self, flights, cost_array, n, source):
        new_cost_array = [None] * n
        new_cost_array[source] = 0
        for flight in flights:
            src, dest, price = flight
            new_cost = cost_array[src] + price if cost_array[src] is not None else None
            if new_cost is not None:
                new_cost_array[dest] = (
                    min(new_cost, cost_array[dest]) if cost_array[dest] is not None else new_cost
                )

        return new_cost_array

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        cost_array = [None] * n
        cost_array[src] = 0

        for i in range(k + 1):
            cost_array = self.process_edges(flights, cost_array, n, src)

        return cost_array[dst] if cost_array[dst] is not None else -1
