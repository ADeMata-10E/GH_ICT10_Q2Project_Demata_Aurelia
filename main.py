from pyscript import display, document

def calculate_average(e):
    student_name = document.getElementById('name').value
    student_section = document.getElementById('section').value

    math = int(document.getElementById('math').value)
    science = int(document.getElementById('science').value)
    english = int(document.getElementById('english').value)
    history = int(document.getElementById('history').value)
    art = int(document.getElementById('art').value)

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

    if avg > 75
        display(f'You passed!', target='output')
    else 
        display(f'You failed', target='output')
    

    message = f'''Hello, {student_name} {student_section}. Your general weighted average is {avg}%. Keep up the good work!'''
    display(message, target='output')
    

    # used the old skills test as a /ref
    # used internet as a ref 
    # needs 2 .pys because the school clubs code is relatively difficult, accidentally deleted it multiple times when it was in thie document
    #assistance from classmate was used here thanks k 
