#core data structure
course_tuple=()
semester_record=()

#1)add_semester_record()--
def add_semester_record(subject,semester):

    semester_num=int(input("Enter Semester No-"))
    course_num=int(input("How many courses are there-"))
    i=0
    while i<course_num:
        course_code=input("Enter Course Code-")
        course_name=input("Enter Course Name-")
        course_credit=float(input("Enter Course Credit-"))
        course_grade_point=float(input("Enter Course Grade Point- "))
        sub=(course_code,course_name,course_credit,course_grade_point)
        if course_code in subject or course_name in subject:
            print("The values are duplicate.please add it again!")
            continue
        subject=subject+sub
        i=i+1
    print(subject)
    semester=(semester_num,subject)
    return subject,semester

#2)Calculate semester gp
def calculate_semester_gpa(subject,semester):
    # if option 1 is already clicked and the semster record and course tuples are empty
    sem_num=int(input(("Which semester GPA Do u want to calculate:")))
    print("Courses are:",subject,"Semester Records:",semester)
    if sem_num in semester:
    # if option 1 is clicked and course and semester tuples are full and semester number is also in the semester tuple

        sum=0
        total_credit=0
        for i in range(0,len(subject),4):
            print("loop started")
            print(subject[i:i+4])
            (course_code,course_name,course_credit,course_grade_point)=subject[i:i+4]
            print(course_code,course_name)
            credits_gpa= course_credit*course_grade_point
            sum=sum+credits_gpa
            total_credit=total_credit+course_credit
        return sum/total_credit

    # if option 1 is not clicked and course and semester tuples are empty
    elif course_tuple is None and semester_record is None or sem_num not in semester:
        print("If your desired semester info are not added")
        print("Please add the semester and coures record before the GPA calculation-")

        while True:
            updated_sub,updated_sem=add_semester_record(subject,semester)
            if sem_num in updated_sem:
                sum=0
                total_credit=0
    #Courses are: ('121', 'dg', 3.0, 4.0, '213', 'dgd', 3.0, 4.0)
    #Semester Record: (1, ('121', 'dg', 3.0, 4.0, '213', 'dgd', 3.0, 4.0))
                for i in range(0,len(updated_sub),4):
                    print("loop started")
                    print(updated_sub[i:i+4])
                    (course_code,course_name,course_credit,course_grade_point)=updated_sub[i:i+4]
                    print(course_code,course_name)
                    credits_gpa= course_credit*course_grade_point
                    sum=sum+credits_gpa
                    total_credit=total_credit+course_credit
                break
            else:
                print("Sorry selected semester not added.Please add it again")
                continue

        return sum/total_credit






def calculate_cgpa(subject,semester):
    while True:
        sem_sub,sem_rec=add_semester_record(subject,semester)
        answer=input("Do you want to add more semester?(Yes/No):")
        if answer=="Yes":
            continue
        else:
            break

    sum=0
    total_credit=0
    print(sem_rec)
    for i in range(1,len(sem_rec),2):# ekane semester record nite hbe karon buja jacche na kon subject kon semester er
        print("loop started")
        print(sem_rec[i])
        (course_code,course_name,course_credit,course_grade_point)=sem_rec[i]
        print(course_code,course_name)
    #     credits_gpa= course_credit*course_grade_point
    #     sum=sum+credits_gpa
    #     total_credit=total_credit+course_credit
    #     i=i+2
    # cgpa=sum/total_credit
    # print("Your all semester cgpa is",cgpa)




#Main Program
while True:

    print("1. Input New Semester Results\n2. View Semester-wise GPA\n3.Calculate CGPA\n4. Generate Full Academic Transcript\n0. Exit")
    user=int(input("Enter Your Choice:"))
    if user==1:
        while True:
            print("Semester Record:",semester_record)
            course_tuple,semester_record=add_semester_record(course_tuple,semester_record)
            print("Courses are:",course_tuple,"Semester Record:",semester_record)
            answer=input("Do you want to add more semester?(Yes/No):")
            if answer=="Yes":
                continue
            else:
                break
    elif user==2:
        GPA=calculate_semester_gpa(course_tuple,semester_record)
        print("Semester GPA:",GPA)
        print("GPA is published!")
    elif user==3:
        calculate_cgpa(course_tuple,semester_record)
        print("All Semester CGPA is published!")
    elif user==4:
        calculate_academic_transcript(course_tuple,semester_record)
    else:
        break
