def get_personal(name,age):
    pass

def save_personal(name,age=18):
    print('name',name)
    print('age',age)

get_personal('ani',22)

save_personal('adi',27)

save_personal(name='udin',age=54)

def buy(customer_name, *items):
    pass

# Example of Function Creation

def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)

my_function(25,5)

def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
   
# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

# Now you can call printme function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

# Function definition is here
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = mylist+[1,2,3,4]
   print("\nValues inside the function : ", mylist)
   return mylist

# Now you can call changeme function
mylist = [10,20,30]
print("\nValues outside the function - before : ", mylist)
mylist = changeme( mylist )
print("\nValues outside the function - after  : ", mylist)

# Function definition is here
def changeme( mylist ):
   '''This changes a passed list into this function'''
   mylist = [1, 2, 3, 4] # This would assign new reference in mylist
   print("Values inside the function  : ", mylist)

# Now you can call changeme function
mylist = [10, 20, 30]
changeme( mylist )
print("Values outside the function : ", mylist)

# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)
 
# Now you can call printme function
printme("Hello")

# # This syntax will give you an error
# printme()

# Function definition is here
def calculate_rect(length, width):
  '''This function is used to calculate area of rectangle'''
  print('Area : ', length*width)

# Define parameters
length = 100
width = 20

# Call calculate_rect
calculate_rect(length, width)

# # This syntax will give you an error
# calculate_rect(length)

# Function definition is here
def printme( str_input ):
   '''This prints a passed string into this function'''
   print(str_input)

# Now you can call printme function
printme(str_input = "Hacktiv8")

# Function definition is here
def printinfo( name, age ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age. : ", age)

# Now you can call printinfo function
printinfo( age=4, name="a" )

# Function definition is here
def printinfo( name, age = 26 ):
   '''This prints a passed info into this function'''
   print("Name : ", name)
   print("Age  : ", age)
   print("")

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

# Function definition is here
def printinfo( arg1, *vartuple ):
# def printinfo(arg1, arg2, arg3, arg4):
   '''This prints a variable passed arguments'''
   print('arg1     : ', arg1)
   print('vartuple : ', vartuple)
   print('')
   
   for var in vartuple:
      print('isi vartuple : ', var) 

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50, "a" )

def sum(num1,num2):
    pass
sum = lambda num1,num2: num1+num2

import person
print(person.display('Good Night'))

from person import name,devices
    