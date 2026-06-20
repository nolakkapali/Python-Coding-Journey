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

#2)Calculate semester gpa
def calculate_semester_cgpa(subject,semester):
    add_semester_record(subject,semester)
    #tuple unpacking
    sum=0
    total_credit=0
#Courses are: ('121', 'dg', 3.0, 4.0, '213', 'dgd', 3.0, 4.0)
#Semester Record: (1, ('121', 'dg', 3.0, 4.0, '213', 'dgd', 3.0, 4.0))
    for i in semester:
        (course_code,course_name,course_credit,course_grade_point)=subject[2::]
        print(subject[course_code],subject[course_name])
        credits_gpa= subject[course_credit]*subject[course_grade_point]
        sum=sum+credits_gpa
        total_credit=total_credit+subject[course_credit]
    print("Semester GPA:",sum/total_credit)










#Main Program
while True:

    print("1. Input New Semester Results\n2. View Semester-wise GPA\n3.Calculate CGPA\n4. Generate Full Academic Transcript\n0. Exit")
    user=int(input("Enter Your Choice:"))
    if user==1:
        print("Semester Record:",semester_record)
        course_tuple,semester_record=add_semester_record(course_tuple,semester_record)
        print("Courses are:",course_tuple,"Semester Record:",semester_record)
    elif user==2:
        calculate_semester_cgpa(course_tuple,semester_record)
    elif user==3:
        calculate_cgpa(course_tuple,semester_record)
    elif user==4:
        calculate_academic_transcript(course_tuple,semester_record)
    else:
        break
