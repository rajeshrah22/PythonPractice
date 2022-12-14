#liters per 100k <--> miles per gallon conversion

def liters_100km_to_miles_gallon(liters):
    return 1/(liters/.6214*.2642/100)

def miles_gallon_to_liters_100km(miles):
    return 1/(miles*.0161/3.79)

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
