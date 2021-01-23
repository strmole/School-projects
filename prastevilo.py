num = int(input("Vnesi stevilko : "))
if num>1 :
    for i in range (2,num):
        if (num%i) ==0:
            print(num,"NI prastevilo")
            break
        else:
            print(num, "JE prastevilo")
            break
else:
    print(num,"NI prastevilo")