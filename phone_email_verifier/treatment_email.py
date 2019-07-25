#! -*- Encoding: utf-8 -*-

import re
from .treatment import Treatment

class Treatment_email(Treatment):

    def __init__(self, contacts, other=None):
        Treatment.__init__(self, contacts, other=other)
        self.regex_email = re.compile(r"^[a-z0-9._-]+@[a-z0-9._-]+\.[a-zA-z]{2,3}\Z")
    
    def generate_email_list(self):

        old_contacts = self.contacts[:]

        for contact in old_contacts:
            if self.filter_email(contact):
                self.new_contacts.append(contact)
            else:
                self.error_contacts.append(contact)


    def filter_email(self, contact):
        return True if self.regex_email.match(contact) is not None else False