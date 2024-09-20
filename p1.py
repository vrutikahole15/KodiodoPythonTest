class InvalidMarksException( Exception):
    def __init__(self,msg):
        self.msg=msg

try:
    percentage=float(input("enter a marks:"))

    if percentage < 0 or percentage > 100:
        raise InvalidMarksException("marks must be o to 100")
    print("you entered {marks}%")
except ValueError:
    print("invalid input!please enter a numeric value")

except InvalidMarksException as c:
    print(c)
    
    
        
