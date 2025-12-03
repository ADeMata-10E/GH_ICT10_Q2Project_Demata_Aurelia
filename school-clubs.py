
from pyscript import display, document

cluboptions = {
               
"Band" : {
"Description" : "touch grass guys",
"Advisor" : "Mr. Smith",
"Meeting Time" : "Fridays at 3 PM",
"Location" : "Music Room",
"Amt. of Members" :  20,
"Category" : "Non-academic",
},

"Chess" : {
"Description" : "touch grass more",
"Advisor"  : "Ms. Johnson",
"Meeting Time" : "Tuesdays and Thursdays at 4 PM",
"Location" : "Auditorium",
"Amt. of Members" : 15,
"Category"  : "Non-academic",
},

"Social Studies": {
"Description" : "history council",
"Advisor" : "Ms. Lee",
"Meeting Time" : "Wednesdays at 2 PM",
"Location" : "Room 204",
"Amt. of Members" : 25,
"Category" : "Academic"
},

"Science" : {
"Description" : "boom boom goes the test tube.",
"Advisor" : "Dr. Brown",
"Meeting Time" : "Mondays at 3 PM",
"Location" : "Lab 1",
"Amt. of Members" : 19,
"Category": "Academic" },

"Art": {
"Description" : "the most uneventful club ever",
"Advisor"  : "Ms. Green",
"Meeting Time" : "Thursdays at 2 PM",
"Location" : "Music Room",
"Amt. of Members" : 22,
"Category": "Non-academic"
},

} 


#dictionary


def show_club(e):
       document.getElementById("output").innerText=""
       club_name = document.getElementById("clubmaterial").value
       display(f"Description:{cluboptions[club_name]['Description']}", target="output")
       display(f"Advisor:{cluboptions[club_name]['Advisor']}", target="output")
       display(f"Meeting Time:{cluboptions[club_name]['Meeting Time']}", target="output")
       display(f"Location:{cluboptions[club_name]['Location']}", target="output")
       display(f"Amt. of Members:{cluboptions[club_name]['Amt. of Members']}", target="output")
       display(f"Category:{cluboptions[club_name]['Category']}", target="output")

       

#Dictionary display in the HTML element with id 'output'

