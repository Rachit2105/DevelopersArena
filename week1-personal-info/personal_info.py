# PROJECT NAME - Personal Information Collector
# DESCRIPTION - A simple program to collect and display personal information from the user.

# welcome messager
print("*"*40)
print("!!WELCOME TO PERSONAL INFORMATION MANAGER!!")
print("*"*40)


# these is to take declare from the user and print a greeting message
name = str("Rachit Gupta")
age = int(20)
   

# this is to declare there birth city and hobby details and print a message
city =  str("Delhi")
hobby = str("Coding")


# this is to input the favourite color and favourite food from the user and print it
fav_food = input("What's your favorite food? ")
while fav_food == "":
    print("Please enter a valid food!")
    fav_food = input("What's your favorite food? ")

fav_color = input("What's your favorite color? ")
while fav_color == "":
    print("Please enter a valid color!")
    fav_color = input("What's your favorite color? ")


# Calculate age in months
age_in_months = age * 12
print("-" *40)

print(f"hello {name} you are {age} years old \nyou were born in {city} and you love {hobby} \nyour favourite color is {fav_color} and you love to eat {fav_food}")

print(f"Your Age in months is {age_in_months}")


# Goodbye message
print("*" * 40)
print("THANKS FOR USING OUR INFORMATION MANAGER")
print("*" * 40)