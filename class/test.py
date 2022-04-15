listA = [2,3]
listB = listA

listC = listA[:]
listA[0]
listB[1]

sum([323,4241,3123,1313,121], 0)
all([True, True, True, True])
any([False, False, False, True])
all([x < 5 for x in range(5)])
perfect_square = lambda x: x == round(x ** 0.5) ** 2
any([perfect_square(x) for x in range(50,60)])

coords = [[37,-122], [-22, -115], [56, -163]]
max(coords, key = lambda coord: coord[0])
min(coords, key = lambda coord: coord[0])

gymnasts = [["Brittant", 9.15, 9.4, 9.3, 9.2],
            ["Lea", 9, 8.8, 9.1, 9.5],
            ["Maya", 9.2, 8.7, 9.2, 8.8]]
min(gymnasts, key = lambda scores: min(scores[1:]))
max(gymnasts, key = lambda scores: sum(scores[1:], 0))
max(gymnasts, key = lambda scores: scores[1])

