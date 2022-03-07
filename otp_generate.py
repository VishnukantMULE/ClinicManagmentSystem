import mysql.connector

# establishing the connection
conn = mysql.connector.connect(
    user='root', password='', host='127.0.0.1', database='clinic_managment_system')

# Creating a cursor object using the cursor() method
cursor = conn.cursor()
fname=input("FNAME")
lname=input("lname")
gender=input("gender")
mobile=input("mobile")
email=input("email")
dob=input("dob")
add=input("add")
pincode=input("pincode")
state=input("state")




# Preparing SQL query to INSERT a record into the database.
insert_stmt = (
    "INSERT INTO pateint_details(First_Name, Last_Name,Gender,Mobile,Email,D_O_B,Address,Pincode,State)"
    "VALUES (%s, %s, %s, %s, %s ,%s ,%s ,%s ,%s)"
)
data = (fname, lname, gender,mobile,email,dob,add,pincode, state)

try:
    # Executing the SQL command
    cursor.execute(insert_stmt, data)

    # Commit your changes in the database
    conn.commit()

except:
    # Rolling back in case of error
    conn.rollback()

print("Data inserted")

# Closing the connection
conn.close()