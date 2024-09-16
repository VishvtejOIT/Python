'''
# Ex.2:
# from math import *
def percentage():
    marks=[89,85,91,94,95,97]
    # count=len(marks)
    # total=sum(marks)
    
    # total=0
    # for mark in marks:
    #     total+=mark
    
    # print(f"Total marks:",total)
    print(f"Percaentage:{round(sum(marks)/len(marks),2)}")

percentage()
# Ex.2:
def percentage():
    suresh={
        "Maths":89,
        "Science":85,
        "English":91,
        "History":94,
        "Geography":95,
        "Marathi":97,
    }
    total=0
    for subject in suresh:
        print(subject+":"+str(suresh[subject]))
        total+=suresh[subject]
        
    print(f"Suresh have total {total} marks")
    print(f"Suresh have {round(total/len(suresh),2)} %")

percentage()
'''

# Ex.3:
def percentage(student,name):
    total=0
    for subject in student:
        print(subject+":"+str(student[subject]))
        total+=student[subject]
    print(f"{name} Have {total} marks")
    return round(total/len(student),2)

name=input("Enter student name:")
student={
    "Maths":int(input("Enter marks of Math:")),
    "Science":int(input("Enter marks of Science:")),
    "English":int(input("Enter marks of English:")),
    "History":int(input("Enter marks of History:")),
    "Geography":int(input("Enter marks of Geography:")),
    "Marathi":int(input("Enter marks of Marathi:")),
}
result=percentage(student,name)
print(f"{name} have {result} %")
