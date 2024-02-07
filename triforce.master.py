height = int(input("Number of rows: "))
x = 1
while x <= height:  
    spaces = " " * (height - x)  
    triangles = " ▲" * x  
    print(spaces + triangles)  
    x += 1
