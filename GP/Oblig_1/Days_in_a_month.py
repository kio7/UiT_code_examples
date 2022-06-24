print(f"On the next line i will ask for a number between 1 and 12. The number represents a month. E.g. 1 = Jan, 2 = Feb ect.")
month = int(input(f"Enter a month in the year: "))
year = int(input(f"Enter a year: "))

isLeapYear = (year % 4 == 0 and year % 100 != 0) or \
   (year % 400 == 0)

if month == 1:
    print(f"January {year} has 31 days.")
elif month == 2 and isLeapYear == False:
    print(f"February {year} has 28 days.")
elif month == 2 and isLeapYear == True:
    print(f"February {year} has 29 days.")
elif month == 3:
    print(f"March {year} has 31 days.")
elif month == 4:
    print(f"April {year} has 30 days.")
elif month == 5:
    print(f"May {year} has 31 days.")
elif month == 6:
    print(f"June {year} has 30 days.")
elif month == 7:
    print(f"July {year} has 31 days.")
elif month == 8:
    print(f"August {year} has 31 days.")
elif month == 9:
    print(f"September {year} has 30 days.")
elif month == 10:
    print(f"October {year} has 30 days.")
elif month == 11:
    print(f"November {year} has 30 days.")
elif month == 12:
    print(f"Desember {year} has 31 days.")
else:
    print(f"Invalid number.")