from pyscript import display, document

def calculate_average(e):
    student_name = document.getElementById('name')
    student_section = document.getElementById('section')
    fname = f'{student_name} {student_section}'

    math = document.getElementById('math').value
    science = document.getElementById('science').value
    english = document.getElementById('english').value
    history = document.getElementById('history').value
    art = document.getElementById('art').value

    document.getElementById('output').innerHTML = ''

    #calculator

    subjects = [math, science, english, history, art] #chosen subjects
    amount = [5, 5, 5, 4, 1] #hours for each subject

    
    avg = round((float(subjects[0]) * amount[0] +
        float(subjects[1]) * amount[0] +
        float(subjects[2]) * amount[1] +
        float(subjects[3]) * amount[0] +
        float(subjects[4]) * amount[1] +
        float(subjects[4]) * amount[2]) / 
        (amount[0] + amount[0] + amount[1] + amount[0] + amount[1] + amount[2]), 2)

    message = f'''Hello, {fname}. Your general weighted average is {avg}%. Keep up the good work!'''
    display('message', target='output')

    # used the old skills test as a /ref
    # used internet as a ref 
    # needs 2 .pys because the school clubs code is relatively difficult, accidentally deleted it multiple times when it was in thie document
    #assistance from classmate was used here thanks k 
