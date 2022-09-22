"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
LOW_BONUS_RATE = .10
HIGH_BONUS_RATE = .15
SALES_BONUS_THRESHOLD = 1000
total_bonus = 0

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < SALES_BONUS_THRESHOLD:
        total_bonus = sales * LOW_BONUS_RATE
    else:
        total_bonus = sales * HIGH_BONUS_RATE
    print(f"For ${sales:.2f} in sales, you get a ${total_bonus:.2f} bonus!")
    sales = float(input("Enter sales: $"))
print("Fin.")
