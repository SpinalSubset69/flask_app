#Imports 
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from crud import CRUD
from contact import Contact

#Configuring server
app = Flask(__name__)

#Config Session, data saved on app memory
app.secret_key = 'mysecretkey'

#Configuring MYSQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSwORD'] = 'Resumiendo69%'
app.config['MYSQL_DB'] = 'flaskontact'
#Setting config of database to server
mysql = MySQL(app)

#Create Crud instance
crud = CRUD(mysql)

#Routes Section

@app.route('/')
def index():
    data = crud.lis_contacts()
    return render_template('index.html', contacts=data)

@app.route('/create_contact', methods=['POST'])
def create_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email'] 
        print(f'{fullname}, {phone}')        
        contact = Contact(fullname,phone,email)                
        if contact.no_data():
            print('Missing Data')
        crud.create_contact(contact)
        flash('Contact added successfully')
        return redirect(url_for('index'))

@app.route('/edit/<string:id>')
def edit(id):
    data = crud.get_contact_by_id(id)            
    return render_template('edit.html', data = data)

@app.route('/edit_contact/<string:id>', methods=['POST'])
def edit_contact(id):        
    if request.method == 'POST':        
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        contact = Contact(fullname, phone, email)                                                   
        crud.edit_contact(id, contact)
        flash('Contact update succesfully')
        return redirect(url_for('index'))


#Así se reciben los parámetros
@app.route('/delete/<string:id>')
def delete_contact(id):
    crud.delete_contact(id)
    flash('Contact deleted succesfully')
    return redirect(url_for('index'))

#End Routes Section

#Verifying we are working on main archive
if __name__ == '__main__':
    app.run(port=3000, debug=True)