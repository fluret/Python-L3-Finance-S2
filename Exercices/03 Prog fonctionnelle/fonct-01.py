celsius = [0, 10, 20, 30]

def celsius_to_fahrenheit(temp):
    return temp * 9 / 5 + 32
    
fahrenheit = list(map(celsius_to_fahrenheit, celsius))

print(celsius)
print(fahrenheit)