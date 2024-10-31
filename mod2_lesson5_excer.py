"""#user name valid?
while True:
    username = input("Enter your desired username: ")

    if 5<= len(username) <= 15:
        print("Username is valid!")
    else:
        print("username must be between 5 and 15 characters!")
    
    continue_input = input("Do you want to try another username? (Yes/No) ").lower()
    if continue_input != "yes":
        break"""

"""#Precise price tagger
while True:
    price = float(input("What is the price of the item? "))

    converted_price = round(price) 
    print(f"The price of the item is ${converted_price}")

    check_another = input("Would you like to check another price: (Yes/No)").lower()
    if check_another != "yes":
        break """

"""#global temp translator
celsius_temps = [10, 20 , 25, 30, 35]

for celsius in celsius_temps:
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}C is equal to {fahrenheit}F")"""

"""#the goldiockas room selecta
room_temps = [22, 24, 19, 21]
room_names = ["Living", "kitchen", "bed", "bath"]
warmest_temp = max(room_temps)
coolest_temp = min(room_temps)

warmest_room_index = room_temps.index(warmest_temp)
coolest_room_index = room_temps.index(coolest_temp)

warmest_room = room_names[warmest_room_index]
coolest_room = room_names[coolest_room_index]
print(f"the warmest room is {warmest_room} and the coolest room is {coolest_room}")"""


"""#e commerce cart summary
#products
product_1 = "wireless mouse"
product_2 = "Gmaing keyboard"
product_3 = "Usb c charger"
#prices
price_1 = "$25"
price_2 = "$50"
price_3 = "$10"
#availability
in_stock_1 = True
in_stock_2 = False
in_stock_3 = True

cart_summary = "Your cart items:\n"
cart_summary += "- " + product_1 + ": " + price_1 + ("(In Stock)" if in_stock_1 else "(Out of stock)") + "\n"
cart_summary += "- " + product_2 + ": " + price_2 + ("(In Stock)" if in_stock_2 else "(Out of stock)") + "\n"
cart_summary += "- " + product_3 + ": " + price_3 + ("(In Stock)" if in_stock_3 else "(Out of stock)") + "\n"

print(cart_summary)"""

"""#the interactive story chooser
print("You wake up in a mysterios forest. Two paths await you which one will you choose ")
choices = ['left', 'right']
outcomes = ['you encounter a friendly elf who gives you a map', 'you stumble upon a sleeping dragon']
print(f'Do you go left or right? (Type "Left" or "Right")')
decision = input().lower()

if decision not  in choices:
    print("Confused, You decide to wait for a clearer path to take")
elif decision == 'left':
    outcome_index = choices.index('left')
    print(outcomes[outcome_index])
else:
    outcome_index = choices.index('right')
    print(outcomes[outcome_index])"""

"""   #the custimized list planner
shopping_list = ["apples", "Bananas", "carrots", "muffins", "milk"]

seperator = input("Please enter your preferred item seperator (e.g., ',', '/',  '-'):")
ending = input("Please enter your preferred ending phrase (e.g., 'End of list', 'Thats all!'): ")

print("your shopping list: ", end="\n\n")
for item in shopping_list:
    if item == shopping_list [-1]:
        print(item)
    else:
        print(item, end=seperator + " ")
print("\n\n" + ending)"""

"""#The Dynamic type quiz game
questions = ["whats 10 plus 4?",
  "Enter a decimal betwen 1 and 2,",
   "What is the string representation of 20",
    "Is python a programming language?(True/False)" ]

correct_answers = [14, 1.5, "20", True]
answer_types = [int, float, str, bool]
 
score = 0


for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    try:
        if answer_types[i] == bool:
            converted_answer = user_answer.lower() in ['true', 't', '1','yes', 'y' ]
        else:
            converted_answer = answer_types[i](user_answer)

        if converted_answer == correct_answers[i]:
            print("Correct")
            score += 1
        else:
            print("Wrong Answer")
    except ValueError:
        print("Invalid Input type")

print(f"Your final score is {score}/{len(questions)}")"""

"""#the type inspection
mixed_list = [10, 3.14, 'Python', False, 42, 'Code', 2.718, True, 1]

intergers= []
floats = []
strings = []
booleans = []

for element in mixed_list:
    if isinstance(element, int) and not isinstance(element, bool):
        intergers.append(element)
    elif isinstance(element, float):
        floats.append(element)
    elif isinstance(element, str):
        strings.append(element)
    elif isinstance(element, bool):
        booleans.append(element)
    else:
        print(f"unknown type: {type(element)}")

print(f"intergers: {intergers}")
print(f"floats: {floats}")
print(f"strings: {strings}")
print(f"booleans: {booleans}")"""

"""#the math function marathon
import math

numbers= [2.5, 3.6, 4.7, 5.8, 6.9]

total_sum = sum(numbers)
print(f"the sum of the numbers is: {total_sum}")

average = total_sum / len(numbers)
print(f"The average is: {average}")
for number in numbers:
    sqrt_number = math.sqrt(number)
    rounded_number = round(sqrt_number)
    if rounded_number < sqrt_number:
        rounded_number = math.ceil(sqrt_number)
    else:
        rounded_number = math.floor(sqrt_number)

    if rounded_number > average:
        print(f"{rounded_number} is Above the average.")
    else:
        print(f"{rounded_number} is below the average.")"""

import datetime
def morning_routine():
    print("Good morning")

    weather_conditions = ['sunny', 'rainy', 'cloudy', 'rainy', 'sunny', 'cloudy', 'windy']
    
    today_weather = weather_conditions[datetime.datetime.today(). weekday()]
    if today_weather == 'rainy':
        print("dont dforget your umbrella")

        calendar_events = ["gym", "meeting", 'dentist', "lunch", "grocery"]
        today_event = calendar_events[datetime.datetime.today().weekday()]
        print(f"Todays event is {today_event}")

        unread_emails = 5
        if unread_emails > 0:
            print (f"you have {unread_emails} unread emails")
