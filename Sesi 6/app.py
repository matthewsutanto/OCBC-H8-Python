def my_generator():
    print("Inside my generator")
    yield 'a'
    print("adfsafas")
    yield 'b'
    print("fdsafdas")
    yield 'c'

print(list(my_generator()))

for char in my_generator():
    print(char)
    
def counter_generator(low,high):
    while low<=high:
        yield low
        low+=1

# object_generator = counter_generator(5,10)
# print(next(object_generator))


for i in counter_generator(5,10):
    print(i, end=" ")
    

def inifinite_sequence():
    num=0
    while True:
        yield num
        num += 1
    
# for i in inifinite_sequence():
#     print(i, end=" ")

object_gen = counter_generator(5,10)

def say_hello(name):
    return f"hello {name}"

def be_awesome(name):
    return f"Yo {name} together we are awesome"

def weather_talk(name):
    return f"weather is nice, {name}"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print("\n"+greet_bob(say_hello))
print(greet_bob(be_awesome))
print(greet_bob(weather_talk))

def parent():
    print("From parent")
    
    def firstChild():
        print("From first child")
    
    def secondChild():
        print("From second child")
    
    firstChild()
    
parent()

import parent_return as pr
pr.parent(2)

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_whee():
    print("Whee!")

say_whee()