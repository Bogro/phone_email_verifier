#! -*- Encoding: utf-8 -*-

from .ProcessException import ProcessException


class Index(object):
    
    def __init__(self, contact, country=None, indicative_code=None, specificity=None):

        try:
            
            if type(contact) is not list:
                raise ProcessException('the contact list is not formatted to the program requirement')

            self.contact = contact 
            self.country = country
            self.indicative_code = indicative_code
            self.specificity = specificity

        except ProcessException as e:
            print(f"ERROR : {e}")
        
    def exec(self):
        pass
