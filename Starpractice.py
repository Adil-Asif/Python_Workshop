
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
   

triangle(5)