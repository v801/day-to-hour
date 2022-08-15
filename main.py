calculation_to_hours = 24
name_of_unit = "hours"

# takes int days and returns string with calculation
def days_to_units(days):
    return f"{days} days is: {days * calculation_to_hours} {name_of_unit}."

# validate input and execute
def validate_and_execute():
    try:
        # check if set item is an int
        input_num = int(num_of_days_element)
        if input_num > 0:
            get_hours = days_to_units(input_num)
            print(f"{get_hours}\n")
        else:
            print("Please choose a positive number.")
    except ValueError:
        print("error")

user_input = ""
# run until input is "exit"
while user_input != "exit":
    user_input = input("Enter a number of days in a comma separated list and I will convert it to hours.\n")
    # split input at comma and store as a set
    list_of_days = user_input.split(", ")
    # iterate through items in the set and run validate function
    for num_of_days_element in set(list_of_days):
        validate_and_execute()