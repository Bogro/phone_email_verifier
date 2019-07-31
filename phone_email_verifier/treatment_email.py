#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

import re

try:
    from .treatment import Treatment
except ImportError as IE:
    print(f"ERROR: {IE}")


class Treatment_email(Treatment):
    '''
    Object Treatment_email
    Qui faire le filtre sur les E-mail
    '''

    def __init__(self, contacts, other=None):
        '''
        Constructor
        '''
        Treatment.__init__(self, contacts)
        
        if type(other) is str :
            country = "[\." + other.lower() + "]\Z"
        else:
            country = "([a-zA-z]{2,3})\Z"
        
        self.regex = re.compile(r"^([a-z0-9._-])+@([a-z0-9._-])+" + country)
    
    def generate_email_list(self):
        '''
        Method generate_email_list
        '''

        old_contacts = self.contacts[:]

        for email in old_contacts:
            if self.filter_email(email):

                if email not in self.new_contacts:
                    self.new_contacts.append(email)

            else:
                self.error_contacts.append(email)


    def filter_email(self, contact):
        '''
        Method filter_email
        '''
        return True if self.regex.match(contact) is not None else False