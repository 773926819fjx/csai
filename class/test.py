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

name = "Psadaad"
type(name)
name[0]
name[4:]
name.upper()
name.lower()

names = ["Pamela", "Spamela", "Pammyla", "ELa"]
type(names)
names[0]
names[-1]
names.index("Spamela")
names.copy()

s = [2, 3]
t = [5, 6]
s.append(4)
s
s.append(t)
s
t = 0

s = [2, 3]
t = [5, 6]
s.extend(4)  # error
s
s.extend(t)
s
t = 0