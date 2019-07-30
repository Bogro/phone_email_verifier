#!/usr/bin/env python3
#! -*- Encoding: utf-8 -*-

import os

class function(object):

    @staticmethod
    def get_dict_code_name():
        '''
        Check if the code file exists and return the file name
        '''
        
        try:
            dict_code = "phone_email_verifier/code.txt"

            with open(dict_code): pass

            return dict_code

        except IOError:
            return os.getenv('DICT_CODE')
        else:
            return None