# Guido's Gorgeous Lasagna
EXPECTED_BAKE_TIME = 40
preparation_time = 2

def bake_time_remaining(actual_minutes):
    return EXPECTED_BAKE_TIME - actual_minutes

print(bake_time_remaining(30))

def preparation_time_in_minutes(number_of_layers):
    return preparation_time * number_of_layers

print(preparation_time_in_minutes(2))

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    return number_of_layers * preparation_time + elapsed_bake_time

print(elapsed_time_in_minutes(3, 20)) 