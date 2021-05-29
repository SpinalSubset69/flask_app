class Contact:
    def __init__(self, fullname, phone, email):
        self.fullname = fullname
        self.phone = phone
        self.email = email

    def no_data(self):
        if self.fullname == '' or self.email == '' or self.phone == '':
            return True
        else:
            return False