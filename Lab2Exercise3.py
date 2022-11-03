def main():
    display_main_menu()
    get_user_input()

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32)") #NO SPACE BETWEEN COMMA AND NUMBER

def get_user_input():
    x = input('Enter some numbers:')
    y = x.split(",")

    z = [float(a) for a in y]

    #z = list(map(float, y))

    #a = len(y)
    #z = [float(a) for a in y]

    #z = []
    #for element in y:
    #    z.append(float(element))


    print(z)

main()