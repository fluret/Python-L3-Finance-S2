temperatures = [18, -35, 22, 47, 31, -5, 12, 60, 0]

def is_valid_temperature(t):
    return -20 <= t <= 45

valid_temperatures = list(filter(is_valid_temperature, temperatures))

print("Relevés bruts :", temperatures)
print("Relevés valides :", valid_temperatures)