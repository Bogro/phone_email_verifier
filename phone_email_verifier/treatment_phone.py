#! -*- Encoding: utf-8 -*-

import re
from .treatment import Treatment

class Treatement_phone(Treatment):
    
    def __init__(self, contacts, other=None):
        Treatment.__init__(self, contacts)
        self.other = other
        self.regex = re.compile(r"[\+\d]{6}")
    
    def generate_phone_list(self):
        old_contacts = self.contacts[:]

        for contact in old_contacts:
            contact = re.sub(r"[/ _-]", "", contact)

            if self.filter_phone(contact):
                self.new_contacts.append(contact)
            else:
                self.error_contacts.append(contact)

    def filter_phone(self, contact):
        if self.regex.match(contact) is not None:
            
            country_code = None
            regex = "[\+\d]{6}"

            if self.other['country'] is None:
                with open('phone_email_verifier/src/code.txt', encoding='utf-8') as country_info:
                    for ligne in country_info:
                        if self.other['country'].upper() in ligne:
                            country_code = ligne.split(',')[2]

            if self.other['indicative_code'] is not None:
                pass

            return True

        else:
            return False