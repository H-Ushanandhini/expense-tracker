expenses=[]
class Expenses:
    def add_exp(self):
        date=input('Enter Date (YYYY-MM-DD):')
        category=input("Enter Category (Food /Travel /Shopping):")
        amount=int(input("Enter amount:"))
        with open('expenses.txt','a')as file:
            file.write(f'{date},{category},{amount}\n')
        
    def view_exp(self):
        with open('expenses.txt','r')as file:
            for line in file:
                data=line.strip().split(',')
                if len(data)==3:
                    date=data[0]
                    category=data[1]
                    amount=data[2]
                    print('Date:',date,'|Category:',category ,'|Amount:',amount)
    
    def total_exp(self):
        total=0
        with open('expenses.txt','r')as file:
            for line in file:
                data=line.strip().split(',')
                if len(data)==3:
                    amount=int(data[2])
                    total+=amount
        
        print('Total Expenses:',total)

def main():
    e=Expenses()
    while True:
        print('1. Add Expenses \n2. View Expenses \n3. Total Expenses \n4. Exit')
        choice=input('Ener your Choice:')
        if choice=='1':
            e.add_exp()
        elif choice=='2':
            e.view_exp()
        elif choice=='3':
            e.total_exp()
        elif choice=='4':
            print('Thank You!')
            break
        else:
            print('Invalid choice')
main()
