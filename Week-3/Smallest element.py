my_list = [3, 1, 4, 1, 5, 9, 2]
smallest = my_list[0]

for num in my_list:
    if num < smallest:
        smallest = num

print("Smallest element is:", smallest)
