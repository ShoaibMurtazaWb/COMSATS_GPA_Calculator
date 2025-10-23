grades = {
    'A': 4.00,
    'A-': 3.66,
    'B+': 3.33,
    'B': 3.00,
    'B-': 2.60,
    'C+': 2.33,
    'C': 2.00,
    'C-': 1.66,
    'D+': 1.30,
    'D': 1.00,
    'F': 0.00
}

# SEMESTER GPA 
def calculate_gpa():
    print("\n--- Semester GPA ---")

    # number of courses
    while True:
        num_courses = input("Enter number of courses: ")
        if num_courses.isdigit() and int(num_courses) > 0:
            num_courses = int(num_courses)
            break
        else:
            print("Invalid input! Please enter a positive whole number.")

    total_credits = 0.0
    total_points = 0.0

    # loop for each course
    for i in range(1, num_courses + 1):
        print("\nCourse", i)

        # get credit hours (must be numeric)
        valid_credit = False
        while not valid_credit:
            credit_text = input("  Enter credit hours: ")

            # check manually if it's numeric (allows 2 or 2.5)
            dot_count = 0
            is_valid_number = True
            for ch in credit_text:
                if ch == '.':
                    dot_count = dot_count + 1
                elif not ch.isdigit():
                    is_valid_number = False
            if dot_count > 1:
                is_valid_number = False

            if is_valid_number:
                credit_value = float(credit_text)
                if credit_value > 0:
                    valid_credit = True
                    credits = credit_value
                else:
                    print("  Credit hours must be positive. Try again.")
            else:
                print("  Invalid input! Enter a number like 3 or 1.5.")

        # get letter grade
        while True:
            grade = input("  Enter grade (A, A-, B+, B, B-, C+, C, C-, D+, D, F): ").upper()
            if grade in grades:
                gp = grades[grade]
                break
            else:
                print("  Invalid grade! Try again using correct format.")

        total_credits = total_credits + credits
        total_points = total_points + (credits * gp)

    gpa = total_points / total_credits
    print("\nYour Semester GPA is:", round(gpa, 2))


# CGPA 
def calculate_cgpa():
    print("\n--- CGPA Calculator ---")

    # number of semesters
    while True:
        semesters = input("Enter number of semesters: ")
        if semesters.isdigit() and int(semesters) > 0:
            semesters = int(semesters)
            break
        else:
            print("Invalid input! Please enter a positive whole number.")

    total_credits = 0.0
    total_points = 0.0

    # loop through semesters
    for s in range(1, semesters + 1):
        print("\nSemester", s)

        # credit hours check
        while True:
            credit_text = input("  Enter total credit hours: ")

            dot_count = 0
            is_valid_number = True
            for ch in credit_text:
                if ch == '.':
                    dot_count = dot_count + 1
                elif not ch.isdigit():
                    is_valid_number = False
            if dot_count > 1:
                is_valid_number = False

            if is_valid_number:
                sem_credits = float(credit_text)
                if sem_credits > 0:
                    break
                else:
                    print("  Credit hours must be positive. Try again.")
            else:
                print("  Invalid input! Enter a number like 15 or 18.5.")

        # GPA check
        while True:
            gpa_text = input("  Enter GPA (0.0 - 4.0): ")

            dot_count = 0
            is_valid_number = True
            for ch in gpa_text:
                if ch == '.':
                    dot_count = dot_count + 1
                elif not ch.isdigit():
                    is_valid_number = False
            if dot_count > 1:
                is_valid_number = False

            if is_valid_number:
                sem_gpa = float(gpa_text)
                if sem_gpa >= 0 and sem_gpa <= 4:
                    break
                else:
                    print("  GPA must be between 0.0 and 4.0. Try again.")
            else:
                print("  Invalid input! Enter a number like 3.5.")

        total_credits = total_credits + sem_credits
        total_points = total_points + (sem_credits * sem_gpa)

    cgpa = total_points / total_credits
    print("\nYour CGPA is:", round(cgpa, 2))


# MENU 
while True:
    print("\n===== GPA/CGPA Calculator =====")
    print("1. Calculate Semester GPA")
    print("2. Calculate CGPA")
    print("3. Exit")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        calculate_gpa()
    elif choice == '2':
        calculate_cgpa()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, or 3.")
