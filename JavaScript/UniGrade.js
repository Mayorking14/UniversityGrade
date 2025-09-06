const prompt = require('prompt-sync')();
let students = [];

// List of official courses
const officialCourses = [
  "Math", "Physics", "Computer Science", "Biology", "Chemistry",
  "English", "Economics", "History", "Law", "Medicine", "Business"
];

// Create a new student
function createStudent(username, name, age, city, zip, courses) {
  // Check if username already exists
  for (let std of students) {
    if (std.username === username) {
      console.log("Username already exists!");
      return;
    }
  }

    let courseList = [];
  for (let c of courseList) {
    if (officialCourses.includes(c) && !courseList.includes(c)) {
      courseList.push(c);
    }
  }

  // Make a new student object
  let student = {
    username: username,
    name: name,
    age: age,
    city: city,
    zip: zip,
    courses: courseList
  };

  // Add to list
  students.push(student);
  console.log("Student created successfully!");
}

// Display a student’s full record
function displayStudent(username) {
  for (let pupil of students) {
    if (pupil.username === username) {
      console.log(pupil);
      return;
    }
  }
  console.log("Student not found.");
}

// Display only courses
function displayCourses(username) {
  for (let pupil of students) {
    if (pupil.username === username) {
      console.log("Courses:", pupil.courses);
      return;
    }
  }
  console.log("Student not found.");
}

// Display city
function displayCity(username) {
  for (let pupil of students) {
    if (pupil.username === username) {
      console.log("City:", pupil.city);
      return;
    }
  }
  console.log("Student not found.");
}

// Display zip code
function displayZip(username) {
  for (let pupil of students) {
    if (pupil.username === username) {
      console.log("Zip:", s.zip);
      return;
    }
  }
  console.log("Student not found.");
}

// Add a course
function addCourse(username, course) {
  for (let pupil of students) {
    if (pupil.username === username) {
      if (!officialCourses.includes(course)) {
        console.log("Course not offered.");
        return;
      }
      if (pupil.courses.includes(course)) {
        console.log("Already enrolled.");
      } else {
        pupil.courses.push(course);
        //console.log(${course} added.);
      }
      return;
    }
  }
  console.log("Student not found.");
}

// Remove a course
function removeCourse(username, course) {
  for (let pupil of students) {
    if (pupil.username === username) {
      let index = pupil.courses.indexOf(course);
      if (index !== -1) {
        pupil.courses.splice(index, 1);
       // console.log(${course} removed.);
      } else {
        console.log("Course not found.");
      }
      return;
    }
  }
  console.log("Student not found.");
}

// Update student details
function updateStudent(username, newName, newAge, newCity, newZip) {
  for (let pupil of students) {
    if (pupil.username === username) {
      if (newName) pupil.name = newName;
      if (newAge) pupil.age = newAge;
      if (newCity) pupil.city = newCity;
      if (newZip) pupil.zip = newZip;
      console.log("Student updated.");
      return;
    }
  }
  console.log("Student not found.");
}

// Show total students
function totalStudents() {
  console.log("Total students:", students.length);
}


function menu() {
      while (true) {
        let choice = prompt(
          "===== Student Management System =====\n" +
          "1. Create Student\n" +
          "2. Display Student\n" +
          "3. Display Courses\n" +
          "4. Add Course\n" +
          "5. Remove Course\n" +
          "6. Update Student\n" +
          "7. Show Total Students\n" +
          "0. Exit\n\n" +
          "Enter choice:"
        );

        if (choice === "1") createStudent();
        else if (choice === "2") displayStudent();
        else if (choice === "3") displayCourses();
        else if (choice === "4") addCourse();
        else if (choice === "5") removeCourse();
        else if (choice === "6") updateStudent();
        else if (choice === "7") totalStudents();
        else if (choice === "0") {
          console.log("Exiting...");
          break;
        } else {
          console.log("Invalid choice, try again.");
        }
      }
    }

  menu()