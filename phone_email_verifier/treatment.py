#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

import re

class Treatment(object):
    '''
    Object Treatment
    Object of general treatment on contact (e-mail, phone)
    '''
    def __init__(self, contacts, other=None):
        '''
        Constructor
        '''
        self.error_contacts = list()
        self.new_contacts = list()
        self.contacts = contacts

    def get_contact_success_list(self):
        return self.new_contacts

    def get_contact_error_list(self):
        return self.error_contacts

    def get_contact_old_list(self):
        return self.contacts

    def number_contact_ok(self):
        return len(self.new_contacts)

    def number_contact_no_ok(self):
        return len(self.error_contacts)
        