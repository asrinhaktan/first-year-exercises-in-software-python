#class of mathematical operations
import math
class math_class():
    numpi = math.pi
    def addition(self, value1,value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1 + self.value2
    def Extraction_process(self, value1,value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1 - self.value2
    def Multiplication(self, value1,value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1 * self.value2
    def Division(self, value1,value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1 / self.value2
    def FindMode(self, value1,value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1 // value2
    def Sinus(self, valsin):
        self.valsin = valsin
        return math.sin(valsin)
    def Cosinus(self,valcos):
        self.valcos = valcos
        return math.cos(valcos)
    def Square(self, value):
        self.value = value
        return self.value * self.value
    def SquarePerCal(self, value):
        self.value = value
        return self.value * 4
    def RectangularCal(self, value1,value2):
        self.value1 = value1
        self.value2 = value2
        return self.value1*value2
    def RectangularEnvCal(self, value1,value2):
        self.value1 = value1
        self.value2 = value2
        return (self.value1*2)+(self.value2*2)
    def TriangleEnvCal(self, value1,value2,value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        return (self.value1+self.value2+self.value3)
    def TriangleArCal(self, value1,value2):
        self.value1 = value1
        self.value2 = value2
        return (self.value1*self.value2)/2
    def Circumference(self, value,numpi):
        self.value = value
        return self.value*2*numpi
    def CircleAr(self, value,numpi):
        self.value = value   
        return (self.value*self.value)*numpi
    

class transactions(math_class):
    numpi = math.pi
    print("---------------------------------------\nSimple Calculator\n---------------------------------------")
    while True:
        choose = input("please select the action you want to do\n 1-Addition\n 2-Substract\n 3-Multiplication\n 4-Division\n 5-Find Mode\n 6-Sinus angle\n 7-Cosinus angle\n 8-Area of the square\n 9-Perimeter of the square\n 10-rectangular area calculation\n 11-Rectangular perimeter calculation\n 12-Triangular perimeter calculation\n 13-triangular area calculation\n 14-Circle perimeter calculation\n 15-circle area calculation\n press q to exit\n What is the transaction number you want to choose? : ")
        if choose =="q":
            print("Leaving...")
            break
        else:
            if choose == "1":
                valuea = int(input("enter the first number : "))
                valueb = int(input("enter the second number : "))
                print("Transaction result :",math_class().addition(valuea,valueb))
            elif choose == "2":
                valuea = int(input("enter the first number : "))
                valueb = int(input("enter the second number : "))
                print("Transaction result :",math_class().Extraction_process(valuea,valueb))
            elif choose == "3":
                valuea = int(input("enter the first number : "))
                valueb = int(input("enter the second number : "))
                print("Transaction result :",math_class().Multiplication(valuea,valueb))
            elif choose == "4":
                valuea = int(input("enter the first number : "))
                valueb = int(input("enter the second number : "))
                print("Transaction result :", math_class().Division(valuea,valueb))    
            elif choose == "5":
                valuea = int(input("enter the first number : "))
                valueb = int(input("enter the second number : "))
                print("Transaction result :",math_class().FindMode(valuea,valueb))
            elif choose == "6":
                valsin = int(input("enter the extent : "))
                print("Transaction result :",math_class().Sinus(valsin))
            elif choose == "7":
                valcos = int(input("enter the angle : "))
                print("Transaction result :",math_class().Cosinus(valcos))
            elif choose == "8":
                valuea = int(input("enter the number : "))
                print("Transaction result :",math_class().Square(valuea))
            elif choose == "9":
                valuea = int(input("enter one side of the square : "))
                print("Transaction result :",math_class().SquarePerCal(valuea))
            elif choose == "10":
                valuea = int(input("enter one side of the rectangular : "))
                valueb = int(input("enter the other side of the rectangular : "))
                print("Transaction result :",math_class().RectangularCal(valuea,valueb))
            elif choose == "11":
                valuea = int(input("enter one side of the rectangular : "))
                valueb = int(input("enter the other side of the rectangular : "))
                print("Transaction result :",math_class().RectangularEnvCal(valuea,valueb))
            elif choose == "12":
                valuea = int(input("Enter the length of the first side of the scalene triangle : "))
                valueb = int(input("Enter the length of the second side of the scalene triangle : "))
                valuec = int(input("Enter the length of the third side of the scalene triangle : "))
                print("Transaction result :",math_class().TriangleEnvCal(valuea,valueb,valuec))
            elif choose == "13":
                valuea = int(input("enter the first side of the right triangle : "))
                valueb = int(input("enter the second side of the right triangle : "))
                print("Transaction result :",math_class().TriangleArCal(valuea,valueb))
            elif choose == "14":
                valuea = int(input("enter the radius value : "))
                print("Transaction result : ",math_class().Circumference(valuea,numpi))
            elif choose == "15":
                valuea = int(input("enter the radius value : "))
                print("Transaction result :",math_class().CircleAr(valuea,numpi))


                
                
                









                
                    
            
                
                
                
                
                
                
                
                
                
                
                


            


   

    
        






    
