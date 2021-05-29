from flask_mysqldb import MySQL
from contact import Contact

class CRUD:    
#  ''' Base Operations with database '''

    def __init__(self, mysql):
      self.mysql = mysql

    def lis_contacts(self):
        try:
            cur = self.mysql.connection.cursor()
            cur.execute('SELECT * FROM contacts')
            return cur.fetchall()
        except:
            print('An error has ocurred on the database')             

    def create_contact(self, contact:Contact):
        try:
            #Cursor se utiliza para saber donde esta la conexion, permite ejecutar las consultas
            cur = self.mysql.connection.cursor()
            cur.execute('insert into contacts (fullname, phone, email) values (%s, %s, %s)',
            (contact.fullname, contact.phone, contact.email))
            cur.connection.commit()
        except: print('An error has ocurred on the database')

    def delete_contact(self, id:str):
        try:
            cur = self.mysql.connection.cursor()
            cur.execute('delete from contacts where id = %s', {id})
            cur.connection.commit()
        except: print('An error has ocurred on the database')

    def get_contact_by_id(self, id:str):
        try:
            cur = self.mysql.connection.cursor()
            cur.execute('select * from contacts where id = %s' , {id})            
            return cur.fetchall()
        except: print('An error has ocurred on the database')

    def edit_contact(self, id:str, contact:Contact):
        try:                   
            cur = self.mysql.connection.cursor()
            cur.execute('UPDATE contacts SET fullname = %s, phone = %s, email = %s WHERE id = %s', (
                contact.fullname, contact.phone, contact.email, id
            ))
            cur.connection.commit()
        except Exception as e: print(e)