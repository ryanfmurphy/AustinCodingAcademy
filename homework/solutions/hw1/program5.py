# Fancy fortune cookie
def get_random_fortune():
    import urllib2
    fortune_url = 'http://www.fortunecookiemessage.com'
    resp = urllib2.urlopen(fortune_url)
    html = resp.read()

    start_flag = 'cookie-link">'
    fortune_start =  html.index(start_flag) + len(start_flag)
    fortune_end = html.index('<', fortune_start)
    fortune =  html[fortune_start:fortune_end]
    if not fortune or len(fortune) > 70:
        return get_random_fortune()
    else:
        return fortune

def print_ascii_frame(message):
    l_border = "<<"
    r_border = ">>"
    msg_flair = " ~ ~ "

    msg_with_flair = msg_flair + message + msg_flair
    msg_size = len(msg_with_flair)

    msg_line = l_border + msg_with_flair + r_border
    header_footer = l_border + "=" * msg_size + r_border
    blank_line = l_border + " " * msg_size + r_border

    print(header_footer)
    print(blank_line)
    print(msg_line)
    print(blank_line)
    print(header_footer)

print_ascii_frame(get_random_fortune())
