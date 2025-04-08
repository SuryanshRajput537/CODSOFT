print("---CALCULATOR---")

# lets create a function of calculator so that we don't have to write code again and again:-

def calculator():
    while True:
        print("press '1' for ADDITION")
        print("press '2' for SUBTRACTION")
        print("press '3' for MULTIPLICATION")
        print("press '4' for DIVISION")
        print("press '5' to EXIT")
        
        
        operation=(input("enter your choice from 1 to 5:"))
        
        if operation == '5':
            print("Exiting the contact book.thankyou for using CODSOFT CONTACTBOOK!!")
            break
        else:
            num1=float(input("enter the first number:"))
            num2=float(input("enter the second number:"))
         
         
         
               
        
        if operation not in ('1','2','3','4','5'):
            print("Invalid output, please choose correct option from 1 to 4")
           
    
    
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
