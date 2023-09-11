rate = float(input("Current exchange rate for the Euro to Dollar: "))
amount = float(input("Amount of currency that you want to exchange: "))
total = rate * amount
print("Total:", total)
service_fee = 3.0
result = total - service_fee
print("Result:", result)