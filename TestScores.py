#Stephen Davis

def main():
    TESTS = 7
    total = 0.0
    average = 0.0
    
    grades = [0.0 for _ in range(TESTS)]
    for i in range(TESTS):
        while True:
            try:
                temp = float(input(f'Enter the grade for test {i + 1}: '))
                if temp < 0:  # Optionally handle non-negative grades
                    print("Grade cannot be negative. Please enter a valid grade.")
                    continue
                grades[i] = temp
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    total = sum(grades)
    average = total / TESTS

    print("Score\t\tNumeric Score")
    for i, grade in enumerate(grades):
        print(f"Score {i + 1}:\t{format(grade, ',.1f')}")
    print("Total:\t\t", format(total, ',.1f'))
    print("Average Score:\t", format(average, ',.1f'))
main()
