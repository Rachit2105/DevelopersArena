# ==========================================
# Student Grade Calculator
# Week 2 Project - Control Flow & Lists
# ==========================================


# ---------- Function to decide grade ----------
# This function takes average marks
# and returns grade + feedback message
def decide_grade(avg_marks):
    if avg_marks >= 90:
        return "A", "Excellent performance!"
    elif avg_marks >= 80:
        return "B", "Very good work!"
    elif avg_marks >= 70:
        return "C", "Good job, can improve more."
    elif avg_marks >= 60:
        return "D", "You need more practice."
    else:
        return "F", "You have failed. Work harder."


# ---------- Function to safely take marks input ----------
# This function keeps asking until user enters
# a valid number between 0 and 100
def input_marks(message):
    while True:
        try:
            marks = float(input(message))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number!")


# ---------- Main Program Starts Here ----------
def main():

    # Display title
    print("=" * 50)
    print("        STUDENT GRADE CALCULATOR")
    print("=" * 50)

    # --------- Taking number of students ----------
    # We check that the number is positive
    while True:
        try:
            total_students = int(input("\nEnter total number of students: "))
            if total_students > 0:
                break
            else:
                print("Number must be greater than 0.")
        except ValueError:
            print("Please enter a whole number.")

    # --------- Creating empty lists to store data ----------
    names_list = []
    marks_list = []
    results_list = []

    # --------- Taking input for each student ----------
    for i in range(total_students):

        print(f"\n--- Enter details for Student {i + 1} ---")

        # Taking student name (cannot be empty)
        student_name = input("Enter student name: ")
        while student_name.strip() == "":
            print("Name cannot be empty.")
            student_name = input("Enter student name: ")

        names_list.append(student_name)

        # Taking marks for 3 subjects
        print("Enter marks out of 100:")
        m1 = input_marks("Math: ")
        m2 = input_marks("Science: ")
        m3 = input_marks("English: ")

        marks_list.append([m1, m2, m3])

        # --------- Calculating average ----------
        avg = (m1 + m2 + m3) / 3

        # Getting grade and feedback
        grade, feedback = decide_grade(avg)

        # Storing result in dictionary
        results_list.append({
            "average": avg,
            "grade": grade,
            "feedback": feedback
        })

    # --------- Printing Results Table ----------
    print("\n" + "=" * 50)
    print("              RESULTS")
    print("=" * 50)

    print(f"{'Name':<20} {'Average':>8} {'Grade':>8}")
    print("-" * 40)

    for i in range(total_students):
        print(f"{names_list[i]:<20} {results_list[i]['average']:>8.1f} {results_list[i]['grade']:>8}")

    # --------- Calculating Class Statistics ----------
    averages_only = [data["average"] for data in results_list]

    class_average = sum(averages_only) / len(averages_only)
    highest = max(averages_only)
    lowest = min(averages_only)

    top_student = names_list[averages_only.index(highest)]
    low_student = names_list[averages_only.index(lowest)]

    print("\n" + "=" * 50)
    print("           CLASS STATISTICS")
    print("=" * 50)

    print(f"Total Students  : {total_students}")
    print(f"Class Average   : {class_average:.1f}")
    print(f"Highest Average : {highest:.1f} ({top_student})")
    print(f"Lowest Average  : {lowest:.1f} ({low_student})")

    print("\nProgram Finished Successfully!")


# ---------- Running the Program ----------
if __name__ == "__main__":
    main()
