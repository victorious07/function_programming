'''
Author Name :Sanjay Jaiswal
Date        :15/06/2020
Description :To display student name and their laptop details
Input       :Enter the total no. of student: 2

             Enter student 1 name: Sanjay

             Enter Sanjay's laptop details: 
             1. Enter company	: Lenovo
             2. Enter Ram(GB)	: 8
             3. Enter Price(Rs)	: 25000
             ..................................................................

             Enter student 2 name: Sandeep

             Enter Sandeep's laptop details: 
             1. Enter company	: hp
             2. Enter Ram(GB)	: 12
             3. Enter Price(Rs)	: 35000
             ...................................................................


Output      :Displaying student names with their laptap details: 
             ...................................................................

            Name of the student:  Sanjay

            Laptop Details:
            Company	: Lenovo
            Ram	: 8.0GB
            Price	: Rs25000.0
            ....................................................................

            Name of the student:  Sandeep

            Laptop Details:
            Company	: hp
            Ram	: 12.0GB
            Price	: Rs35000.0
            .....................................................................
'''    

class student:                                        #class student definition 
    def __init__(self, name):
        self.name = name                              #passing student name and assiging it to class instance variable

    def display_name(self):                            #function to display name of the current student
        print("\nName of the student: ", self.name)

    class laptop:                                       #inner class definition
        def __init__(self, company, ram, price):        #collecting company, ram and price of the class in from inner class object
            self.company = company                      #and assiging to its instance variable
            self.ram = ram
            self.price = price
        def display_details(self):
            print("\nLaptop Details:\nCompany\t: {}\nRam\t: {}GB\nPrice\t: Rs{}".format(self.company, self.ram, self.price))
            print("...............................................................")

total_stu = int(input("Enter the total no. of student: "))

total_stu += 1    #increasing total student plus 1 because using range function in loop and instead of student 0 start from student 1...

stu_list = []         #student list to keep the student names
pc_detail_list = []   #to keep the laptop details for each student in thr form of list of tuples

for i in range(1, total_stu):                             #iterate as per the number of students
    name = input("\nEnter student "+str(i)+" name: ")
    stu_list.append(name)                                 #input name and add to the list

    print("\nEnter "+name+"'s laptop details: ")
    company = input("1. Enter company\t: ")
    ram = float(input("2. Enter Ram(GB)\t: "))
    price = float(input("3. Enter Price(Rs)\t: "))
    pc_detail_list.append((company, ram, price))        #taking 3 inputs and adding tuple of 3 element for company, ram and price

    print("..................................................................")

total_stu -= 1                                          #reducing back as numbers not needed for now
print("\n\nDisplaying student names with their laptap details: ")
print(".......................................................................")

for i in range(total_stu):                              #creating class instance or object and passing student name as per the index 
    stu_obj = student(stu_list[i])            
    stu_obj.display_name()                              #display student name

    laptop_det_obj = stu_obj.laptop(pc_detail_list[i][0], pc_detail_list[i][1], pc_detail_list[i][2]) #passing laptop details using outer
    laptop_det_obj.display_details()                                      #class object

