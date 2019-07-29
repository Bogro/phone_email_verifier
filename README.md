# PHONE & EMAIL Verifier

## Description
 Validation of the email or international or local telephone number

## Install
   -------

    pip install phone_email_verifier


## Usage
   -----

    >>> from phone_email_verifier import phone_email_verifier

    >>> filter = phone_email_verifier()

    

   ### E-mail

E-mail list

    email = ['test@mail.tx', 'demo@mail.test', 'e.mail@mailer.com']

    >>> filter.set_email_list(email, )

    >>> filter.exec()

    {'OK': ['test@mail.tx', 'e.mail@mailer.com'], 'ERROR': ['demo@mail.test']}

   ### Phone

Number phone list 
    
    #simple use

    phone = ['+22547000000', '+225-47-00-00-00', '+225 47 00 00 00 00', '+33 00 25 00 11 00', '47 02 00 00']

    >>> filter.set_phone_list(phone)

    {'OK': ['+22547000000', '+22547000000', '+2254700000000', '+330025001100'], 'ERROR': ['47020000']}



appartie d'un fichier

    #simple use of a contact list

    name_list = list_phone.csv

    >>> filter.set_phone_in_file(name_list, colum=0) # colum is column of numbers

    >>> filter.exec()

    {'OK': ['+22547000000', '22547000010'], 'ERROR': ['030020585', '4578', '33024558452', '55552222', '658945898']}


It is important to specify the number column when the file is a csv file.