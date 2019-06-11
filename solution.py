if __name__ == '__main__':
    T = int(input())

    import sys

    def min_cost(cost, m, n):
        if n < 0 or m < 0:
            return sys.maxsize

        elif m == 0 and n == 0:
            return cost[m][n]

        else:
            return cost[m][n] + min(min_cost(cost, m-1, n-1), min_cost(cost, m-1, n), min_cost(cost, m, n-1))


    for _ in range(T):
        houses, roads = map(int, input().split())

        costs = [[1001 for ___ in range(houses)] for __ in range(houses)]

        for i in range(roads):
            x, y, c = map(int, input().split())
            costs[x-1][y-1] = c
            costs[y-1][x-1] = c

        q = int(input())

        for i in range(q):
            h, k = map(int, input().split())
            min_c = min_cost(costs, houses - 1, h - 1)
            if 2*min_c < k:
                print(k - 2*min_c)

            else:
                print(0)
