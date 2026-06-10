"""
## Exercise: Python If Condition
1. Using following list of cities per country,
    ```
    india = ["mumbai", "banglore", "chennai", "delhi"]
    pakistan = ["lahore","karachi","islamabad"]
    bangladesh = ["dhaka", "khulna", "rangpur"]
    ```
    1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
    2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
2. Write a Python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
    1. Ask user to enter his fasting sugar level
    2. If it is below 80 to 100 range then print that sugar is low
    3. If it is above 100 then print that it is high otherwise print that it is normal
"""
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore", "karachi", "islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city=input("Enter a city name to know the country it belongs to :")
if city in india:
    print(f"{city} is in India")
elif city in pakistan:
    print(f"{city} is in Pakistan")
elif city in bangladesh:
    print(f"{city} is in Bangladesh")
else:
    print(f"{city} is not in India,Pakistan,Bangladesh")

city1=input("Enter a city name to know the country it belongs to :")
city2=input("Enter a city name to know the country it belongs to :")

if city1 and city2 in india:
    print(f"{city1} and {city2} are in India")
elif city1 and city2 in pakistan:
    print(f"{city1} and {city2} are in Pakistan")
elif city1 and city2 in bangladesh:
    print(f"{city1} and {city2} are in Bangladesh")
else:
    print(f"{city1} and {city2} is not in India,Pakistan,Bangladesh")

sugar_lvl=int(input("Enter your blood sugar level"))
if sugar_lvl in range(80,100):
    print("You blood sugar level is low")
elif sugar_lvl>200:
    print("You blood sugar level is high")
else:
    print("You blood sugar level is normal")
