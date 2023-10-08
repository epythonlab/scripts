# Underscore Placeholder - 
#   Ignoring Values

# List of student tuples 
# containing names and test scores
students = [("Alice", 95),
            ("Bob", 88),
            ("Charlie", 92),
            ("David", 78)]

for student, _ in students:
    print(student)