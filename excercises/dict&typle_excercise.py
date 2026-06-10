"""
## Exercise: Python Dict and Tuples

1. We have following information on countries and their population (population is in crores),

    |Country|Population|
    |-------|----------|
    |China|143|
    |India|136|
    |USA|32|
    |Pakistan|21|
    1. Using above create a dictionary of countries and its population
    2. Write a program that asks user for three type of inputs,
        1. print: if user enter print then it should print all countries with their population in this format,
            ```
            china==>143
            india==>136
            usa==>32
            pakistan==>21
            ```
        1. add: if user input add then it should further ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
        2. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
        3. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.


2. You are given following list of stocks and their prices in last 3 days,

    |Stock|Prices|
    |-------|----------|
    |info|[600,630,620]|
    |ril|[1430,1490,1567]|
    |mtl|[234,180,160]|

    1. Write a program that asks user for operation. Value of operations could be,
        1. print: When user enters print it should print following,
            ```
            info ==> [600, 630, 620] ==> avg:  616.67
            ril ==> [1430, 1490, 1567] ==> avg:  1495.67
            mtl ==> [234, 180, 160] ==> avg:  191.33
            ```
        2. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.


3. Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them

"""
import math
import statistics

countires = {
    "china":"143",
    "india":"136",
    "usa":"32",
    "pakistan":"21",

}
user_input = input("Please enter three types of inputs: print , add , remove , query :")
if user_input == "print":
    for key,value in countires.items():
        print(f'{key} ==> {value}')
elif user_input == "add":
    country_name = input("Please enter country name : ")
    if country_name in countires.keys():
        print(f'{country_name} already exists in dictionary')
    else:
        population = int(input("Please enter population : "))
        countires[country_name] = population
if user_input == "remove":
    country_to_be_remove = input("Please enter country to remove : ")
    if country_to_be_remove in countires.keys():
        del countires[country_to_be_remove]
    for key,value in countires.items():
        print(f'{key} ==> {value}')
if user_input == "query":
    country_to_query = input("Please enter country to query : ")
    if country_to_query in countires.keys():
        print(f'population of {country_to_query} ==> {countires[country_to_query]}')

stocks_data={
    "info":[600,630,620],
    "ril":[1430,1490,567],
    "mtl":[234,180,160]
}
def print_val():
    for key,value in stocks_data.items():
        avg = statistics.mean(value)
        print(f'{key} ==> {value} ==>', round(avg,2))
def add_list(ticker,price):
    if ticker in  stocks_data.keys():
        stocks_data[ticker].append(price)
    else:
        stocks_data[ticker] = [int(price)]

user_input_stock_ques = input("Please enter the options 1.print 2.add")
if user_input_stock_ques == "print":
    print_val()
elif user_input_stock_ques == "add":
    ticker = input("Please enter ticker : ")
    price = input("Please enter price : ")
    add_list(ticker,price)
    print_val()


def circle_calc(radius):
    area = radius * radius
    print(f'The area of circle is {area}')
    circumference = 2 * math.pi * radius
    print(f'The circumference of circle is {circumference}')
    diameter = 2 * radius + 1
    print(f'The diameter of circle is {diameter}')

rad = int(input("Please enter radius : "))
circle_calc(rad)