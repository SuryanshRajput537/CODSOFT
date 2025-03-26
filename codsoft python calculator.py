print("---CALCULATOR---")

# lets create a function of calculator so that we don't have to write code again and again:-

def calculator():
    while True:
        num1=float(input("enter the first number:"))
        num2=float(input("enter the second number:"))

        print("press '1' for Addition(+)")
        print("press '2' for Subtraction(-)")
        print("press '3' for Multiplication(*)")
        print("press '4' for Division(/)")
       

        operation=(input("enter your choice from 1 to 4:"))
               
        
        if operation not in ('1','2','3','4'):
            print("Invalid output, please choose correct option from 1 to 4")
            continue
        
    
    
        if operation =='1':
            result=num1+num2
            print(f"the Addition of {num1} and {num2} is {result} ")
            
    
        elif operation =='2':
            result=num1-num2
            print(f"the Subtraction of {num1} and {num2} is {result} ")
            
    
        elif operation =='3':
            result=num1*num2
            print(f"the Multiplication of {num1} and {num2} is {result} ")
           
        
            
    
        elif operation =='4':
            if num2 ==0:
                print("Error!,Division by zero is not allowed")
            else:
                result=num1/num2
                print(f"the Division  of {num1} and {num2} is {round(result,2)} ")
            
    
calculator()