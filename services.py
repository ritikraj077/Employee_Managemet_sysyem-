import pandas as pd
from datetime import datetime

df = pd.read_csv("attendance_data.csv")



def get_entry(employee_id):
    # Check if the employee ID exists in the DataFrame
    #if employee_id not in df['EmployeeID'].values:
        #return ("Employee ID not found")
             # return get_entry(employee_id)
        
    
    # Find the index of the employee_id
    row_ind = df[df['EmployeeID'] == employee_id].index[0]
    
    # Update the "EntryTime" column with the current date and time
    entry_col_name = "EntryTime"
    df.loc[row_ind, entry_col_name] = datetime.now().time()
    row = df.loc[row_ind]
    print(row)
    

    return "Entry time recorded"

def get_exit(employee_id):
    a= row_ind = df[df['EmployeeID'] == employee_id].index[0]
    if pd.isna(df.loc[a,"EntryTime"]):
        print("Employee's Entry is not done")
    else:
    
        entry_col_name = "ExitTime"


    # Assuming df is your DataFrame
        df.loc[a,  entry_col_name] = datetime.now().time()
        row = df.loc[a]
        print(row)
    

# Use datetime.datetime.now() instead of datetime.datetime.now().time()
        return "exit time recoreded"
    
    ##function for the new employee
def new_employee():
        employeeid = int(input("plezz enter your employe id : "))##taking input from the user 
        name = input("plezz enter your Name")
        Mobie_no = int(input("plezz enter your Mobile_no"))
        df.loc[len(df)] = {'EmployeeID': employeeid , ##usicg loc function to select the row and add the values in the dataframe
        'Name': name,
        'Mobile_No': Mobie_no ,
        'Date': "none"}
        #row = df.loc[index] = 
        #print(row)
        return "New employee record is created sucessfully"##returning the value out:
    
    
    
def check_user(employee_id):
    if df[df['EmployeeID'] == employee_id].empty:###select the emoloyee id column and if it iis eyal to the employee id then print existing user
        print("New user")
        return new_employee()##return new employee funstion to record the data
    else:
        print("Existing user")
        
        
def existing_emp(employee_id):
    if df[df['EmployeeID'] == employee_id].empty:###select the emoloyee id column and if it iis eyal to the employee id then print existing user
        print("Employee id is not Correct Plezz Enter the valid Id")
        return get_entry(employee_id)##return new employee funstion to record the data
    else:
        print("Existing user")
        
        
## function to add store changes in the dataframe
def save_changes():
    df.sort_values('EmployeeID',inplace = True)
    df.sort_index(inplace = True)
    
    df.to_csv("attendance_data.csv",index =False)
    return "Thank you "
        
        
def delete_record(employee_id):
    row_del_index = df[df['EmployeeID']== employee_id].index[0]
    
    df.drop(row_del_index, inplace=True)
    return "Employe details has been removed sucessfully"


def update_detail():
    employee_id = int(input("Enter your Employee ID: "))
    
    # Check if the employee ID is in the DataFrame
    if employee_id not in df['EmployeeID'].values:
        print("Employee ID not found.")
    else:
        # Get the index of the row with the specified Employee ID
        index = df[df['EmployeeID'] == employee_id].index[0]
        
        # Update the values
        name = input("Enter your Name: ")
        mobile_no = int(input("Enter your Mobile Number: "))
        #date = input("Enter the Date: ")

        # Using .loc to update the values in the DataFrame
        df.loc[index, ['Name', 'Mobile_No']] = [name, mobile_no]

        print("Employee information updated successfully.")
        row = df.loc[index]
        print(row)
        
#function to add data to the database :
      
def record_to_csv():
    df.to_csv("attendance_data.csv",index =False)
    return "Thank you "