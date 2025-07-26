meal = []

while True:  # This statement will run the loop. when operation performe.
    print("What do you want to do?")
    print("1. Add a new meal")
    print("2. View all meal")
    print("3. Delete a meal")
    print("4. Exit")

    operation = int(input("What you want? (1,2,3,4) "))  # input from user

    if (operation == 1):  # Add new reminder
        breakfast = input("What you will be eat in breakfast? ")
        lunch = input("what you will be eat in lunch? ")
        dinner = input("what you will be eat in dinner? ")
        day_plan = (breakfast, lunch, dinner)
        meal.append(day_plan)

        print("meal Added")

    elif (operation == 2):  # print all reminders
        if len(meal) == 0:
            print("No meal are added yet! ")
        else:
            for b, l, d in meal:
                print("Breakfast", b, "|" "Lunch", l, "|" "Dinner", d)

    elif (operation == 3):  # remove complete meal
        meal.clear()
        print("complete meal list removed.")

    elif (operation == 4):  # this will end the the process
        print("Good by")
        break

    else:
        print("Invalid input. Please enter (1,2,3,4): ")
