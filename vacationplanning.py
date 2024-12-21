def vacation_trip(return_flight, hotel_per_day, weekly_car_rental, duration):
        
    return return_flight + (hotel_per_day * duration) + weekly_car_rental

# vacation of 7 days
print("Paris")
print(vacation_trip(200, 20, 200, 7))
print(vacation_trip(200, 20, 200, 4))
print(vacation_trip(200, 20, 200, 10))
print(vacation_trip(200, 20, 200, 14))

print("________")

print("London")
print(vacation_trip(250, 30, 120, 7))
print(vacation_trip(50, 30, 120, 4))
print(vacation_trip(250, 30, 120, 10))
print(vacation_trip(250, 30, 120, 14))

print("________")

print("Dubai")
print(vacation_trip(370, 15, 80, 7))
print(vacation_trip(370, 15, 80, 4))
print(vacation_trip(370, 15, 80, 10))
print(vacation_trip(370, 15, 80, 14))

print("________")

print("Mumbai")
print(vacation_trip(450, 10, 70, 7))
print(vacation_trip(450, 10, 70, 4))
print(vacation_trip(450, 10, 70, 10))
print(vacation_trip(450, 10, 70, 14))
