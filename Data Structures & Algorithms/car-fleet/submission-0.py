class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for x, y in zip(position, speed):
            cars.append((x, y))

        cars.sort(key=lambda x: -x[0])
        print(cars)

        max_time_till_now = None
        ans = 0

        for car in cars:
            distance_to_travel = target - car[0]
            time_to_reach = distance_to_travel / car[1]
            if max_time_till_now is None or time_to_reach > max_time_till_now:
                max_time_till_now = time_to_reach
                ans += 1

        return ans