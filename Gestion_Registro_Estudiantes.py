student_records = {}

def add_student(name, age, courses):
    if name in student_records:
        print(f"Student '{name}' alredy exists.")
    else:
        student_records[name] = {
            "age": age,
            "grades": set(),
            "courses": set(courses)
        }
        print(f"Student '{name}' added successfully.")

def add_grade(name, grade):
    if name in student_records:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
    else:
        print(f"Student '{name}' not found.")

def is_enrolled(name, course):
    if name in student_records:
        if course in student_records[name]["courses"]:
            return True
        else:
            return False
    else:
        print(f"Student '{name}' not found.")
        return False

def calculate_average_grade(name):
    if name not in student_records:
        print(f"Student '{name}' not found.")
        return None
    
    grades = student_records[name]["grades"]
    
    if not grades:
        return 0
    
    return float(sum(grades) / len(grades))

def list_students_by_course(course):
    students_in_course = []
    
    for name, data in student_records.items():
        if course in data["courses"]:
            students_in_course.append(name)
            
    return students_in_course

def filter_top_students(threshold):
    return [name for name in student_records if calculate_average_grade(name) > threshold]

add_student("Alice", 20, ["Math", "Physics"])
add_student("Bob", 22, ["Math", "Biology"])
add_student("Diana", 23, ["Chemistry", "Physics"])
add_grade("Alice", 90)
add_grade("Alice", 85)
add_grade("Bob", 75)
add_grade("Diana", 95)
print(filter_top_students(80))  # Debería devolver ["Alice", "Diana"]
print(filter_top_students(90))  # Debería devolver ["Diana"]
print(filter_top_students(100))  # Debería devolver una lista vacía