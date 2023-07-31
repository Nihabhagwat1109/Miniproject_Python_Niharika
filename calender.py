import calendar

year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

print(calendar.month(year, month))

days_in_month = calendar.monthrange(year, month)[1]
if days_in_month == 30:
    print(f"The month {calendar.month_name[month]} in {year} has 30 days.")
elif days_in_month == 31:
    print(f"The month {calendar.month_name[month]} in {year} has 31 days.")
else:
    print(f"The month {calendar.month_name[month]} in {year} has {days_in_month} days.")

