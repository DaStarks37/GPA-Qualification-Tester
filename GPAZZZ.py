# Dane Starks #
#  GPAZZZ.py  #
# This program asks for a last name and first name, then tests to see if you qualify for the Honor Roll or Deans list. #

while True:
    lastnameinput = input("Enter Last Name: ")
    if lastnameinput == "ZZZ":
        print("Ending Task.")
        break
    else:    
        firstnameinput = input("Enter First Name: ")
        gpainput = float(input("Enter GPA: "))
        if gpainput < 3.25:
            print(firstnameinput + " " + lastnameinput + " doesn't qualify for Deans List or Honor Roll.")
        elif gpainput >= 3.25 and gpainput < 3.5:
            print(firstnameinput + " " + lastnameinput + " qualifies for the Honor Roll!")
        elif gpainput >= 3.5:
            print(firstnameinput + " " + lastnameinput + " qualifies for Deans List!")