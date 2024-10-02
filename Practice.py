def get_passed():
    scores = input("Please enter the  students' scores separated by commas:")
    students = input("Please enter the students' names separated by commas:")
    stud_list = students.split(',')
    score_list = list(map(int, scores.split(',')))
    stud_score = dict(zip(stud_list, score_list))
    passed = ', '.join([k for k, v in stud_score.items() if v >= 35])
    if passed:
        return f"{passed} passed the exam!"
    else:
        return 'None passed the exam.'
print(get_passed())