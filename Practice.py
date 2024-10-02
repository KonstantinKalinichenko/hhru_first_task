def get_passed():
    scores = input("Please enter the  students' scores separated by commas:")
    students = input("Please enter the students' names separated by commas:")

    stud_list = students.split(',')
    score_list = list(map(int, scores.split(',')))

    stud_score = [(stud.strip(), score) for stud, score in zip(stud_list, score_list)]
    passed = ', '.join([name for name, score in stud_score if score >= 35])

    if passed:
        return f"{passed} passed the exam!"
    else:
        return 'None passed the exam.'


print(get_passed())