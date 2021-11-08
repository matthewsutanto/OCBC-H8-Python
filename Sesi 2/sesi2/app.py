x=0
y=5

if x<y:
    print("Yes")
    
if y<x:
    print("No")
    
# weather = 'nice'
weather = 'cloudy'

if weather == 'nice':
    print('Mow the lawn')
    print('Take the garden')
    
uang = 5000
hargaBuku = 10000
print("Beli buku") if uang>hargaBuku else print('uang tidak cukup')

print('#23')
a=['foo','bar']
while len(a) :
    print(a.pop(0))
    b=['baz','quz']
    
    while len(b):
        print('>', b.pop(0))
        
x = range(0,100,20)
for n in x:
    print(n)
    
d={'foo':1, 'bar':2, 'baz':3}

for key,value in d.items():
    print(key+" "+str(value))