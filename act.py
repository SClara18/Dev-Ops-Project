from datetime import datetime

teacher = "Ash Raju"
student = "Outis Rog"
major = "Cyber Security"
date = datetime.now().strftime("%Y-%m-%d")

menssage = f"""
###################
# Project phase3 #
###################

Date: {date}
Teacher: {teacher}
Student: {student}
Major: {major}

"""

print(menssage)
print("Phase 1 changed to phase3")
print("New commit added")
