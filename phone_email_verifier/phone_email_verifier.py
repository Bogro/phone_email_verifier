#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

import re
import csv

try:
    from .function import function as func
    from .ProcessException import ProcessException
    from .treatment_email import Treatment_email as Email
    from .treatment_phone import Treatement_phone as Phone
except ImportError as IE:
    print(f"ERROR: {IE}")


class phone_email_verifier(object):
    '''
    Object phone_email_verifier 
    '''

    def __init__(self):
        '''
        Constructor 
        '''
        self.email = None
        self.phone = None
        self.country = None
        self.indicative_code = None
        self.specificity = None
        
    def contact_is_list(self, contact):
        '''
        contact_is_list 
        Who can do the check on a contact list
        if contact is not a list an exception is clipped
        '''
        try:
            if type(contact) is not list:
                raise ProcessException('the contact list is not formatted to the program requirement')
        except ProcessException as e:
            raise ProcessException(f"ERROR : {e}")

    def set_phone_list(self, phone, country=None, indicative_code=None, specificity=None):
        '''
        set_phone_list
        Which retrieves the information for the verification of the contacts of the list
        '''

        try:
            success = 0

            if country is not None and indicative_code is not None:
                with open(func.get_dict_code_name(), encoding='utf-8') as country_info:
                    for ligne in country_info:
                        info = ligne.split(',')
                        if country == info[1] and re.match(r'^[\\' + info[2] + ']{2,4}', indicative_code) is not None:
                            success = 0
                            break
                        success +=1
                    
            
            if success > 0:
                raise Exception('The country does not match this code')
                        
            self.contact_is_list(phone)#appel de la method contact_is_list

            self.phone = phone

            self.country = country

            self.indicative_code = self.get_code(country) if country is not None and indicative_code is None else indicative_code
            
            self.specificity = specificity

        except Exception as e:
            print(f'ERROR in program: \n {e}')
        
    
    def get_code(self, country):
        '''
        get_code
        Load to give the code of a selected country
        '''
        with open(func.get_dict_code_name(), encoding='utf-8') as country_info:
            for ligne in country_info:
                info = ligne.split(',')
                if country == info[1]:
                    return info[2]

        raise Exception('the country to select does not have its code identify in our data')

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

    
    def set_phone_in_file(self, file, country=None, indicative_code=None, colum=None):
        '''
        set_phone_in_file 
        Search for numbers in a "TXT" or "CSV" file for verification
        :country, choose country Ex: CI, FR, ...
        :indicative_code, country code not required
        :colum, the column where the number is if the file is a CSV
        '''
        try:
            ext = file.split('.')
            ext = ext[len(ext) - 1:]

            if colum is not None and type(colum) is not int:
                raise Exception('The type is not (int)')

            if ext[0].upper() == 'TXT':
                with open(file, encoding='utf-8') as contact_of_file:
                    self.phone = [phone.split(',')[0] for phone in contact_of_file]
                
                self.country = country
                self.indicative_code = self.get_code(country) if country is not None and indicative_code is None else indicative_code
                
            elif ext[0].upper() == 'CSV':
                self.phone = self.get_contact_of_file(file, colum)
                self.country = country
                self.indicative_code = self.get_code(country) if country is not None and indicative_code is None else indicative_code

        except Exception as e:
            print(f'ERROR: {e}')

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

    def get_contact_of_file(self, file, colum):
        with open(file, newline='') as contact_of_file:
            contact_list = csv.reader(contact_of_file)
            if colum is not None:
                contacts = [cnt[0] for cnt in contact_list]
            else:
                contacts = [cnt[colum] for cnt in contact_list]

        return contacts

    def treatment_selected(self):
        '''
        Methode
        A selection of treatment
        '''
        return True if self.email is not None else False

    def exec(self):
        if self.email is not None or self.phone is not None:
            if self.treatment_selected():
                treatment_email = Email(self.email, self.country)
                treatment_email.generate_email_list()
                return dict(
                    OK=treatment_email.get_contact_success_list(),
                    ERROR=treatment_email.get_contact_error_list()
                )
            else:
                treatment_phone = Phone(self.phone, dict(country=self.country, indicative_code=self.indicative_code, specificity=self.specificity))
                treatment_phone.generate_phone_list()
                return dict(
                    OK=treatment_phone.get_contact_success_list(),
                    ERROR=treatment_phone.get_contact_error_list()
                )
        else:
            return 0