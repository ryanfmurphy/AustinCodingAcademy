def mean(num_list):
    total = 0.0
    for n in num_list:
        total += n
    return total / len(num_list)

def median(num_list):
    num_list = sorted(num_list)
    size = len(num_list)
    midpoint = size/2

    even_number_of_elements = size % 2 == 0
    if(even_number_of_elements):
        middle_val_1 = num_list[midpoint]
        middle_val_2 = num_list[midpoint-1]
        return mean([middle_val_1, middle_val_2])
    else:
        return num_list[midpoint]

def mode(num_list):
    max_occurences = 0
    for n in num_list:
        occurences = num_list.count(n)
        if occurences > max_occurences:
            max_occurences = occurences

    no_mode = max_occurences == 1
    if no_mode:
        return None
    else:
        mode_nums = set()
        for n in num_list:
            if num_list.count(n) == max_occurences:
                mode_nums.add(n)
        return mode_nums

user_nums = []
prompt = 'Enter an integer, or "done" if you are done: '

user_data = raw_input(prompt)
while user_data.lower() != 'done':
    user_val = int(user_data)
    user_nums.append(user_val)
    user_data = raw_input(prompt)

if user_nums:
    print("The mean is: %s" % mean(user_nums))
    print("The median is: %s" % median(user_nums))
    print("The mode is: %s" % mode(user_nums))
else:
    print("No numbers provided")
