#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

import re
import csv

try:
    from .function import function as func
    from .ProcessException import ProcessException
except ImportError as IE:
    print(f"ERROR: {IE}")


class contacts_verifier(object):
    '''
    Object phone_email_verifier 
    '''

    def __init__(self):
        '''
        Constructor 
        '''
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

    
    def get_contact_of_file(self, file, colum):
        with open(file, newline='') as contact_of_file:
            contact_list = csv.reader(contact_of_file)
            if colum is None:
                contacts = [cnt[0] for cnt in contact_list]
            else:
                contacts = [cnt[colum] for cnt in contact_list]

        return contacts


    