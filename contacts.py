contacts = {
    'number': 4,
    'students': 
        [
            {'name': 'John', 'email': 'john@example.com'},
            {'name': 'Jane', 'email': 'jane@example.com'},
            {'name': 'Doe', 'email': 'doe@example.com'},
            {'name': 'Smith', 'email': 'smith@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])