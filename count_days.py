"""Get the number of days
in the current month """
import calendar
import datetime

# Get the current date
current_date = datetime.datetime.now()

# Extract the current year and month
current_year = current_date.year
current_month = current_date.month

# Get the number of days in the current month
days_in_month = calendar.monthrange(
    current_year,
    current_month)[1]

# Get the name of the current month
month_name = current_date.strftime('%B')

# Display the information
print(f"Year: {current_year}")
print(f"Month: {month_name}")
print(f"""Number of Days in {month_name}:
      {days_in_month}""")



