a=int(input("enter starting year for leap year"))
b=int(input("enter the ending year for the leap year search"))
print(f"{a}"" to "f"{b} leap year are")
for year in range(a, b+1):
    if (year % 4 == 0 and year % 100 !=0):
        print(f"{year}  ")
