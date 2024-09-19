def get_student_data():
    # Ask how many students' data needs to be entered
    num_students = int(input("Enter the number of students: "))

    # Open the file in write mode (or append mode if needed)
    with open("Marks.data", "w") as file:
        # Write header
        file.write("Roll Number, Name, Marks\n")

        # Loop to get data for each student
        for i in range(num_students):
            print(f"\nEntering details for Student {i + 1}:")
            roll_number = input("Enter Roll Number: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")

            # Write the student's details into the file
            file.write(f"{roll_number}, {name}, {marks}\n")

    print("\nData has been successfully written to Marks.data!")


# Main program
get_student_data()
