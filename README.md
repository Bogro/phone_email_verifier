# PHONE & EMAIL Verifier

## Description
 Validation of the email or international or local telephone number

## Install
   -------

   pip install phone_email_verifier


## Usage
   -----

    >>> from phone_email_verifier import 
    >>> phone_email_verifier

    >>> filter = phone_email_verifier()

    

   ### E-mail

appartie d'une variable 

    >>> filter.set_email_list()

    >>> filter.exec()

   ### Phone

appartie d'une variable 
    
    >>> filter.set_phone_list()

    # appartie d'un fichier
    >>> filter.set_phone_in_file()

    >>> filter.exec()