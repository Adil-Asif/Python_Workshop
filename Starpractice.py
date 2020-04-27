
def right_triangle(n):
    for i in range(1,n+1):
           
        for j in range(0,i):
            print('* ',end = '')
        print("")    
    
def left_triangle(n):
    for i in range(n,0,-1):
        for j in range(0,i):
            print("* ",end = '')
        print("")
            
def triangle(n):
    for i in range(1,n+1):
        for x in range(0,n-i):
            print(' ', end = '')
        for j in range(0,i):
            print("* ",end = '')
        print('')        
   


print("1) Right Triangle\n2) Left Triangle\n3) Triangle")
choice = input("Enter your choice: ")
n = input("Enter Hieght of Triangle of your choice: ")

if choice == '1':
    right_triangle(int(n))
elif choice == '2':
    left_triangle(int(n))
elif choice == '3':
    triangle(int(n))