import random
 
arrayexample = [1,2,3,4,5]

for i in range(5):
    arrayexample[i]=int(random.uniform(100, 200))
    print(arrayexample[i-1])

    varInput=int(input("Ingrese el valor:"))
    print(varInput)

    for i in range(5):
        if arrayexample[i]>= varInput:
            print("el valor del arreglo es mayor")
        else:
            print("el valor del arreglo es menor"git init)  
        print(str(arrayexample[i])+">"+str(varInput))     
