#core data structure
course_tuple=()
semester_record=()

#1)add_semester_record()--
def add_semester_record(subject,semester):
    semester_num=int(input("Enter Semester No-"))
    course_num=int(input("How many courses are there-"))

    for i in range(course_num):
        course_code=input("Enter Course Code-")
        course_name=input("Enter Course Name-")
        course_credit=float(input("Enter Course Credit-"))
        course_grade_point=float(input("Enter Course Grade Point- "))
        sub=(course_code,course_name,course_credit,course_grade_point)
        subject=subject+sub
    print(subject)
    semester=(semester_num,subject)
    return subject,semester






#Main Program
while True:

    print("1. Input New Semester Results\n2. View Semester-wise GPA\n3.Calculate CGPA\n4. Generate Full Academic Transcript\n0. Exit")
    user=int(input("Enter Your Choice:"))
    if user==1:
        course_tuple,semester_record=add_semester_record(course_tuple,semester_record)
        print(course_tuple,semester_record)
    elif user==2:
        calculate_semester_cgpa()
    elif user==3:
        calculate_cgpa()
    elif user==4:
        calculate_academic_transcript()
    else:
        break
