
#create class
class Circle:
    __pi = 3.141  #class private variable or attribute.private variable can be used only inside class

#constructor which takes list as argument
    def __init__(self):
        self.lists = [10,501,22,37,100,999,87,351]
    def cons(self):
        return self.lists

#Method for Area
    def area(self):
        for list in self.lists:
            a = self.__pi*(list**2)
            print("The area of radius", list, "=",a)
            
#Method name is perimeter but calculate radius as in question
    def perimeter(self):
        for list in self.lists:
            r = list/(2*self.__pi)
            print("The radius of circumference", list, "=", r)

#create object or instance of class
c = Circle()
#call the methods
c.area()
c.perimeter()
c.cons()