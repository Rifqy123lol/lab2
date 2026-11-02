def main():
    numbers = get_user_input()
    avg = calc_average(numbers)
    minmax = find_minmax(numbers)
    display_main_menu(numbers, avg, minmax)
def get_user_input():
    number = input("Enter numbers: ")
    number_list = number.split(",")
    return number_list

def calc_average(numbers):
    sum = 0.0
    for i in numbers:
        sum += float(i)
    avg = sum/len(numbers)
    return avg

def find_minmax(numbers):
    minmax = [min(numbers), max(numbers)]
    return minmax

def display_main_menu(numbers, avg, minmax):
    print("List of numbers:", numbers)  
    print("Average: ", avg)
    print("Min max: ",minmax)

if __name__ == "__main__":
    main()