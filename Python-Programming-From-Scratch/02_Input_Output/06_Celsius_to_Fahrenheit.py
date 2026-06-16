# ============================================================
# Program 06 : Celsius to Fahrenheit Converter
# ============================================================
#
# Problem Statement:
# Write a Python program that accepts the temperature
# in Celsius from the user.
#
# Convert the temperature to Fahrenheit using the formula:
#
# Fahrenheit = (Celsius × 9 / 5) + 32
#
# Display the converted temperature.
#
# ============================================================

celsius = float(input("Enter Tempreature In Celsius : "))

fahrenheit = (celsius * 9 / 5) + 32

print("Tempreature In Fahrenheit : ",fahrenheit)