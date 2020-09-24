import math

def trunc(nb, decimals):
    multiplier = 10.0 ** decimals
    return math.trunc(nb * multiplier) / multiplier

def get_input_as_float(label):
    input_value = None

    while type(input_value) != float:
        input_value = input(label)
        try:
            input_value = float(input_value)
            break
        except ValueError:
            continue

    return input_value

def ex_311():

    total_galon = 0
    total_miles = 0

    while 1:
        input_galon = get_input_as_float("Enter the gallons used (-1 to end): ")
        input_miles = -1
        if input_galon < 0:
            break
        while input_miles < 0:
            input_miles = get_input_as_float("Enter the miles driven: ")
        
        total_galon += input_galon
        total_miles += input_miles

        print(f'The miles/gallon for this tank was {trunc(0 if input_galon == 0 else input_miles / input_galon, 6):.6f}')

    print(f'The overall average miles/gallon was {trunc(0 if total_galon == 0 else total_miles / total_galon, 6):.6f}')

ex_311()