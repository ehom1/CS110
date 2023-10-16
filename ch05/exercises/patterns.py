def star_pyramid():
    rows = int(input("Please enter how many rows you wish to have: "))
    for i in range(1, rows + 1):
        print('*' * i)

star_pyramid()

def rstar_pyramid():
    rows = int(input("Please enter how many rows you wish to have in reverse: "))
    for i in range(rows, 0, -1):
        print('*' * i)
        
rstar_pyramid()