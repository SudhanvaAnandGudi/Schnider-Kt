print("The rightAngleTraingle pattern")
def right_triangle():
    rows = 6
    for i in range(1, rows ):
            for j in range(rows - i):
                print(" ", end=" ")
            for k in range(i):
                print("*", end=" ")
            print()
result = right_triangle()
print(result)

print("The pyramid pattern")
def pyramid():
     for i in range(1, 7+1):
          for j in range(7 - i):
               print(" ", end=" ")
          for k in range(i):
               print(" * ",end=" ")
          print()
result2 = pyramid()
print(result2)

print("The diamond pattern")
def diamond():
     for i in range(1, 7+1):
          for j in range(7 - i):
               print(" ", end=" ")
          for k in range(i):
               print(" * ",end=" ")
          print()
     for i in range(1, 7 + 1):
          for j in range(7-i):
               print(" * ",end=" ")
          
          for k in range(2*i-1):
               print( end=" "  )
          print()
          

result3 = diamond()
print(result3)