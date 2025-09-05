official_courses = {
"Math", "Physics", "Computer Science", "Biology", "Chemistry",
"Statistics", "English", "Economics", "History", "Philosophy",
"Sociology", "Political Science", "Geography", "Psychology",
"Art", "Music", "Engineering", "Law", "Medicine", "Business"
}

students = {}

def create_student():
	username = input("Enter a unique username: ")

	if username in students:
		print("Username already exists!")
		return

	name = input("Enter student name: ")
	age = int(input("Enter student age: "))
	city = input("Enter city: ")
	zip_code = input("Enter zip code: ")
    

	print("\nAvailable Courses:")
	print(", ".join(official_courses))
    
	courses = input("Enter courses (comma separated): ").split(",")
    
    # Clean spaces and only accept valid courses
	course_list = []
	for c in courses:
		c = c.strip()        # remove spaces
		if c in official_courses:   # only allow valid course
			if c not in course_list:  # avoid duplicates
				course_list.append(c)
    
    # Save student details inside dictionary
	students[username] = {
		"name": name,
		"age": age,
		"courses": course_list,    # use list for courses (simple)
		"address": {"city": city, "zip": zip_code}   # another dictionary for address
}
    
print("Student created successfully!\n")


def display_student(username):
    # Show full record
	if username in students:
		print(students[username])
	else:
		print("Student not found.")


def display_courses(username):
    # Show only courses
	if username in students:
		print("Courses:", students[username]["courses"])
	else:
		print("Student not found.")

def display_zip(username):
    # Show only zip
	if username in students:
		print("Zip:", students[username]["address"]["zip"])
	else:
		print("Student not found.")


def display_city(username):
    # Show only city
	if username in students:
		print("City:", students[username]["address"]["city"])
	else:
		print("Student not found.")


def add_course(username):
    # Add a new course
	if username not in students:
		print("Student not found.")
		return
    
	course = input("Enter course to add: ").strip()
    
	if course in official_courses:  # only allow valid course
		if course not in students[username]["courses"]:
			students[username]["courses"].append(course)
			print(f"{course} added successfully.")
		else:
			print("Course already enrolled.")
	else:
			print("Course not offered by department.")


def remove_course(username):
    # Remove a course
	if username not in students:
		print("Student not found.")
		return
    
	course = input("Enter course to remove: ").strip()
    
	if course in students[username]["courses"]:
		students[username]["courses"].remove(course)
		print(f"{course} removed.")
	else:
		print("Course not found in student’s list.")


def update_student(username):
    # Update student details
	if username not in students:
		print("Student not found.")
		return
    
	name = input("Enter new name (leave blank to skip): ")
	age = input("Enter new age (leave blank to skip): ")
	city = input("Enter new city (leave blank to skip): ")
	zip_code = input("Enter new zip (leave blank to skip): ")

	if name != "":
        	students[username]["name"] = name
	if age != "":
		students[username]["age"] = int(age)
	if city != "":
		students[username]["address"]["city"] = city
	if zip_code != "":
		students[username]["address"]["zip"] = zip_code
    
	print("Student record updated.")

def total_students():
    # Count number of students
	print(f"Total students: {len(students)}")

def menu():
	while True:
		print("\n===== Student Management System =====")
		print("1. Create Student")
		print("2. Display Student Record")
		print("3. Display Courses")
		print("4. Display Zip Code")
		print("5. Display City")
		print("6. Add Course")
		print("7. Remove Course")
		print("8. Update Student")
		print("9. Show Total Students")
		print("0. Exit")

		option = input("Choose an option: ")

		if option == "1":
			create_student()
		elif option == "2":
			username = input("Enter username: ")
			display_student(username)
		elif option == "3":
			username = input("Enter username: ")
			display_courses(username)
		elif option == "4":
			username = input("Enter username: ")
			display_zip(username)
		elif option == "5":
			username = input("Enter username: ")
			display_city(username)
		elif option == "6":
			username = input("Enter username: ")
			add_course(username)
		elif option == "7":
			username = input("Enter username: ")
			remove_course(username)
		elif option == "8":
			username = input("Enter username: ")
			update_student(username)
		elif option == "9":
			total_students()
		elif option == "0":
			print("Exiting... Goodbye!")
			break
		else:
			print("invalid")
	

menu()
