#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

import re

try:
    from .function import function as func
    from .treatment import Treatment
    from .ProcessException import ProcessException
except ImportError as IE:
    print(f"ERROR: {IE}")


class Treatement_phone(Treatment):
    '''
    Object Treatement_phone
    Qui faire le filtre sur les numéros de téléphone
    '''

    def __init__(self, contacts, other=None):
        '''
        Constructor
        '''
        Treatment.__init__(self, contacts)
        self.other = other
        self.regex = re.compile(r'[\+\d]{6,15}\Z')
        self.code = None
        self.len_phone = None
    
    def generate_phone_list(self):
        old_contacts = [re.sub(r"[@#.!?/ _-]", "", phone) for phone in self.contacts[:]]
        for contact in old_contacts:
            phone = self.filter_phone(contact)
            if phone is not False:
                number = self.add_code(phone)
                if number not in self.new_contacts:
                    self.new_contacts.append(number)

            else:
                self.error_contacts.append(contact)

    def filter_by_all_country(self, contact):
        with open(func.get_dict_code_name(), encoding='utf-8') as country_info:
            for ligne in country_info:

                lg = ligne.split(',')[:4]

                regex = f"(^\\{lg[2]})"
                
                if re.match(regex, contact) is not None:
                    
                    try:
                        
                        self.code = lg[2]

                        regex = f"{regex}(\d{ {int(lg[3])} }\Z)"

                        r = re.match(regex, contact)
                        
                        if r is not None:
                            return r.groups()

                    except Exception as E:
                        return False
            return False

    def filter_by_code(self, contact, country, code=None):
        with open(func.get_dict_code_name(), encoding='utf-8') as country_info:
            for ligne in country_info:
                if code in ligne:
                    
                    try:
                        
                        lg = ligne.split(',')[:4]
                        
                        self.code = lg[2]

                        if '\n' in lg:
                            regex = f'^(\\{lg[2]})(\d{ {6,11} }\Z)'
                            r = re.match(regex, contact)
                            if r is not None:
                                return r.groups()

                        
                        if '|' not in lg[3]:
                            l = f'(\d{ {int(lg[3])} }\Z)'
                        else:
                            l = lg[3].split('|')
                            l = f'(\d{ {int(l[:1][0]),int(l[-1:][0])} }\Z)'.replace(" ", "")
                            

                        regex = f'^(\\{lg[2]})' + l
                        
                        r = re.match(regex, contact)

                        if r is not None:
                            return r.groups()

                        lg = ligne.split(',')[:5]
                        
                        if '\n' in lg:
                            regex = l
                            r = re.match(regex, contact)
                            if r is not None:
                                return r.groups()

                        if '|' not in lg[4]:

                            regex = f'^({lg[4]})' + l
                            r = re.match(regex, contact)
                            if r is not None:
                                return r.groups()
                            
                        else:

                            for p in lg[4].split('|'):
                                regex = f'^({lg[4]})' + l
                                r = re.match(regex, contact)
                                if r is not None:
                                    return r.groups() 
                        
                    except Exception as E:
                        print(f'ERROR: {E}')
                        return False

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
            
    def add_code(self, phone):

        if '|' in self.code:
            self.code = self.code.split('|')[0]

        if len(phone) > 1:
            if phone[0] == self.code:
                return phone[0] + phone[1]
            else:
                return self.code + phone[1]
        else:
            return self.code + phone[0]

        