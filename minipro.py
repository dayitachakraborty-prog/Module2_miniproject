from datetime import datetime, timedelta

# Estimated review periods according to food category

expiry_periods = {
    "Dairy Products": (14, 21),
    "Poultry Products": 7,
    "Bakery Products": 30,
    "Beverages": 30,
    "Confectionery": 30,
    "Preserves": (60, 90),
    "Vegetables": 7
}


# Default fridge inventory organised by category
# Each item contains its purchase date and quantity.

default_items = {

    "Dairy Products": {
        "Milk": {"date": "05-11-2026", "quantity": "1 litres"},
        "Cheese": {"date": "31-10-2026", "quantity": "250 grams"},
        "Butter": {"date": "31-10-2026", "quantity": " 500 grams"}
    },

    "Poultry Products": {
        "Eggs": {"date": "04-11-2026", "quantity": "12 pieces"},
        "Meat": {"date": "06-11-2026", "quantity": "750 g"}
    },

    "Bakery Products": {
        "Bread": {"date": "04-11-2026", "quantity": "2 packets"}
    },

    "Beverages": {
        "Juice": {"date": "19-10-2026", "quantity": "2 litres"}
    },

    "Confectionery": {
        "Chocolate1": {"date": "17-10-2026", "quantity": "6 bars"},
        "Chocolate2": {"date": "15-08-2026", "quantity": "1 box"},
        "Candy": {"date": "15-08-2026", "quantity": "1 bag"},
        "Sweets": {"date": "02-11-2026", "quantity": "200 grams"}
    },

    "Preserves": {
        "Pickles": {"date": "15-06-2026", "quantity": "3 jars"}
    },

    "Vegetables": {
        "Vegetables": {"date": "04-11-2026", "quantity": "2 kg"}
    }
}


# Separate dictionary for items added by the user

new_items = {}


# Food categories

categories = {
    "1": "Dairy Products",
    "2": "Poultry Products",
    "3": "Bakery Products",
    "4": "Beverages",
    "5": "Confectionery",
    "6": "Preserves",
    "7": "Vegetables"
}


# Displaying the default fridge inventory

print("\n========== DEFAULT FRIDGE INVENTORY ==========")

for category in default_items:

    print(f"\n----- {category.upper()} -----")

    for item in default_items[category]:

        details = default_items[category][item]

        print(
            f"{item} : Purchased on {details['date']} | "
            f"Quantity: {details['quantity']}"
        )


# Adding new items

print("\n========== ADD NEW ITEMS ==========")

choice = input(
    "Would you like to add new items? (Yes/No): "
).strip().lower()


if choice == "yes":

    while True:

        try:

            number = int(
                input("How many items altogether would you like to add? ")
            )

            if number > 0:
                break

            print("Please enter a number greater than zero.")

        except ValueError:

            print("Please enter a valid whole number.")


    for i in range(number):

        print(f"\nEnter details for item {i + 1}:")


        # Selecting the food category

        print("\nChoose the food category:")

        for key, value in categories.items():

            print(f"{key}. {value}")


        while True:

            category_choice = input(
                "Enter your choice (1-7): "
            ).strip()

            if category_choice in categories:

                category = categories[category_choice]
                break

            print("Invalid choice. Please enter a number from 1 to 7.")


        # Entering the food item's name

        while True:

            item = input(
                "Enter the food item's name: "
            ).strip()

            if not item:

                print("Item name cannot be empty.")

            elif any(
                item.lower() == existing.lower()
                for group in (default_items, new_items)
                for category_items in group.values()
                for existing in category_items
            ):

                print("This item already exists!")

            else:

                break


        # Entering the food item's quantity

        while True:

            quantity = input(
                "Enter the quantity "
                "(e.g., litres, grams, boxes): "
            ).strip()

            if quantity:

                break

            print("Quantity cannot be empty.")


        # Entering the purchase date

        while True:

            date = input(
                "Enter the purchase date (DD-MM-YYYY): "
            ).strip()

            try:

                datetime.strptime(date, "%d-%m-%Y")
                break

            except ValueError:

                print("Invalid date. Please try again.")


        # Storing the new item under its category

        if category not in new_items:

            new_items[category] = {}

        new_items[category][item] = {
            "date": date,
            "quantity": quantity
        }

        print("Item successfully added!")


elif choice == "no":

    print("No new items will be added.")

else:

    print("Invalid choice. No new items will be added.")


# Combining both inventories

complete_inventory = {}

for category in default_items:

    complete_inventory[category] = {
        **default_items[category],
        **new_items.get(category, {})
    }


# Displaying the complete refreshed fridge inventory

print("\n========== COMPLETE FRIDGE INVENTORY ==========")

for category in complete_inventory:

    print(f"\n----- {category.upper()} -----")

    for item in complete_inventory[category]:

        details = complete_inventory[category][item]

        print(
            f"{item} : Purchased on {details['date']} | "
            f"Quantity: {details['quantity']}"
        )


# Automatically obtaining the current date

user_date = datetime.today()

print(
    "\nToday's date is:",
    user_date.strftime("%d-%m-%Y")
)


# Checking estimated review dates

print("\n========== FOOD REVIEW REPORT ==========")

for category in complete_inventory:

    period = expiry_periods[category]

    if isinstance(period, tuple):

        days_to_add = period[0]

    else:

        days_to_add = period


    for item in complete_inventory[category]:

        details = complete_inventory[category][item]

        purchase_date = datetime.strptime(
            details["date"],
            "%d-%m-%Y"
        )

        quantity = details["quantity"]

        review_date = purchase_date + timedelta(
            days=days_to_add
        )

        days_left = (
            review_date.date() - user_date.date()
        ).days


        if days_left < 0:

            print(
                f"\nThe {item} (Quantity: {quantity}) "
                f"has expired its estimated review date."
            )

        elif 0 <= days_left <= 4:

            print(
                f"\nPlease review the {item} "
                f"(Quantity: {quantity}) soon."
            )

        else:

            print(
                f"\n{item} (Quantity: {quantity}) "
                f"is not yet due for review. "
                f"Days remaining: {days_left}"
            )


# Recipe Dictionary

recipes = {
    "Veg": {
        "Dal": {
            "Ingredients": ("Dal", "Water", "Salt", "Turmeric", "Spices"),

            "Steps": [
                "Step 1: Wash the dal properly with clean water.",
                "Step 2: Put the dal in a pot with water and cook until it becomes soft.",
                "Step 3: Add salt, turmeric and other spices according to taste.",
                "Step 4: Mix everything well.",
                "Step 5: Serve the dal hot with rice."
            ]
        },

        "Cucumber Sandwich": {
            "Ingredients": ("Bread", "Butter", "Cucumber", "Salt", "Pepper", "Tomato Ketchup"),

            "Steps": [
                "Step 1: Take two slices of bread and spread a little butter on them.",
                "Step 2: Wash and cut the cucumber into thin round slices.",
                "Step 3: Arrange the cucumber slices on one slice of bread.",
                "Step 4: Sprinkle a little salt and pepper, then cover with the other slice.",
                "Step 5: Cut the sandwich into halves.",
                "Step 6: Serve fresh with tomato ketchup."
            ]
        },

        "Aloo Paratha": {
            "Ingredients": ("Potatoes", "Wheat Flour", "Salt", "Coriander", "Spices", "Curd", "Pickle"),

            "Steps": [
                "Step 1: Boil the potatoes, peel them and mash them properly.",
                "Step 2: Add salt, chopped coriander and spices to the mashed potatoes.",
                "Step 3: Take a small ball of dough and flatten it slightly.",
                "Step 4: Place some potato filling in the centre and close the dough.",
                "Step 5: Roll it gently into a flat paratha.",
                "Step 6: Cook on a pan until golden on both sides.",
                "Step 7: Serve hot with curd or pickle."
            ]
        }
    },

    "Non-Veg": {
        "Egg Roll": {
            "Ingredients": ("Wheat Flour", "Egg", "Salt", "Onion", "Cucumber", "Sauce"),

            "Steps": [
                "Step 1: Prepare a thin roti using wheat flour.",
                "Step 2: Beat an egg with a little salt and pour it into a heated pan.",
                "Step 3: Place the roti over the egg while it is cooking.",
                "Step 4: Flip it carefully so that the roti gets lightly cooked.",
                "Step 5: Add sliced onion, cucumber and sauce.",
                "Step 6: Roll it up properly.",
                "Step 7: Serve hot with drinks."
            ]
        },

        "Fish Fry": {
            "Ingredients": ("Fish", "Salt", "Turmeric", "Chilli Powder", "Lemon Juice", "Flour", "Breadcrumbs", "Mustard"),

            "Steps": [
                "Step 1: Clean the fish pieces properly and remove excess water.",
                "Step 2: Mix salt, turmeric, chilli powder and lemon juice to prepare a marinade.",
                "Step 3: Coat the fish pieces with the marinade and let them rest for some time.",
                "Step 4: Coat the pieces lightly with flour or breadcrumbs.",
                "Step 5: Have an adult cook the fish until it is fully cooked.",
                "Step 6: Serve hot with mustard and salad."
            ]
        },

        "Chicken Pakora": {
            "Ingredients": ("Chicken", "Gram Flour", "Salt", "Turmeric", "Chilli Powder", "Water", "Chutney", "Sauce"),

            "Steps": [
                "Step 1: Cut the chicken into small, even-sized pieces.",
                "Step 2: Mix gram flour with salt, turmeric, chilli powder and a little water to make a thick batter.",
                "Step 3: Add the chicken pieces to the batter and coat them properly.",
                "Step 4: Have an adult cook the chicken until it is fully cooked inside.",
                "Step 5: Serve the chicken pakoras hot with chutney or sauce."
            ]
        }
    }
}


# Starting the Recipe Section

print("\n========== RECIPE SECTION ==========")

print("Would you like a Veg or Non-Veg recipe?")

category = input("Enter your choice: ").title()


# Checking the selected category

if category in recipes:

    print(f"\nAvailable {category} recipes:")

    for food in recipes[category]:
        print(food)

    # Asking the user to select a food item

    food_choice = input("\nChoose a food item: ").title()

    if food_choice in recipes[category]:

        print(f"\n========== RECIPE FOR {food_choice.upper()} ==========")

        # Displaying the ingredients

        print("\nIngredients required:")

        for ingredient in recipes[category][food_choice]["Ingredients"]:
            print(ingredient)

        # Displaying the recipe step by step

        print("\nPreparation Steps:")

        for step in recipes[category][food_choice]["Steps"]:
            print(step)

    else:
        print("Recipe not found.")

else:
    print("Invalid category.")

print("\nThank you for trying our Recipe Book!")
