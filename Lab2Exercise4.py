import statistics

def main():
    display_main_menu()
    INPUT = get_user_input()
    calc_average(INPUT)
    find_min_max(INPUT)
    sort_temperature(INPUT)
    calc_median_temperature(INPUT)

#Test Output: 1,2,3,4,5,6,7,8,9,10
#Test Output: 2,3,1,4,7,5,6,8,9,10

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
    x = input('Enter some numbers:')
    y = x.split(",")
    z = [float(a) for a in y]
    print(z)
    return z
def calc_average(num):
    AVERAGE = sum(num)/len(num)
    print(AVERAGE)
    return AVERAGE
def find_min_max(num):
    MINIMUM = min(num)
    MAXIMUM = max(num)
    print(MINIMUM,MAXIMUM)
    return(MINIMUM,MAXIMUM)
def sort_temperature(num):
    num.sort()
    print(num)
    return num
def calc_median_temperature(num):
    MEDIAN = statistics.median(num)
    print(MEDIAN)
    return MEDIAN
main()