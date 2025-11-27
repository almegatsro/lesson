import sys
def initial_phonebook():
    rows, cols = int(input("please enter number of contacts: ")), 5
    phone_book =[]
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("Note: * Indicates Mandatory Fields")
        print("....................................................")
        temp = []

        for j in range(cols):
            if j == 0:
                temp.append(str(input("Enter Name*: ")))
                if temp[j] == '' or temp[j] = ' ':
                    sys.exit("NAme is a Mandatory Field, Process is exiting due to Balnk Field.....")
            if j == 1:
                temp.append(int(input("Enter Number*: ")))
            if j == 2:
                temp.append(str(input("Enter Email Address: ")))
                if temp[j] == '' or temp[j] ==' ':
                    temp[j] = None
            if j == 3:
                temp.append(str(input("Enter Date of Birth(dd/mm/yy):")))
                if temp[j] == '' or temp[j] ==' ':
                    temp[j] = None
            if j == 4:
                temp.append(str(input("Enter Category(Family/Friends/Work/Others): ")))
                if temp[j] == '' or temp[j] ==' ':
                    temp[j] = None

        phone_book.append(temp)

    print(phone_book)
    return phone_book


def menu():
    print("*************************************************************")
    print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
    print("*******************************************************************")
    print("\tYou can now perfom the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an Existing Contact")
    print("3. Delete All Contacts")
    print("4. Search for a contact")
    print("5. Display all Contacts")
    print("6. Exit Phone book")

    choice = int(input("Please Enter your Choice: "))
    return choice

def add_contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Enter Name: ")))
        if i == 1:
            dip.append(str(input("Enter Number: ")))
        if i == 2:
            dip.append(str(input("Enter E-mail address: ")))
        if i == 3:
            dip.append(str(input("Enter Date of Birth(dd/mm/yy): ")))
        if i == 0:
            dip.append(str(input("Enter Category(Family/Friends/work/others): ")))
    pb.append(dip)
    return pb

def remove_exixting(pb):
    query = (str(input("Please enter the name of the contact you wish to remove")))
    temp = 0
    
    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb.pop(i))
            print("This query has been removed")
            return pb
    if temp == 0:
        print("sorry, You have entered an invali query. \nPlease Recheck and try again later")
        return pb

def delete_all(pb):

