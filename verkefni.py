import pymysql
from bottle import *

@route('/')
def index():
       return template("index.tpl")

@route('/donyskra', method='POST')
def nyr():
    u = request.forms.get('user')
    p = request.forms.get('pass')
    n = request.forms.get('nafn')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2811992349', passwd='mypassword', db='2811992349_vefv7')
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM 2811992349_vefv7.users where user = %s",(u))

    result = cur.fetchone()

    if result[0] == 0:
        cur.execute("INSERT INTO 2811992349_vefv7.users Values(%s,%s,%s)",(u,p,n))
        conn.commit()
        cur.close()
        conn.close()

        return u," hefur verið srkáður <br><a href='/'>Heim</a>"
    else:
        return u," frátekið notendanafn, reyndu aftur <br><a href='/#ny'>Nyskrá</a>"

@route('/doinnskra', method='post')
def leyni():
    u = request.forms.get('user')
    p = request.forms.get('pass')

    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2811992349', passwd='mypassword', db='2811992349_vefv7')
    cur = conn.cursor()

    cur.execute("SELECT count(*) FROM 2811992349_vefv7.users where user=%s and pass=%s",(u,p))
    result = cur.fetchone()
    print(result)
    # er u og til í db?
    if result[0] == 1:
        cur.close()
        conn.close()
        return template('leyni.tpl', u=u)
    else:
        return template('ekkileyni.tpl')

@route('/members')
def member():
    conn = pymysql.connect(host='tsuts.tskoli.is', port=3306, user='2811992349', passwd='mypassword')
    c = conn.cursor()
    c.execute("SELECT nafn FROM 2811992349_vefv7.users")
    result = c.fetchall()
    c.close()
    output = template("member.tpl", rows = result)
    return output

try:
    run(host="0.0.0.0", port=os.environ.get('PORT'))
except:
    run(debug=True)



