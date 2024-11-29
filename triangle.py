def check_right_triangle(sides):
    sides.sort()
    if sides[2]**2 == sides[0]**2 + sides[1]**2:
        return True
    return False

sides=[]
sides.append(int(input("Enter the length of the first side")))
sides.append(int(input("Enter the length of the second side")))
sides.append(int(input("Enter the length of third side")))
if check_right_triangle(sides):
    print("the given sides are part of the given triangle")
else:
    print("the given sides are not part of the given triangle")