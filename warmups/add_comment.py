my_file = raw_input("Which file would you like to append some information? ")
raw_text = ''
new_data = raw_input("Please enter anything you would like to add at the end of the file: ")
'''
with open(myFile) as f:
    rawText = f.read()
'''

def add_comment(string_data, remark):
    string_data = string_data.strip()
    string_data += '\n'*2 + remark
    return string_data


def add_comment_to_file(file_name, remark):
    with open(file_name) as f:
        raw_text = f.read()

    with open(file_name, 'w') as f:
        f.write(add_comment(raw_text, remark))

if __name__ == "__main__":
    add_comment_to_file(my_file, new_data)