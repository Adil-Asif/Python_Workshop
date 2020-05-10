class Ab:
    __x=0
    y=0
    def __init__ (self):
        self.__x=5
        self.y=5

    
def checking():
        ab = int(input("Enter Value: "))

        if (ab == 1) or (ab == 3):
            print("Good Morning")
        elif (ab == 2) or (ab == 4):
            print("Hello World")
        else:
              print("Have a nice sleep")
                



aab= Ab()

checking()
