def evaporator(content, evap_per_day, threshold):
    n = 0
    current = 100
    percent = 1 - evap_per_day / 100.0
    while current > threshold:
        current *= percent
        n += 1
    return n

            


evaporator(10, 10, 10)
