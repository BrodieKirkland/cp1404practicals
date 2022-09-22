TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
cents_per_kwh = 0
print("Electricity bill estimator")
tariff_choice = int(input("Which tariff? 11 or 31:"))
if tariff_choice == 11:
    cents_per_kwh = TARIFF_11
elif tariff_choice == 31:
    cents_per_kwh = TARIFF_31
# cents_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
estimate_bill = cents_per_kwh * daily_use_kwh * number_of_billing_days

print(f"Estimated bill: ${estimate_bill:.2f}")
