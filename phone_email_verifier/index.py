#! -*- Encoding: utf-8 -*-

from .ProcessException import ProcessException
from .treatment_email import Treatment_email as Email
from .treatment_phone import Treatement_phone as Phone


class Index(object):
    '''
    Object index 
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
        Methode 
        Qui permet de faire la verification sur une list de contact
        is contact n'est pas une list 
        Une exception est enclancher
        '''
        try:
            if type(contact) is not list:
                raise ProcessException('the contact list is not formatted to the program requirement')
        except ProcessException as e:
            raise ProcessException(f"ERROR : {e}")

    def set_phone_list(self, phone, country=None, indicative_code=None, specificity=None):
        '''
        Methode
        Qui permet de recupérer les information pour la 
        verification des contacts de la list
        '''
        try:
            self.contact_is_list(phone)#appel de la method contact_is_list
            self.phone = phone
            self.country = country
            self.indicative_code = indicative_code
            self.specificity = specificity
        except Exception as e:
            print(f'ERROR in program: \n {e}')
        
    
    def set_email_list(self, email, country=None):
        '''
        Methode
        Qui permet de recupérer les information pour la 
        verification des contacts de la list
        '''
        try:
            self.contact_is_list(email)#appel de la method contact_is_list
            self.email = email
            self.country = country if country is not None else None 
        except Exception as e:
            print(f'ERROR in program: \n {e}')
        

    def treatment_selected(self):
        '''
        Methode
        Qui permet de faire une selection de traitement
        '''
        return True if self.email is not None else False

    def exec(self):
        if self.email is not None or self.phone is not None:
            if self.treatment_selected():
                treatment_email = Email(self.email, self.country)
                treatment_email.generate_email_list()
                return dict(
                    OK=treatment_email.get_contact_success_list(),
                    ERROR=treatment_email.get_contact_error_list(),
                    OLD=treatment_email.get_contact_old_list()
                )
            else:
                treatment_phone = Phone(self.phone, dict(country=self.country, indicative_code=self.indicative_code, specificity=self.specificity))
                treatment_phone.generate_phone_list()
                return dict(
                    OK=treatment_phone.get_contact_success_list(),
                    ERROR=treatment_phone.get_contact_error_list(),
                    ORL=treatment_phone.get_contact_old_list()
                )
        else:
            return 0