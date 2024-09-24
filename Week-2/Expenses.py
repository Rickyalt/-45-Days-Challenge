food=[]
transport=[]
entertainment=[]
choice=input("To categorise you expenses, Please press the following keys to categorise them-F for food, T for transport, E for entertainment:")
if choice=='f' or choice=='F':
    n=int(input("Enter the number of food expenses:"))
    for i in range(n-1):
        food=input("Enter your food expense:")
    sumf=sum(food)

elif choice=='T' or choice=='t':
    n=int(input("Enter the number of transport expenses:"))
    for i in range(n-1):
        transport=input("Enter your transport expense:")
    sumt=sum(transport)

elif choice=='e' or choice=='E':
    n=int(input("Enter the number of entertainment expenses:"))
    for i in range(n):
        entertainment=input("Enter your entertainment expense:")
    sume=sum(entertainment) 

else:
    print("Invalid choice")

print("Food Expenses:",sumf,"Transport Expenses:",sumt,"Entertainment Expenses:",sume)