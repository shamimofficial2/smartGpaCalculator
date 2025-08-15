def exam_marks_grade_and_point_calculator(subject_mark):

    try:
        subject_mark = int(subject_mark)
        if subject_mark < 0 or subject_mark > 100:
            return "Invalid", 0.0   
    except ValueError:
        return "Invalid", 0.0       
    
    if subject_mark >= 80:
        return "A+", 5.0
    
    elif subject_mark >= 70:
        return "A", 4.0

    elif subject_mark >= 60:
        return "A-", 3.5
    
    elif subject_mark >= 50:
        return "B", 3.0
    
    elif subject_mark >= 40:
        return "C", 2.0
    
    elif subject_mark >= 33:
        return "D", 1.0
    
    else:
        return "F", 0.0
    
subjects = input("How many subjects do you want to calculate GPA for? ")
total_points = 0
marks_result = {}

try:
    subjects = int(subjects)
except ValueError:
    print("Invalid input. Please enter an integer value.")

for i in range(subjects):
    subject_name = input("Name of subject: ").title().strip()
    subject_mark = int(input(f"Marks obtained in {subject_name}: "))   
    subject_gread , subject_point = exam_marks_grade_and_point_calculator(subject_mark)
    total_points += subject_point
    marks_result[subject_name] = subject_gread , subject_point

print("\n-------------- Results -------------")
for subject_name , (subject_gread , subject_point) in marks_result.items():    
    print(f"\033[92m{subject_name}\033[1m - \033[0mGrade: {subject_gread}, GPA: {subject_point}")
    
print("------------------------------------")
subjects_GPA = total_points / subjects
print(f"\033[92mTotal GPA: \033[0m{round(subjects_GPA,2)}")