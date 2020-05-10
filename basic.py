def main():
    hieght = int(input("Enter Hieght: "))
 
    for i in range(0,hieght):
         
        for j in range(0,i+1):
             print("*",end= "" )
        print("")         


if __name__ == "__main__":
    main()    