'''
############
Lab 4.04
############

Part 1
-----------
The goal of this lab is to practice using and accessing items from lists of lists.

You have a few errands to run and have created a few shopping lists to help you remember what to buy. 
You stored your notes in a nested list, shopping_cart. This program will allow the user to ask for a 
specific item by its index or update what items are in the cart. The user can request to view list to 
see the items in a specific shopping list.

Shopping Lists
    shopping_lists = [
        ['toothpaste', 'q-tips', 'milk'],
        ['milk', 'candy', 'apples'],
        ['planner', 'pencils', 'q-tips']
    ]
User Inputs
1 - Update

The program asks which shopping list the user wants to update, which position it should update, and the new value to update.

2 - View Item

The program asks which shopping list the item is on and which position it occupies, then prints the item's name.

3 - View List

The program asks which shopping list the user wants and prints all of the items associated with that shopping list.

Functions
update_list

Takes in an integer representing the index of the shopping list, an integer representing the index of the item to update, and a string representing the new value for that item. Does not alter the length of the list.

print_item

Takes an int representing the index of the shopping list followed by an int representing the index of the item to print.

print_list

Takes an int representing the index of the shopping list to print.

Feel free to add more functions as you see fit.

Example
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 1
    Which shopping list would you like to update? 1
    Which item would you like to change? 2
    New value for item #2? cheese
    toothpaste, cheese, milk
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 2
    Which shopping list do you want to choose? 2
    Which item on list #2 do you want to see? 3
    apples
    >>> Choose 1 = update item, 2 = view item, or 3 = view list: 3
    Which shopping list would you like to see? 3
    planner, pencils, q-tips

Part 2
------------
In this part of the lab you will go through your shopping list program and perform a few different calculations.

Create a function, all_in_one, that will put all the shopping lists into a single combined list using a for loop.

Create a function, count_q_tips, which will go through all items of the list and keep a count of how many times 
'q-tips' occurs.

In order to make the shopping lists more calcium rich, write a function, drink_more_milk, that adds 'milk' to each 
of the lists (unless it's already there).

You can't have milk without cookies. Write a function if_you_give_a_moose_a_cookie, that will go through every 
element of shopping_cart and update 'milk' to be 'milk and cookies'.

Extension
-------------
Write a function to reverse the order of the lists, and also reverse the order of the items in each list, in the shopping_cart nested list.

The new reversed list should look like the following when printed (newlines and spacing added for clarity):

    shopping_cart = [
        ['q-tips', 'pencils', 'planner'],
        ['apples', 'candy', 'milk'],
        ['milk', 'q-tips', 'tooth paste']
    ]
Tip
Last item can be gotten by my_list[-1]

Second to last element: my_list[-2]

Third to last element: my_list[-3]
'''

#functions

def update(list_number, item_number, new_item):
    shopping_lists[list_number][item_number] = new_item

def view_item(list_number, item_number):
    print(shopping_lists[list_number][item_number])

def view_list(list_number):
    count = 0
    list_string = ''
    for item in shopping_lists[list_number]:
        if count < 2:
            list_string += item+ ", "
        
        else:
            list_string += item
            
            count += 1  
    print(list_string)

def all_in_one():
    big_list = []

    for list in shopping_lists:
        for item in list:
            big_list.append(item)
    print(big_list)

def count_q_tips(list_choice):
    num_q_tips = 0
    for item in shopping_lists[list_choice]:
        if item == 'q-tips':
            num_q_tips += 1
    print(f"You have {num_q_tips} q-tips in that list.")

def drink_more_milk():

    for i in range(len(shopping_lists)):
        if 'milk' not in shopping_lists[i]:
            shopping_lists[i].append('milk')
        
def if_you_give_a_moose_a_cookie():
    for i in range(len(shopping_lists)):
        if 'milk' in shopping_lists[i]:
            shopping_lists[i].append('milk & cookies')




shopping_lists = [
        ['toothpaste', 'q-tips', 'milk'],
        ['milk', 'candy', 'apples'],
        ['planner', 'pencils', 'q-tips']
]

#user inputs

while True:

    user_choice = input("What would you like to do? Choice one updates the list, choice two views an item, choice three views a list, choice four prints the entire list," 
    "choice five tells you how many times you have q-tips in your list, choice 6 adds milk to your list, choice 7 adds cookies to every milk in your list, if you would like to quit, type 'quit' ")

    if user_choice == '1':
        list_choice = int(input("Which list number contains the item you want to change? ")) - 1
        item_choice = int(input("Which item number would you like to update? ")) - 1
        new_item = input("What item do you want to add? ")

        update(list_choice, item_choice, new_item)

    elif user_choice == '2':
        list_choice = int(input("Which list number contains the item you want to view? ")) - 1
        item_choice = int(input("Which item number would you like to view? ")) - 1

        view_item(list_choice, item_choice)

    elif user_choice == '3':
        list_choice = int(input("Which list number contains the item you want to view? ")) - 1

        view_list(list_choice)

    elif user_choice == '4':
        all_in_one()

    elif user_choice == 'quit':
        break 

    elif user_choice == '5':
        list_choice = int(input("Which list would you like to count q-tips in? ")) - 1

        count_q_tips(list_choice)

    elif user_choice == '6':
        drink_more_milk()

    elif user_choice == '7':
        if_you_give_a_moose_a_cookie()