iteration = int(input("Enter how many number you will input ? = "))
stopNumber = int(input("Number when the variable will be stop ? = "))
numberValue = []

for x in range(iteration):
    number = str(x+1)
    numberValue.append(int(input("Enter number for index-"+number+"= ")))
isFinish = False   
i = 0
while not isFinish and i<iteration:
    if numberValue[i]==stopNumber:
        isFinish = True
        print("Done")
    elif numberValue[i]%2==0:
        print(numberValue[i])
    i+=1
if isFinish==False:
    print("Stop number isn't found in list")