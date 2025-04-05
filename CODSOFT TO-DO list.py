print("---TO-DO LIST---")

def TO_DO_LIST():
    tasks=[]
    while True:
    
        print("press '1' to ADD NEW TASK")
        print("press '2' to DELETE A TASK")
        print("press '3' to SHOW TASKS")
        print("press '4' to EXIT")
       

        choice=(input("enter your choice from 1/2/3/4:"))
         
         
          
        
        if choice not in ('1','2','3','4'):
            print("Invalid output, please choose correct option from 1 to 4")
           
    
    
        if choice =='1':
            task=input("enter the task to add:")
            if task in tasks:
                print(f"The task {task} already exists in the list")
            else:
                tasks.append(task)
                print(f"The task {task} has been added successfully")    
    
        elif choice =='2':
            task=input("enter the task you want to delete:")
            if task in tasks:
                tasks.remove(task)
                print(f"The task {task} has been removed from the list.")
            else:
                print(f"The task {task} is not in the list")
                    
            
    
        elif choice =='3':
            if not tasks:
                print("No tasks to display.")
            else:
                print("tasks:")
                for task in tasks:
                    print("-->" + task)    
            
            
           
        
            
    
        elif choice =='4':
            break
                
            
    
TO_DO_LIST()