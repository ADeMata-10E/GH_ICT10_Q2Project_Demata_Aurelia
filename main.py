from pyscript import display, document

def calculate_average(e):
    mathgrade = float(document.getElementById('math').value or 0)
    sciencegrade = float(document.getElementById('science').value)
    englishgrade = float(document.getElementById('english').value)
    historygrade = float(document.getElementById('history').value)
    artgrade = float(document.getElementById('art').value)

    student_name = document.getElementById('name')
    student_section = document.getElementById('section')

    document.getElementById('output').innerHTML = ''

    hours = [4, 5, 3, 3, 1]  # corresponding credit hours for each subject

    subjects = [mathgrade, sciencegrade, englishgrade, historygrade, artgrade]

    weighted_average = sum(grade * hours for grade, hours in zip(subjects, hours)) / sum(hours)
    total_hours = sum(hours)
    average = round(weighted_average / total_hours, 2)
    

    message = f'Report Card Summary:  Student Name: {student_name},  Section: {student_section}, Your general weighted average is {average}%.  Keep up the good work!'
    display('message', target='output')

    # used the old skills test as a /ref
    # used internet as a ref 

