while True:
    try:
        base = int(input("What is the base size? "))
        if base <= 0:
            print("Size must be greater than 0!")
            continue
        break
    except ValueError:
        print("Insert only numbers!")
        continue    
while True:
    shape = str(input("What is the triangle shape? "))
    if len(shape) > 1:
        print("Insert only 1 character!")
        continue
    else:
        break
while True:
    try:
        spacing_size = int(input("What is the spacing size? "))
        if spacing_size < 0:
            print("Spacing cannot be negative!")
            continue
        break
    except ValueError:
        print("Insert only numbers!")
        continue
space = ""
for i in range(spacing_size):
    space = space + " "
shape = f"{shape}{space}"
for i in range(base):
    print(shape)
    shape = shape + f"{shape[0]}{space}"
