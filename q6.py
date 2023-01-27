def student_data(student_id , **kwargs):
    print(f"Student id is {student_id}")
    if "student_name" in kwargs:
        print(f"The student name is {kwargs['student_name']}")
    if "student_name" and "student_branch" in kwargs:
        print(f"The student name is {kwargs['student_name']} and branch is {kwargs['student_branch']}")

def main():
    
    student_data(student_id="22105079")
    student_data(student_id="22105079" , student_name="GAUTAM" , student_branch="ECE")

main()
