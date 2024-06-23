from datetime import datetime

teacher = "Ash Raju"
student = "Outis Rog"
major = "Cyber Security"
date = datetime.now().strftime("%Y-%m-%d")

menssage = f"""
###################
# Project phase 1 #
:q
###################

Date: {date}
Teacher: {teacher}
Student: {student}
Major: {major}

"""

print(menssage)

