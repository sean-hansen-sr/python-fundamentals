#expenses = [10.50, 8, 5, 15, 20, 5, 3]
expenses = []
num_expenses = int(input("How many expenses do you want to enter?\n"))

for _ in range(num_expenses):
    expense = float(input("Enter an expense amount:\n"))
    expenses.append(expense)

total = sum(expenses)
#sum = 0

#for expense in expenses:
#    sum += expense

print("You spent $", total, sep = '')