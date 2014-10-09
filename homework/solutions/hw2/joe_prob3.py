import urllib2

def read_test_file(file_path):
    if file_path.startswith('http://'):
        resp = urllib2.urlopen(file_path)
        file_contents = resp.read()
    else:
        with open(file_path) as f:
            file_contents = f.read()
    return file_contents

def parse_test_file(test_file_contents):
    file_lines = test_file_contents.split('\n')

    # Skip test title and date
    file_lines.pop(0)
    file_lines.pop(0)

    lines_per_student = 3
    num_students = len(file_lines) / lines_per_student

    current_line_num = 0
    current_student = ''
    current_grade = 0
    total_grade = 0
    max_grade = 0
    max_student = ''

    for line in file_lines:
        if current_line_num % lines_per_student == 0:
            current_student = line
        elif current_line_num % lines_per_student == 2:
            current_grade = int(line)
            total_grade += current_grade

            if current_grade > max_grade:
                max_grade = current_grade
                max_student = current_student

        current_line_num += 1

    score_details = {
        'max_grade': max_grade,
        'student': max_student,
        'class_avg': float(total_grade) / num_students
    }
    return score_details

def test_data_as_string(test_data):
    results = "The average test score: %.1f\n" % test_data['class_avg']
    results += "The highest test score: %d\n" % test_data['max_grade']
    results += "Student who scored the highest: %s\n" % test_data['student']
    return results

test_file_path = raw_input('Enter a the location of the test data file: ')

test_file_contents = read_test_file(test_file_path )
test_data = parse_test_file(test_file_contents)

print(test_data_as_string(test_data))

user_input = raw_input('Enter a file path to save this data, or q to quit: ')
if user_input.lower() == 'q':
    print("Exiting")
else:
    with open(user_input, 'w') as f:
        f.write(test_data_as_string(test_data))
    print("Data saved to %s" % user_input)
