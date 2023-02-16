# Login(Admin)
`http://127.0.0.1:8000/api/token/`

{
    "username": 
        "admin"
    ,
    "password": 
        "admin"
}


# create(admin)

`http://127.0.0.1:8000/create/`

{
    "Employee_Name": 
        "test"
    ,
    "Contact_Number": 
        "9495434706"
    ,
    "Emergency_Contact_Number": 
        "9495434706"
    ,
    "Address": 
        "home"
    ,
    "Postion": 
        "dob"
    ,
    "DOB": 
        "2020-10-10"
    ,
    "Blood_Group": 
        "O +ve"
    ,
    "Job_Title": 
        "job"
    ,
    "work_Location": 
        "ktm"
    ,
    "Reporting_to": 
        "sad"
    ,
    "Linked_In": 
        "https//www.linkedin.com"
    ,
    "Email": 
        "test@gmail.com"
    ,
    "Password": 
        "test"
    
}

# list all employees(admin)

`http://127.0.0.1:8000/employees/`

[
    {
        "user": 6,
        "Employee_Id": 1,
        "Employee_Name": "kris",
        "Contact_Number": 9496791108,
        "Email": "kris.2610@gmail.com",
        "Postion": "Back end trainee",
        "Reporting_to": "Geethu",
        "work_Location": "Work from home"
    },
    {
        "user": 7,
        "Employee_Id": 2,
        "Employee_Name": "test",
        "Contact_Number": 9495434706,
        "Email": "test@gmail.com",
        "Postion": "dob",
        "Reporting_to": "sad",
        "work_Location": "ktm"
    }
]


# Particular employee detail

`http://127.0.0.1:8000/employee/2`

{
    "Employee_Id": 2,
    "Employee_Name": "test",
    "Contact_Number": 9495434706,
    "Emergency_Contact_Number": 9495434706,
    "Address": "home",
    "Postion": "dob",
    "DOB": "2020-10-10",
    "Martial_status": false,
    "Blood_Group": "O +ve",
    "Job_Title": "job",
    "work_Location": "ktm",
    "Date_of_Joining": "2023-02-14",
    "Reporting_to": "sad",
    "Linked_In": "https://www.linkedin.com/in/dheeraj-kumar-s-2106411ba",
    "Profile_Picture": null,
    "Email": "test@gmail.com",
    "Password": "test",
    "user": 7
}

# Delete user(admin)
`http://127.0.0.1:8000/employee/delete/2`


Update employee(admin)
http://127.0.0.1:8000/employee/update/2

List all leaves(admin)
http://127.0.0.1:8000/leaves/


Approve Leaves(admin)
http://127.0.0.1:8000/leaveapprove/1/

Approve Multiple leave of same employee(admin)
http://127.0.0.1:8000/leaveapprove/1/10/


Status of leave(admin)
Approved : http://127.0.0.1:8000/leave/approved/

Pending: http://127.0.0.1:8000/leave/pending/

Sorting employees(admin)
Ascending: http://127.0.0.1:8000/sortemployees/asc/
Descending: http://127.0.0.1:8000/sortemployees/desc/

Search Employee(Admin)
http://127.0.0.1:8000/searchemployee/1/




User Login
http://127.0.0.1:8000/login/

{
    "username":"test@gmail.com",
    "password":"test"
}

User Apply Leave
http://127.0.0.1:8000/leaveapply/7/ POST Method
{
    "nature_of_leave":"sick",
    "first_Day":"2020-02-10",
    "last_Day":"2020-02-12"
}


list user leaves 
http://127.0.0.1:8000/myleave/7/

Sort leaves of particular user
http://127.0.0.1:8000/sortedleaves/7/asc/
http://127.0.0.1:8000/sortedleaves/7/desc/

Search Leaves of particular user
http://127.0.0.1:8000/searchleave/7/2020-02-10/

Logout
http://127.0.0.1:8000/logoutuser/





