string = input("Vstavite besedo : ")
rev_string = string[::-1]
print("Obrnjeno:",rev_string)
if string == rev_string:
    print("beseda JE palindrom")
else:
    print("beseda NI palindrom")