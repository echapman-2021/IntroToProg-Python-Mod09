# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
#EChapman, 3.11.2021 Opened Assignment
#EChapman, 3.14.2021, Modified code to complete Assignment 09
# ------------------------------------------------------------------------ #
file_name = "EmployeeData.txt"

if __name__ == "__main__":
    import DataClasses as D
    import ProcessingClasses as P
    import IOClasses as I
else:
    raise Exception("This file was not created to be imported")
# Main Body of Script  ---------------------------------------------------- #

objP1 = D.Person("Bob", "Smith")
objP2 = D.Person("Sue", "Jones")
lstTable = [objP1, objP2]


lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
lstTable.clear()
for line in lstFileData:
    lstTable.append(D.Employee(line[0], line[1], line[2].strip()))

I.EmployeeIO.print_current_list_items(lstTable)

while True:
    I.EmployeeIO.print_menu_items()
    user_choice = I.EmployeeIO.input_menu_options()
    if user_choice.strip() == '1':
        """Show user current data in the list of product objects"""
        print("*** Displaying Current Data: ***")
        I.EmployeeIO.print_current_list_items(lstTable)
        continue

    elif user_choice.strip() == '2':
        """User inputs new employee data, displays current data with user appended new data"""
        new_data = I.EmployeeIO.input_employee_data()
        print(type(new_data))
        lstTable.append(new_data)
        print("*** Displaying Current Data: ***")
        I.EmployeeIO.print_current_list_items(lstTable)
        continue

    elif user_choice.strip() == '3':
        """Saves data to file"""
        print("Saving data to file")
        print("...")
        P.FileProcessor.save_data_to_file("EmployeeData.txt", lstTable)
        print("Checking if went through")
        lstFileData = P.FileProcessor.read_data_from_file("EmployeeData.txt")
        for row in lstFileData:
            p = D.Person(row[0], row[1])
            print(p.to_string().strip(), type(p))
        print("Data Saved!")
        continue


    elif user_choice.strip() == '4':
        """Let user exit program"""
        print("Goodbye")
        break
# Main Body of Script  ---------------------------------------------------- #