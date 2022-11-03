def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    x = input('Enter some numbers:')
    y = x.split(", ")
    print(y)
def calc_average():
    print("calc_average")

display_main_menu()
calc_average()