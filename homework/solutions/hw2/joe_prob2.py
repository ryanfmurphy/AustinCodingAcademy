def get_nonwhitespace_chars(opened_file, num_chars):
    valid_chars = ''
    num_valid_chars = 0

    while num_valid_chars < num_chars:
        c = opened_file.read(1)
        if not c:
            break

        if not c.isspace():
            valid_chars += c
            num_valid_chars += 1

    return valid_chars

def print_zigzag_right(s):
    size = len(s)
    for i in xrange(size):
        c = s[i]
        print(' ' * i + c)

def print_zigzag_left(s):
    size = len(s)
    for i in xrange(size):
        c = s[i]
        print(' ' * (size-i) + c)

def print_file_zigzag(file_path):
    zigzag_width = 20
    go_right = True

    with open(file_path) as f:
        text_chunk = get_nonwhitespace_chars(f, zigzag_width)
        while text_chunk:
            if go_right:
                print_zigzag_right(text_chunk)
            else:
                print_zigzag_left(text_chunk)

            go_right = not go_right
            text_chunk = get_nonwhitespace_chars(f, zigzag_width)

print_file_zigzag('zigzag.txt')
