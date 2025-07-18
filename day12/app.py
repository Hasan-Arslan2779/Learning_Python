# This is a simple Python script that demonstrates the use of functions and variable unpacking.


# def math_operation(a, b):
#     addition = a + b
#     subtraction = a - b
#     multiplication = a * b
#     division = a / b if b != 0 else 'undefined'
#     return addition, subtraction, multiplication, division


# add, subtraction, multiplication, division = math_operation(3, 5)
# print(f"The result of the operation is: {add}")

#! Temperature converter application
# Adım 1:Dönüştürme fonksiyonunu tanımlayın
def celcius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def celcius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15


def kelvin_to_celcius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32


# adım 2: Menüyü Gösterin
def show_menu():
    print("Welcome to the Temperature Converter!")
    print("1. Convert Celsius to Fahrenheit  & kelvin")
    print("2. Convert Fahrenheit to Celsius & kelvin")
    print("3. Convert Kelvin to Celsius & Fahrenheit")
    print("4. Exit")


# adım 3 : Ana döngüyü oluşturun
while True:
    show_menu()
    choice = input("Please select an option (1-4): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"fahrenheit: {celcius_to_fahrenheit(celsius):.2f}°F")
        print(f"kelvin: {celcius_to_kelvin(celsius):.2f}K")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"Celsius: {fahrenheit_to_celcius(fahrenheit):.2f}°C")
        print(f"Kelvin: {fahrenheit_to_kelvin(fahrenheit):.2f}K")
    elif choice == '3':
        kelvin = float(input("Enter temperature in Kelvin: "))
        print(f"Celsius: {kelvin_to_celcius(kelvin):.2f}°C")
        print(f"Fahrenheit: {kelvin_to_fahrenheit(kelvin):.2f}°F")
    elif choice == '4':
        print("Exiting the Temperature Converter. Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")
