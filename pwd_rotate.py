import subprocess
import string
import random

#subprocess module is used to run the query
#string module is used to create new password
#random module is used to generate some random characters for password

#Get current password from the user
current_password = input("Enter the current password : ")

#Generate a new password
new_passowrd = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(20))

#Change the password using subprocess
subprocess.run(['mysql', '-u-, 'root', '-p' + current_password, '-e', f"AlTER USER 'root'@'localhost' IDENTIFIED BY '{new_password}';"])

#Print and store new passowrd in a file
print(f"The new My SQL password is : {new_password}")
with open('/home/my_access/mysql_secret_password.txt', 'w') as f:
          f.write(new_password)
