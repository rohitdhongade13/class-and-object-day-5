import numpy as np
from scipy import stats
class math_op :
    
    def __init__(self,n1=0,n2=0,n3=0,n4=0,n5=0):
        list1 =[n1,n2,n3,n4,n5]
        


        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.list1 = list1

        


    def addition(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        print(f'Addition is = {self.n1 + self.n2 + self.n3 + self.n4 + self.n5}\n')

    
    def subtraction(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        print(f'subtraction is = {self.n1 - self.n2 - self.n3 - self.n4 - self.n5}\n')



    def multiplication(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        print(f'multiplication is = {self.n1 * self.n2 * self.n3 * self.n4 * self.n5}\n')

    def division(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        print(f'division is = {self.n1 / self.n2 / self.n3 / self.n4 / self.n5}\n')


    def mode(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        l1 = stats.mode(self.list1)

        print(f'mode is = {l1}'"\n")



    def mean(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        x = np.mean(self.list1)

        print(f'mean is = {x}\n')


    def min(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        x = min(self.list1)
        print(f'min is = {x}\n')


    def max(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        x = max(self.list1) 
        print(f'max is = {x}\n')


    def medain(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        x = np.median(self.list1)
        print(f'medain is = {x}\n')


    def per_75(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        x = np.percentile(self.list1, 75)
        print(f'per_75% is = {x}\n')

    def per_50(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        x = np.percentile(self.list1, 50)
        print(f'per_50% is = {x}\n')

    def per_25(self):
        print(f'your enter value are {self.n1, self.n2, self.n3, self.n4, self.n5}\n')
        x = np.percentile(self.list1, 25)
        print(f'per_25% is = {x}\n')

    
a = float(input("ENTER THE NUMBER - "))
b = float(input("ENTER THE NUMBER - "))
c = float(input("ENTER THE NUMBER - "))
d = float(input("ENTER THE NUMBER - "))
e = float(input("ENTER THE NUMBER - "))
print()


m = math_op(a,b,c,d,e)

m.division()
m.multiplication()
m.addition()
m.subtraction()
m.mean()
m.mode()
m.medain()
m.min()
m.max()
m.per_25()
m.per_50()
m.per_75()
print()
