from collections import Counter

def subsetA(arr) :
        arr = sorted(arr)
        c = Counter(arr)

        # knapsack
        actual = list(c.keys())
        values = list(c.values())
        weight = [actual[i] * values[i] for i in range(len(c))]

        # dp for set B
        max_weight = int((sum(weight) - 1) / 2)
        dp = [[0] * (max_weight + 1) for _ in range(len(c) + 1)]
        for i in range(1, len(c) + 1):
            for w in range(1, max_weight + 1):
                if weight[i - 1] <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight[i - 1]] + values[i - 1])
                else:
                    dp[i][w] = dp[i - 1][w]

        # get set B
        set_B = set()
        w = max_weight
        for i in range(len(c), 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                set_B.add(actual[i - 1])
                w -= weight[i - 1]

        # get set A
        A = []
        for i in arr:
            if i not in set_B:
                A.append(i)
        return A
