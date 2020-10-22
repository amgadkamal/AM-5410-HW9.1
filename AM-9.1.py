"""Calculator program with Python classes"""
#global input holders
a=b=0

#begin match functions
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def sqr(a,_):
    return a*a
#end match functions

def menu():
    #menus
    print("calculator type your operation: \n","+ \n","- \n","* \n","/ \n","^")
#end def menu
class Switcher(object):
          def indirect(self,i):
                   method_name='number_'+str(i)
                   method=getattr(self,method_name,lambda :'Invalid')
                   return method()

          def number_43(self):
                   return add
          def number_45(self):
                   return sub
          def number_42(self):
                   return mul
          def number_47(self):
                   return div
          def number_94(self):
                   return sqr
#end class Switcher

def operation(ch):
    s = Switcher()
    w = s.indirect(ch)
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    return w(a,b)
#end def operation

def main():
 menu()
 #input choise
 ch = ord(input("Enter Choice: "))
 ans=operation(ch)
 print(ans)
#end def main

if __name__ == '__main__':
    main()



