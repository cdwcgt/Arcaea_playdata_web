"""
The flask application package.
"""
import random
import string
from flask import Flask,g
from flask import render_template,request,flash
import time
import sqlite3
import os.path


app = Flask(__name__)


key = random.sample(string.ascii_letters + string.digits, 8)
app.secret_key=str(key)

def query_db(db_path,query, args=(),one=False):
    g.db = sqlite3.connect(db_path)
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    g.db.close()
    return (rv[0] if rv else None) if one else rv




@app.route('/arcquery/<user_id>')
def queryhist_page(user_id):
    if str.isdigit(user_id) == False:
        return('非法id')
    db_p='C:\\Users\\Administrator\\arc\\qu_history\\userplayed.db'

    user_h = query_db(db_p,'select * from \''+ user_id +'\' order by time DESC')
    user_info = query_db(db_p,'select * from userinfo where id glob \''+ user_id +'\'')
    print(user_info)
    if os.path.isfile('C:\\Users\\Administrator\\Desktop\\arc\\qu_history\\no_query\\' + user_id):
        return('用户 '+ user_id +' 已设置禁止被查询。若非您本人设置,请在群内发送`#arc web refute`')
    return render_template('userhist.html',user_info=user_info,user_h=user_h)


 
#if __name__ == '__main__':
#    manager.run('127.0.0.1', 11451) 
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0",port=1234)

#import FlaskWebProject1.views_my
