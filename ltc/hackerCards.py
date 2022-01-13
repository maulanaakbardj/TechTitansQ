'''Q1: Birthday Card Collection
HackerCards is a trendy new card game. Each type of HackerCard has a distinct ID number greater that or equals to 1, and the cost of each HackerCard equals its ID number. For example, HackerCard 1 costs 1, HackerCard 5 costs 5, and so on.

Leanne already has a collection started. For her birthday, Mike wants to buy her as many cards as he can, but they must cost less than or equals to his budget. He wants to buy one each of some cards she doesn't already have. If he has to make one choice among several, he will always choose the lowest cost option. Determine which cards he will buy.

For example, Leanne's collection = [2, 4, 5] and Mike has d = 7 to spend. He can purchase a maximum of 2 cards, the 1 and the 3 to add to her collection. Two other options he has are 1 and 6 (costs more) or 7(fewer cards, costs more)'''

def hackerCards(collection, d):
    collection = set(collection)
    res = []
    curSum = 0
    # Write your code here
    for i in range(1, d + 1):
        if i in collection:
            continue
        if curSum + i > d:
            break
        curSum += i
        res.append(i)
    return res
