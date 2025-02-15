>>> startSal = float(input("Enter the starting salary: $"))
Enter the starting salary: $45000
>>> increase = int(input("Enter the annual increase: "))
Enter the annual increase: 3
>>> years = int(input("Enter the number of years: "))
Enter the number of years: 7
>>> print("Year   Salary   Stipend\n------------------------")
Year   Salary   Stipend
------------------------
>>> multiplier = 1 + increase / 100
>>> nextSal = startSal
>>> for year in range(1, years + 1):
...     stipend = 1000
...
>>> totalSalary = nextSal + stipend
>>> print("%2d%10.2f%10.2f" % (year, nextSal, totalSalary))
 7  45000.00  46000.00
>>> nextSal *= multiplier
