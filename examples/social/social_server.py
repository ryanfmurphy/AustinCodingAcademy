from flask import Flask, render_template, request, session
import json
import urllib2, urllib

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'mon_key'

def send_text_msg(to_num, txt_msg):
    url = 'http://opensms.joequery.me/sms'
    data = json.dumps({'to': to_num, 'body': txt_msg})
    request = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    return urllib2.urlopen(request).read()

def post_msg(me,friends,msg):
    for friend in friends:
        num = friends[friend]
        send_text_msg(num, me['name'] + ': ' + msg)

master_log = []

@app.route('/', methods=['GET','POST'])
def index():
    global master_log
    if request.method == 'POST':
        master_log.append({'me': json.loads(request.form['me']),
                           'friends': json.loads(request.form['friends']),
                           'msg': request.form['msg']})
        post_msg(   json.loads(request.form['me']),
                    json.loads(request.form['friends']),
                    request.form['msg'])
        return "Sending message..."
    else:
        return "You just did a GET.  Congrats!"

@app.route('/admin')
def admin():
    return str(master_log)

if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
