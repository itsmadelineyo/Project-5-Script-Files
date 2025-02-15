>>> DOWN_PAYMENT_RATE = 0.10
>>> ANNUAL_INTEREST_RATE = 0.12
>>> MONTHLY_PAYMENTS_RATE = 0.05
>>> purchasePrice = float(input("Enter the purchase price: "))
Enter the purchase price: 100000
>>> month = 1
>>> payment = purchasePrice * MONTHLY_PAYMENTS_RATE
>>> startingBalance = purchasePrice
>>> print("\n%s%19s%18s%19s%10s%17s" % ("Month", "Starting Balance", "Interest to pay", "Principal to pay", "Payment", \"Ending Balance"))

Month   Starting Balance   Interest to pay   Principal to pay   Payment   Ending Balance
>>> while startingBalance > 0:
...     interestToPay = startingBalance * ANNUAL_INTEREST_RATE / 12
...     principalToPay = payment - interestToPay
...     endingBalance = startingBalance - payment
...     print("%2d%15.2f%16.2f%18.2f%18.2f%15.2f" % (month, startingBalance, interestToPay, principalToPay, payment, en\dingBalance))
...     startingBalance = endingBalance
...     month = month + 1
...
 1      100000.00         1000.00           4000.00           5000.00       95000.00
 2       95000.00          950.00           4050.00           5000.00       90000.00
 3       90000.00          900.00           4100.00           5000.00       85000.00
 4       85000.00          850.00           4150.00           5000.00       80000.00
 5       80000.00          800.00           4200.00           5000.00       75000.00
 6       75000.00          750.00           4250.00           5000.00       70000.00
 7       70000.00          700.00           4300.00           5000.00       65000.00
 8       65000.00          650.00           4350.00           5000.00       60000.00
 9       60000.00          600.00           4400.00           5000.00       55000.00
10       55000.00          550.00           4450.00           5000.00       50000.00
11       50000.00          500.00           4500.00           5000.00       45000.00
12       45000.00          450.00           4550.00           5000.00       40000.00
13       40000.00          400.00           4600.00           5000.00       35000.00
14       35000.00          350.00           4650.00           5000.00       30000.00
15       30000.00          300.00           4700.00           5000.00       25000.00
16       25000.00          250.00           4750.00           5000.00       20000.00
17       20000.00          200.00           4800.00           5000.00       15000.00
18       15000.00          150.00           4850.00           5000.00       10000.00
19       10000.00          100.00           4900.00           5000.00        5000.00
20        5000.00           50.00           4950.00           5000.00           0.00
