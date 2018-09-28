days = int(input("how many days wil you work for a pennies a day?: "))
penny = 2
print("Days Worked | Amount Earned That day")
for time in range(days):
    print(time, "| $      ", penny ** time / 100)
