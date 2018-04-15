from __future__ import unicode_literals
from __future__ import print_function
from flask import Flask, render_template, flash, redirect, url_for, request, session
from flaskext.mysql import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators


app = Flask(__name__)


#Config MYSQL
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'doctorinfo'
app.config['MYSQL_DATABASE_CURSORCLASS'] = 'DictCursor'
mysql.init_app(app)



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/instruction')
def instruction():
    return render_template('instruction.html')

#@app.route('/doctors')
#def doctor():
#    return render_template('doctors.html', doctors = doc)

class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    doc_id = StringField('Doc_id', [validators.Length(min=4, max=50)])
    address = StringField('Address', [validators.Length(min=6, max=50)])
    address2 = StringField('Address2', [validators.Length(min=6, max=50)])


@app.route('/cudoc', methods=['GET', 'POST'])
def cudoc():
    cur = mysql.get_db().cursor()

    result = cur.execute("SELECT * FROM docinfo")
    docinfo = cur.fetchall()

    if result > 0:
        return render_template('cudoc.html', docinfo=docinfo)
    else:
        msg = 'No Doctor Information'
        return render_template('cudoc.html', msg=msg)
    cur.close()

#Delete doctor info
@app.route('/delete_docinfo/<string:id>', methods=['POST'])
def delete_docinfo(id):
    #create cursor
    cur = mysql.get_db().cursor()
    cur.execute("DELETE FROM docinfo WHERE docid = %s", [id])
    cur.execute("DELETE FROM avapp WHERE docid = %s", [id])
    cur.execute("DELETE FROM boapp WHERE docid = %s", [id])
    cur.execute("DELETE FROM unavapp WHERE docid = %s", [id])
    mysql.get_db().commit()
    cur.close()

    flash('Doctor Deleted', 'success')
    return redirect(url_for('cudoc'))



@app.route('/input', methods=['GET', 'POST'])
def input():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        doc_id = form.doc_id.data
        doc_id1 = int(doc_id) + 1
        address = form.address.data
        address2 = form.address2.data

        #create cursor
        cur = mysql.get_db().cursor()
        #execute
        cur.execute("INSERT INTO docinfo(name, docid, address, address2) VALUES(%s, %s, %s, %s)", (name, doc_id, address, address2))

        #create availabe appointment
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'MON morning')", (name, doc_id, address, int(doc_id) + 2))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'MON morning')", (name, doc_id, address2, int(doc_id) + 2))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'MON afternoon')", (name, doc_id, address, int(doc_id) + 4))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'MON afternoon')", (name, doc_id, address2, int(doc_id) + 4))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'TUE morning')", (name, doc_id, address, int(doc_id) + 6))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'TUE morning')", (name, doc_id, address2, int(doc_id) + 6))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'TUE afternoon')", (name, doc_id, address, int(doc_id) + 8))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'TUE afternoon')", (name, doc_id, address2, int(doc_id) + 8))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'WED morning')", (name, doc_id, address, int(doc_id) + 10))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'WED morning')", (name, doc_id, address2, int(doc_id) + 10))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'WED afternoon')", (name, doc_id, address, int(doc_id) + 12))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'WED afternoon')", (name, doc_id, address2, int(doc_id) + 12))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'THR morning')", (name, doc_id, address, int(doc_id) + 14))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'THR morning')", (name, doc_id, address2, int(doc_id) + 14))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'THR afternoon')", (name, doc_id, address, int(doc_id) + 16))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'THR afternoon')", (name, doc_id, address2, int(doc_id) + 16))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'FRI morning')", (name, doc_id, address, int(doc_id) + 18))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'FRI morning')", (name, doc_id, address2, int(doc_id) + 18))

        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'FRI afternoon')", (name, doc_id, address, int(doc_id) + 20))
        cur.execute("INSERT INTO avapp(name, docid, address, dateid, date) VALUES(%s, %s, %s, %s, 'FRI afternoon')", (name, doc_id, address2, int(doc_id) + 20))

        #commit to DB
        mysql.get_db().commit()
        cur.close()

        flash('Input successful', 'success')

        redirect(url_for('instruction'))
    return render_template('input.html', form=form)


@app.route('/makeapp', methods=['GET', 'POST'])
def makeapp():
    cur = mysql.get_db().cursor()

    result = cur.execute("SELECT * FROM avapp")
    appinfo = cur.fetchall()

    if result > 0:
        return render_template('makeapp.html', appinfo=appinfo)
    else:
        msg = 'No Available Appointment'
        return render_template('makeapp.html', msg=msg)
    cur.close()

@app.route('/book_app/<string:id>', methods=['POST'])
def book_app(id):
    #create cursor
    cur = mysql.get_db().cursor()
    resultaa = cur.execute("SELECT dateid FROM avapp WHERE id = %s", [id])
    aaaa = cur.fetchall()
    #print ('%s', aaaa[0][1])
    cur.execute("INSERT INTO boapp(name, docid, dateid, date, address) SELECT name, docid, dateid, date, address FROM avapp WHERE id = %s", [id] )
    cur.execute("DELETE FROM avapp WHERE id = %s", [id])
    cur.execute("INSERT INTO unavapp(name, docid, dateid, date, address) SELECT name, docid, dateid, date, address FROM avapp WHERE dateid = '%s'", aaaa[0][0] )
    cur.execute("DELETE FROM avapp WHERE dateid = %s", aaaa[0][0])
    # cur.execute("DELETE FROM avapp WHERE id = %s", [id])
    mysql.get_db().commit()
    cur.close()
    flash('Appointment is made', 'success')
    return redirect(url_for('makeapp'))


@app.route('/curapp', methods=['GET', 'POST'])
def curapp():
    cur = mysql.get_db().cursor()
    result = cur.execute("SELECT * FROM boapp")
    appinfo = cur.fetchall()

    if result > 0:
        return render_template('curapp.html', appinfo=appinfo)
    else:
        msg = 'No Current Appointment'
        return render_template('curapp.html', msg=msg)
    cur.close()


@app.route('/cancel_app/<string:id>', methods=['POST'])
def cancel_app(id):
    #create cursor
    cur = mysql.get_db().cursor()
    resultbb = cur.execute("SELECT dateid FROM boapp WHERE id = %s", [id])
    bbbb = cur.fetchall()
    cur.execute("INSERT INTO avapp(name, docid, dateid, date, address) SELECT name, docid, dateid, date, address FROM boapp WHERE id = %s", [id] )
    cur.execute("DELETE FROM boapp WHERE id = %s", [id])
    cur.execute("INSERT INTO avapp(name, docid, dateid, date, address) SELECT name, docid, dateid, date, address FROM unavapp WHERE dateid = '%s'", bbbb[0][0] )
    cur.execute("DELETE FROM unavapp WHERE dateid = %s", bbbb[0][0])
    mysql.get_db().commit()
    cur.close()
    flash('Appointment is canceled', 'success')
    return redirect(url_for('curapp'))



if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
