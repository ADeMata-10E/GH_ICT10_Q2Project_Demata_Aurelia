from pyscript import display, document

def calculate_average(e):
    student_name = document.getElementById('name')
    student_section = document.getElementById('section')

    mathgrade = document.getElementById('M').value
    sciencegrade = document.getElementById('S').value
    englishgrade = document.getElementById('E').value
    historygrade = document.getElementById('H').value)
    artgrade = document.getElementById('A').value

    document.getElementById('output').innerHTML = ''

    #calculator

    

    message = f'''Report Card Summary:  
    Student Name: {student_name},  
    Section: {student_section}, 
    Your general weighted average is {average}%.  
    Keep up the good work!'''
    display('message', target='output')

    # used the old skills test as a /ref
    # used internet as a ref 
    # needs 2 .pys because the school clubs code is relatively difficult, accidentally deleted it multiple times when it was in thie document
    #assistance from classmate was used here thanks k 
