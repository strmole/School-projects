tree_height = input("Velikost smrekce : ")
tree_height = int(tree_height)
spaces = tree_height-1
stars = 1
stump_spaces = tree_height-1

while tree_height != 0 :
    for i in range(stars):
        print('*', end="")
    print()
    tree_height -= 1
    stars += 1

