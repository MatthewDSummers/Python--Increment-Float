import math

# Take the float and increment it by its decimal value (rounded to two places) until the stopping point without exceeding its stopping point
    # return the results in a list
def increment_by_decimal_value(start,stop):
    x = round(start, 2)
    if x < 0:
        x = abs(x)

    num_parts = math.modf(x)
    dec_val = num_parts[0]

    if dec_val <= 0.0:
        print("Please provide a decimal value greater than or equal to 0.005")
        return None
    else:
        result = []

        starter = round(start, 2)
        result.append(starter)

        dec_val = round(dec_val, 2)
        print(f"\nThe rounded starting point is {starter}\nThe decimal value is {dec_val}\nThe stopping point is {stop}\n")

        while starter < stop :
            starter += dec_val
            if starter > stop:
                break
            starter = round(starter, 2)
            result.append(starter)
        return result

print(increment_by_decimal_value(2.5, 8))
# OUTPUT:
    # The rounded starting point is 2.5
    # The decimal value is 0.5
    # The stopping point is 8

    # [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0]

print(increment_by_decimal_value(-.005, .1))
# OUTPUT:
    # The rounded starting point is -0.01
    # The decimal value is 0.01
    # The stopping point is 0.1

    # [-0.01, 0.0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1]

print(increment_by_decimal_value(-.0049, .1))
# OUTPUT
    # Please provide a decimal value greater than or equal to 0.005

print(increment_by_decimal_value(2.7, 10))
# OUTPUT
    # The rounded starting point is 2.7
    # The decimal value is 0.7
    # The stopping point is 10

    # [2.7, 3.4, 4.1, 4.8, 5.5, 6.2, 6.9, 7.6, 8.3, 9.0, 9.7]