class rational:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def add(self):
        if self.x2 == self.y2:
            a = self.x1 + self.y1
            b = self.x2
        else:
            a = self.x1 * self.y2 + self.y1 * self.x2
            b = self.x2 * self.y2
        x = a
        y = b
        while a % b != 0:
            a, b = b, (a % b)
        if x % y == 0:
            return x//y
        else:
            return str(x//b) + '/' + str(y // b)\
                
a = input().split()
b = []
for i in a:
    n , m = i.split('/')
    b.append(int(n))
    b.append(int(m))
num = rational(b[0] , b[1] , b[2] , b[3])
print(num.add())