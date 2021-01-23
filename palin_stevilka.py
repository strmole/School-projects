number = int(input("Vnesite stevilko : "))
string = str(number)
rev_string = string[::-1]
print("Obrnjeno : ", rev_string)
if string == rev_string:
    print("stevilo JE palindrom")
else:
    print("stevilo NI palindrom")