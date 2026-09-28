#temperature_input = input("Enter a temperature [32C/77F]: ")

temperature_input = '25C'
temperature_input = '50K'


temperature_type = temperature_input[-1].upper()
temperature_number = float(temperature_input[:-1])


if temperature_type == 'C' or temperature_type == 'F':

    temperature = 0
    
    if temperature_type == 'C':
        # Celsius to Fahrenheit
        temperature = temperature_number * ( 9 / 5) + 32
        temperature_from = 'Celsius'
        temperature_to = 'Fahrenheit'
    else:
        # Fahrenheit to Celsius
        temperature = (temperature_number - 32) * 5 / 9
        temperature_from = 'Fahrenheit'
        temperature_to = 'Celsius'

    print(f"{temperature_number} degrees {temperature_from} is {temperature} degrees {temperature_to}.")

else:
    print('Invalid unit of measurement.')