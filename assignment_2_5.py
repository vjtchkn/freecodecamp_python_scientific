# Ask user for temperature in Celsius and convert it to Fahrenheit
temp_c = float(input("Temperature in Celsius: "))
temp_f = round(temp_c * 1.8 + 32, 2)
print("Temperature in Fahrenheit:", temp_f)
