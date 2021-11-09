file = open('Hack8_Sample_Text.txt')
print(file)
file.close()

try:
    file = open('Hack8_Sample_Text.txt')
finally:
    print('closing the file')
    file.close()


with open("sample.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
   
f=open("sample.txt","r", encoding='utf-8')
data = f.read(4)
print(data)
data = f.read()
print(data)
f.close()

f=open("sample.txt","a", encoding='utf-8')
# data = f.read(4)
# print(data)

data = f.write('\n404\n')
print(data)

print("Coba tell")
with open("sample.txt","r", encoding='utf-8') as f:
    data = f.read(4)
    print(data)
    data = f.read(4)
    print(data)
    n=f.tell()
    print(n)
    
    f.seek(15)
    data = f.read(3)
    
    f.seek(0)
    for line in f:
        print(line, end = ' ')
        
    f.seek(0)
    data= f.readline()
    print(data)
    
# x=10
# if x>5:
#     raise Exception('x should not not exceed The value of x was: {}'.format(x))

# import sys
# print(sys.platform)
# assert('linux' in sys.platform), "This code is run on linux only"
# assert('windows' in sys.platform), "This code is run on windows only"


def check_coins(coins):
    assert( coins==10 ),"some coins"

coins = 8
   
# try:
#     check_coins(coins)
# except:
#     raise Exception('Some coins fall')

from os import error, read
import sys

def os_interaction():
    assert('linux' in sys.platform),"Only Linux"
    assert('win32' in sys.platform),"Only Windows"
    print("Doing something")

try:
    os_interaction()
    print("Masuk ke try Blok")
except:
    print(error)
    print("Masuk ke except blok")
else:
    print('Executing the clause else')
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    finally:
        print("cleaning up, irrespectifully")
        
    
# try:
#     with open('sample.txt') as file:
#         read_data = file.read()
#     n=10
#     print(n)
# except FileNotFoundError as error:
#     print(error)
#     print('%#')
# else:
#     print("Executing else clause")