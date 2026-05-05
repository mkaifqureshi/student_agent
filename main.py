students_list = []
unique_names = set()

while True :
    print('\n===========AGENT STUDENT SYSTEM===========')
    print('1. ADD STUDENT')
    print('2. SEE ALL STUDENTS')
    print('3. SEARCH STUDENT BY NAME')
    print('4. EXIT')

    choice = input('ENTER YOUR CHOICE : ')

    match choice :
        case '1':
            name = input('TYPE STUDENT NAME  : ')
            if name in unique_names:
                print('STUDENT ALREADY EXIST')
                continue

            age = int(input('TYPE STUDENT AGE : '))
            marks_input = input('TYPE STUDENT MARKS (comma separated) : ')
            marks_list = marks_input.split(',')
            marks_list = [int(m) for m in marks_list]
            average = sum(marks_list) / len(marks_list)
            grade = ''
            if average >=80:
                grade = 'A'
            elif average >=60:
                grade = 'B'
            elif average >=40:
                grade = 'C'
            elif average <40:
                grade = 'FAILED'

            if average >=85:
                print('TOP STUDENTS')
            elif average < 40:
                print('NEED IMPROVEMENT')
            student_data = {
                'name': name,
                'age': age,
                'marks': marks_list,
                'average': average,
                'grade': grade
            }
            students_list.append(student_data)
            unique_names.add(name)
            print('MUBARAK HO ! STUDENT ADDED SUCCESSFULLY')                      
        case '2':
            print("\n--- 📋 ALL STUDENT PROFILES ---")

            # Check karein ke list khali to nahi
            if not students_list:
                print("Abhi tak koi student add nahi hua!")
            else:
                for s in students_list:
                    # Step A: Marks ko string mein badal kar comma se jorna
                    readable_marks = ", ".join(map(str, s['marks']))

                    # Step B: Har student ka data print karna
                    print(f"NAME: {s['name']} | AGE: {s['age']} | MARKS: [{readable_marks}] | AVG: {s['average']:.2f} | GRADE: {s['grade']}")
        case '3':
            search_name = input('ENTER STUDENT NAME TO SEARCH : ')
            found_students = [s for s in students_list if s['name'].lower() == search_name.lower()]
            if found_students:
                for s in found_students:
                    readable_marks = ", ".join(map(str, s['marks']))
                    print(f"NAME: {s['name']} | AGE: {s['age']} | MARKS: [{readable_marks}] | AVG: {s['average']:.2f} | GRADE: {s['grade']}")
            else:
                print('STUDENT NOT FOUND')
        case '4':
            print('THANK YOU FOR USING THE SYSTEM')
            break
        case _:
            print('INVALID CHOICE, PLEASE TRY AGAIN')
