
## Mendefinisikan sebuah fungsi

import math

def kuadrat(n):
    # def adalah keyword utk mendefinisikan sebuah fungsi
    # kuadrat adalah NAMA dari fungsi
    # n adalah Parameter (boleh lebih dari satu)
    return n**2

def akar_kuadrat(a, b, c):
    # ax^2 + bx + c
    D = b**2 - 4*a*c
    if a>0:
       if D>0:
           ##   a >0 & D > 0
           x1 = (-b + math.sqrt( D ) ) /(2.0*a)
           x2 = (-b - math.sqrt( D ) ) /(2.0*a)
           print("x1 = %f " %(x1) )
           print("x2 = %f " %(x2) )
       else:
           print("Nilai D tidak boleh NEGATIF")
    else:
        print ("nilai a tidak boleh NOL")
        
    

class Fraction:
    def __init__(self, top, bottom):
      self.num = top
      self.den = bottom
    def show(self):
      print(self.num, "/", self.den)
      print("%d/%d" %(self.num,self.den) )
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
        

f1 = Fraction(3,5)   # 3 > top,  5 > bottom
f2 = Fraction(2,10)
f3 = f1 + f2;

print( f3 )



    




