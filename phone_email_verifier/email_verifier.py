#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

try:
    from .contacts_verifier import contacts_verifier
    from .treatment_email import Treatment_email as Email
except ImportError as IE:
    print(f"ERROR: {IE}")

class email_verifier(contacts_verifier):

    def __init__(self):
        contacts_verifier.__init__(self)
        self.email = None


    def set_email_list(self, email, country=None):
        '''
        Methode
        Retrieves information for checking list contacts
        '''
        try:
            self.contact_is_list(email)#appel de la method contact_is_list
            self.email = email
            self.country = country if country is not None else None 
        except Exception as e:
            print(f'ERROR in program: \n {e}')

    def set_email_in_file(self, file, country=None, colum=None):
        '''
        set_email_in_file 
        Search for numbers in a "TXT" or "CSV" file for verification
        :country, choose country Ex: CI, FR, ...
        :colum, the column where the number is if the file is a CSV
        '''
        try:
            ext = file.split('.')
            ext = ext[len(ext) - 1:]

            if colum is not None and type(colum) is not int:
                raise Exception('The type is not (int)')

            if ext[0].upper() == 'TXT':
                with open(file, encoding='utf-8') as contact_of_file:
                    self.email = [email.split(',')[0] for email in contact_of_file]
                
                self.country = country
                
            elif ext[0].upper() == 'CSV':
                self.email = self.get_contact_of_file(file, colum)
                self.country = country

        except Exception as e:
            print(f'ERROR: {e}')

    def exec(self):
        if self.email is not None:
            treatment_email = Email(self.email, self.country)
            treatment_email.generate_email_list()
            return dict(
                OK=treatment_email.get_contact_success_list(),
                ERROR=treatment_email.get_contact_error_list()
            )
        else:
            return 0