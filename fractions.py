
def gcd(m,n): #finding the greatest common denominator
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

def lcm(m, n): #finding the least common multiple
    if m > n:
        for i in range(1, m):
            if (i * m) % n == 0:
                return i*m
    else:
        for i in range(1, n):
            if (i * n) % m == 0:
                return i*n
                
    
class Fraction:
    def __init__(self,top,bottom):
        gr_com_den = gcd(top, bottom)
        self.num = top // gr_com_den
        self.den = bottom // gr_com_den

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction): #overload addition
        newnum = self.num*otherfraction.den + \
                      self.den*otherfraction.num
        newden = self.den * otherfraction.den        
        return Fraction(newnum, newden)
        

    def __eq__(self, other): #overload equality
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum
    
    def __mul__(self, otherfraction): #overload multiplication
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    
    def __rmul__(self, otherfraction): #overload rmultiplication
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __truediv__(self, otherfraction): #overload division
        reciprocal = Fraction(otherfraction.den, otherfraction.num)
        return self * reciprocal
    
    def __lt__(self, otherfraction): #overload ordering (less than)
        if self.den == otherfraction.den:
            return self.num < otherfraction.num
        else:
            leastcommon = lcm(self.den, otherfraction.den)
            newmenum = self.num * (leastcommon/self.den)
            newohternum = otherfraction.num * (leastcommon/otherfraction.den)
            return newmenum < newohternum
        
    def __gt__(self, otherfraction): #overload ordering (greater than)
        if self.den == otherfraction.den:
            return self.num > otherfraction.num
        else:
            leastcommon = lcm(self.den, otherfraction.den)
            newmenum = self.num * (leastcommon/self.den)
            newohternum = otherfraction.num * (leastcommon/otherfraction.den)
            return newmenum > newohternum

    def getNum(self): #get numerator
        return self.num

    def getDen(self): #get denominator
        return self.den

"""
x = Fraction(1,2)
y = Fraction(2,5)
print(x+y)
print(x == y)
print(x*y)
print(x/y)
print(x < y)
print(x > y)
print(x.getNum())
print(x.getDen())
"""        
t = Fraction(15, 105)
u = Fraction(3, 7)
print(t+u)

