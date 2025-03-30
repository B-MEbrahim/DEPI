def median(values):
    if values:
        n = len(values)
        sorted_values = b_sort(values)
        mid_index = int(n / 2)

        if n % 2 != 0:
            return sorted_values[mid_index]
        else:
            
            return round(sorted_values[mid_index] + sorted_values[mid_index + 1] / 2, 2)
    else:
        return None



def b_sort(values):
    length = len(values)
    for i in range(length - 1):
        for j in range(i, length):
            if values[j] < values[i]:
                values[i], values[j] = values[j], values[i]
    return values


# Initialize an empty list to store numbers
temperatures = [23, 25, 20, 23, -5, 21, 18, 19, 24, 21,19, 24, 0, 
                20, 24, 55, 22, 50, 22, 20, 21, 22, 20, 25, 19, 
                22, 26, 23, 21, 23, 17, 20, 18]

print(median(temperatures))

