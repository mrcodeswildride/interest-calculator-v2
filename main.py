print()

principal = float(input("Enter the principal: $"))
apy = float(input("Enter the APY: "))
num_years = int(input("Enter years to keep money in account: "))

decimal = apy / 100
balance = principal

for n in range(num_years):
  interest = balance * decimal
  print(f"\nYear {n+1} interest: ${interest:,.2f}")

  balance = balance + interest
  print(f"Year {n+1} balance:  ${balance:,.2f}")

print(f"\n${principal:,.2f} grew to ${balance:,.2f} over {num_years} years.")
