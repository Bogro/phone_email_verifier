#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

import re
from .treatment import Treatment
from .ProcessException import ProcessException

class Treatement_phone(Treatment):
    '''
    Object Treatement_phone
    Qui faire le filtre sur les numéro de téléphone
    '''

    def __init__(self, contacts, other=None):
        '''
        Constructor
        '''
        Treatment.__init__(self, contacts)
        self.other = other
        self.regex = re.compile(r'[\+\d]{6,15}\Z')
    
    def generate_phone_list(self):
        old_contacts = [re.sub(r"[/ _-]", "", phone) for phone in self.contacts[:]]
        for contact in old_contacts:
            if self.filter_phone(contact):
                self.new_contacts.append(contact)
            else:
                self.error_contacts.append(contact)

    def filter_by_all_country(self, contact):
        with open('phone_email_verifier/code.txt', encoding='utf-8') as country_info:
            for ligne in country_info:
                regex = f"(^\\{ligne.split(',')[2]})"
                reg = re.compile(regex)
                if reg.match(contact) is not None:
                    return True
            return False

    def filter_by_code(self, contact, country, code=None):

        if code is not None:
            regex = f'^(\\{code})'
            if re.match(regex, contact) is not None:
                return True
        else:
            with open('phone_email_verifier/code.txt', encoding='utf-8') as country_info:
                for ligne in country_info:
                    if country.upper() in ligne:
                        if re.match(r'^(\\' + ligne.split(',')[2] + ')', contact) is not None:
                            return True
                return False

    def filter_phone(self, contact):

        try:
            if self.regex.match(contact) is not None:
                if self.other['country'] is None:
                    return self.filter_by_all_country(contact)
                else:
                    return self.filter_by_code(contact, self.other['country'], self.other['indicative_code'])
            else:
                return False
                
        except ProcessException as e:
            print(f'ERROR: {e}')
            return False
            

        