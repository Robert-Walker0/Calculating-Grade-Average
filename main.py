
def get_input(prompt):
    print(prompt)
    amount_of_grades = input()
    if amount_of_grades.isdigit():
        return int(amount_of_grades)
    return get_input(prompt)


def calculate_total(number_of_grades):
    total = 0 
    for i in range(1, number_of_grades+1):
        points = get_input(f"Enter points (out of 100) for grade {i}: ")
        total += points
    return total



def calculate_letter(average):
    if average >=.90 and average <= 100:
        return "A"
    elif average < .90 and average>=.80:
        return "B"
    elif average < .80 and average >= .70:
        return "C"
    elif average < .70 and average >=.60:
        return "D"
    elif average < .60 and average >= 0:
        return "F"


def main():
    answer = None
    while(answer != "n"):
        number_of_grades = get_input("Enter the number of grades to process: ")
        if number_of_grades == 0:
            print("Invalid number of grades. You can restart the program from the beginning.")
            break
        total_points = calculate_total(number_of_grades)
        average = total_points / (number_of_grades * 100)
        letter_grade = calculate_letter(average)
        average *= 100
        print(f"Average = {average:.2f}, which is {letter_grade}")
        answer = input("\n\nRun program again? (y/n): ").lower()


if __name__ == '__main__':
    main()
    print("Goodbye!")

