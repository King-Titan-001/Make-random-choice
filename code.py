import random

# Step 1: Create an empty list
my_list = []

# Step 2: Ask the user for the number of items they want on the list
num_items = int(input("How many items do you want on the list? "))

# Step 3: Allow the user to input the items
for i in range(num_items):
    item = input("Enter an item: ")
    my_list.append(item)

# Step 4: Use a while loop to keep choosing random items from the list until the user decides to stop
while True:
    random_item = random.choice(my_list)
    print("Randomly chosen item: ", random_item)

    # Step 5: Ask the user if they want to continue choosing random items from the list
    run_again = input("Do you want to choose another item from the list? (y/n) ").lower()

    # Step 6: Check if the user wants to continue choosing random items from the list or not
    if run_again != 'y':
        break
