import json
import urllib2, urllib

def send_text_msg(to_num, txt_msg):
    url = 'http://opensms.joequery.me/sms'
    data = json.dumps({'to': to_num, 'body': txt_msg})
    request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    return urllib2.urlopen(request).read()

me = {
    'name': 'Ryan',
    'high school': 'J.J.Pearce',
}

friends = {
    'Ryan': '5127867383',
    'Samir': '5127457846',
    'Ian': '5128251908',
    'Paco': '8184977226',
    'Luke': '2014211574',
}

"""
def post(msg):
    global friends, me
    for friend in friends:
        num = friends[friend]
        send_text_msg(num, me['name'] + ': ' + msg)
"""

def post(msg):
    global friends, me
    data = urllib.urlencode({'friends':json.dumps(friends), 'me':json.dumps(me), 'msg':msg})
    return urllib2.urlopen("http://192.168.3.186:5000", data=data).read()

