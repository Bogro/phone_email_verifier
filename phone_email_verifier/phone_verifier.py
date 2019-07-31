#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

import re

try:
    from .treatment_phone import Treatement_phone as Phone
    from .contacts_verifier import contacts_verifier
    from .function import function as func
except ImportError as IE:
    print(f"ERROR: {IE}")

class phone_verifier(contacts_verifier):
    
    def __init__(self):
        contacts_verifier.__init__(self)
        self.phone = None

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

    def exec(self):
        if self.phone is not None:
            treatment_phone = Phone(self.phone, dict(country=self.country, indicative_code=self.indicative_code, specificity=self.specificity))
            treatment_phone.generate_phone_list()
            return dict(
                OK=treatment_phone.get_contact_success_list(),
                ERROR=treatment_phone.get_contact_error_list()
            )
                
        else:
            return 0