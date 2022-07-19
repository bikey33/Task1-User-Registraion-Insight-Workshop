import smtplib
from email.message import EmailMessage
import ssl
import os
def send_email(address):

    # For automatically sending registration verification email
    subject = " Verification of User Registration"
    message = """\
    
    Thank you for registering to our Academy. We will call you shortly after your desired course 
    enrollment starts. Kindly Contact +9837426767 if you have any query.
    Regards,
    Insight Workshop Academy
    """

    sender = 'bividjung33@gmail.com'
    eml = EmailMessage()# Creating EmailMesage Object
    # Defining attributes for above object
    eml['From'] = sender
    eml['To'] = address
    eml['Subject'] = subject
    eml.set_content(message)
    #Using SSL for Encrypted Secure email Data Transfer
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context = context) as smtp:
        smtp.login(sender,"wjlnshhemxdbztpk")
        smtp.sendmail(sender,address,eml.as_string())


class Users:
    def __init__ (self,id):
        # Constructor-->Adds User Id no when the object is created
        self.id = id


    def get_input(self):
        # To Register User Information

        self.firstname = input("Enter Your First Name\n")
        self.lastname = input("Enter Your Last Name\n")
        self.email = input("Enter Your Email Address\n")
        self.address = input("Enter Your Permanent Address")
        self.phone = input("Enter Your Phone Number\n")
        self.desiredcourse = input("Enter the course you want to enroll into\n")
        self.write_file()
        try:
            send_email(self.email)
            print("We Have Sent  Verfication Email to ", self.email,"Please Check the  Email\n")
        except Exception as e:
            print("Email is failed to send")
            print(e)



    def write_file(self):
        # Write all the user Registration Information to a file
        file= open('user_data.txt','a')
        #append every attributes to a list
        info_list = [self.firstname,self.lastname,self.email,self.phone, self.address,self.desiredcourse]
        for data in info_list:
            # Write all attributes individually to  file
            file.write(data + ",")
        file.write("\n")
        file.close()
        # Placing the new Line at the end
        # so every time new User's data will be placed on new line

    def update_file(self,email):
        file_r =open('user_data.txt','r')
        # Read the text from data containing file
        # Open another temporary file in write mode
        file_w= open('temp.txt','w')
        line = ' '
        while(line):#Checking EOF
            line = file_r.readline()
            content_list= line.split(',')
            # Split gives the list of Items contained
            # in a line and separated by ,.
            if (len(line) > 0):
                if content_list[2] == email: # Check if it contains the Email
                    self.firstname = input("Enter the Updated First Name")
                    self.lastname = input("Enter the Updated Last Name")
                    self.email = input("Enter the Updated Email")
                    self.phone = input("Enter the Updated Phone Number")
                    self.address =input("Enter the Updated Address")
                    self.desiredcourse = input ("Enter the Updated Desired Course")
                    info_list = [self.firstname, self.lastname, self.email, self.phone, self.address,
                                 self.desiredcourse]
                    # If contains email then write the line by new content in temp file
                    for data in info_list:
                        # Write all attributes individually to  file
                        file_w.write(data + ",")
                    file_w.write("\n")

                else:
                    #If don't have matching email, Just copy the line and write to temp file
                    file_w.write(line)
        file_w.close()
        file_r.close()
        # Just Delete the old file
        os.remove("user_data.txt")
        # Rename the temp file to original file
        os.rename("temp.txt",'user_data.txt')


    def delete_user(self,email):

        file_r = open('user_data.txt', 'r')
        # Read the text from data containing file
        file_w = open('temp.txt', 'w')
        # If the file contains line including given email
        # Write blank on the temp file
        # Otherwise just copy the read line from file_r
        line = ' '
        while (line):
            line = file_r.readline()
            content_list = line.split(',')
            if (len(line) > 0):
                if content_list[2] == email:
                    file_w.write("")
                    print("Record Sucessfully Deleted")
                else:
                    file_w.write(line)
        file_w.close()
        file_r.close()
        # Delete the original file
        os.remove("user_data.txt")
        #Rename the temporary file by older name
        os.rename("temp.txt", 'user_data.txt')

    def print_user(self,email):
        # Print a User details by Email
        file_r = open('user_data.txt', 'r')
        line = ' '
        while (line):
            line = file_r.readline()
            content_list = line.split(',')
            if (len(line) > 0):
                if content_list[2] == email:
                    # Assigning all the details contained on the list to
                    # attributes of object
                    self.firstname = content_list[0]
                    self.lastname = content_list[1]
                    self.email = content_list[2]
                    self.phone = content_list[3]
                    self.address = content_list[4]
                    self.desiredcourse = content_list[5]

        # Printing all the details
        print("Username:", self.firstname + " "+self.lastname)
        print("Email: ", self.email)
        print("Address:", self.address)
        print("Phone:" , self.phone)
        print("Course Desired:", self.desiredcourse)
    def print_all(self):
        file_r = open('user_data.txt', 'r')
        line = ' '
        index = 1
        while (line):
            line = file_r.readline()
            content_list = line.split(',')
            if (len(line) > 0):
                    # Assigning all the details contained on the list to
                    # attributes of object
                    self.firstname = content_list[0]
                    self.lastname = content_list[1]
                    self.email = content_list[2]
                    self.phone = content_list[3]
                    self.address = content_list[4]
                    self.desiredcourse = content_list[5]

                    # Printing all the details
                    print("User Entry Number:", index)
                    print("Username:", self.firstname + " " + self.lastname)
                    print("Email: ", self.email)
                    print("Address:", self.address)
                    print("Phone:", self.phone)
                    print("Course Desired:", self.desiredcourse)
                    print("-----------------------------")
            index += 1

if __name__ == '__main__':
    while(1):
        print(" Welcome to Insight Workshop Academy")
        print("-------------------------------------")
        print("Type 'U' if you are User\n")
        in_ch = input("Type 'A' if you are Admin\n")
        if(in_ch == 'U'or in_ch == 'u'):
            user1 = Users(1)
            user1.get_input()
        elif(in_ch == 'A' or in_ch == 'a'):
            while(1):
                print(" Welcome Admin")
                print("You can See All the User Records ,or Search and See Specific User Records ,or Update a User ,or Delete a User")
                print("Press 'A'---> If you want to See All the User Records")
                print("Press 'S'---> If you want to Search Specific User's Record by Email")
                print("Press 'U'---> If you want to  Update a User Record")
                print("Press 'D'---> If you want to Search and Delete Specific User\n")
                character_input = input("\n")
                if (character_input == 'A' or character_input == 'a'):
                    user = Users(1)
                    user.print_all()
                if (character_input == 'S' or character_input == 's'):
                    user1 = Users(1)
                    eml = input("Enter the User Email You want to See Record of\n")
                    user1.print_user(eml)
                if (character_input == 'U' or character_input == 'u'):
                    user1 = Users(1)
                    eml = input("Enter the User Email You want to Update\n")
                    user1.update_file(eml)

                if (character_input == 'D' or character_input == 'd'):
                    user1 = Users(1)
                    eml = input("Enter the User Email You want to Delete Records of\n")
                    user1.delete_user(eml)
                else:
                    print("Invalid Character!!\n")
                    ch = input("Press 'X' to Go Back\n")
                    if (ch == 'X'):
                        break
                    else:
                        pass
        else:
            print("You've entered the Invalid Character")
            ch = input("Enter 'Q' to quit the Application")
            if(ch == 'Q'):
                os._exit(0)




#user1.get_input()
#eml = input("Enter the User Email You want to Update\n")
#user1.delete_user(eml)
#user1.update_file(eml)
#user1.print_user(eml)
#user1.print_all()
