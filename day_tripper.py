def compute_day_of_week(date):
    day, month, year = date
    century = year // 100
    year_part = year % 100
    
    # Compute Century-Item
    if year < 1752 or (year == 1752 and (month < 9 or (month == 9 and day < 14))):
        century_item = (18 - century) % 7
    else:
        century_item = ((3 - (century % 4)) * 2) % 7
    
    # Compute Year-Item
    year_item = (year_part + (year_part // 4)) % 7
    
    # Compute Month-Item
    month_items = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    month_item = month_items[month - 1]
    
    # Compute Day-Item
    day_item = day % 7
    
    # Total
    total = (century_item + year_item + month_item + day_item) % 7
    
    # Correction for Leap Year
    if month <= 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        total = (total - 1 + 7) % 7
    
    return total

def day_of_week_string(day_index):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    return days[day_index]

# Prompt for the date 
date_input = input("Enter a date (yyyy-mm-dd): ")
year, month, day = map(int, date_input.split('-'))
date = (day, month, year)

# Compute and print the day of the week
day_index = compute_day_of_week(date)
day_name = day_of_week_string(day_index)
print(f"The day of the week for {date_input} is {day_name}.")
