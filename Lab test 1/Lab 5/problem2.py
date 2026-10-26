students = [
    [201, "Amina", [78, 85, 90]],
    [202, "Rahim", [65, 70, 68]],
    [203, "Nadia", [92, 88, 95]],
    [204, "Hasan", [55, 60, 65]],
    [205, "Tania", [80, 80, 80]]
]


def calculate_average(marks):
    """Return the average of a student's marks."""
    return sum(marks) / len(marks)


def classify_performance(average):
    """Return a performance category based on the average."""
    if average >= 80:
        return "Excellent"
    elif average >= 70:
        return "Good"
    elif average >= 60:
        return "Satisfactory"
    else:
        return "Needs Improvement"


def display_report(students):
    """Display each student's ID, name, average, and category."""
    print("\nStudent Performance Report")
    print("-" * 60)
    print(f"{'ID':<6}{'Name':<12}{'Average':<12}{'Performance':<20}")
    print("-" * 60)
    for s in students:
        student_id = s[0]
        name = s[1]
        marks = s[2]

        avg = calculate_average(marks)
        category = classify_performance(avg)

        print(f"{student_id:<6}{name:<12}{avg:<12.2f}{category:<20}")


# Main program
display_report(students)
