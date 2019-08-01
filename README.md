# PHONE & EMAIL Verifier

## Description
 Validation of the email and international or local telephone number.

## Install

If you install with

    pip install phone_email_verifier


1 : Download here https://github.com/Bogro/phone_email_verifier/blob/develop/phone_email_verifier/code.txt and drop it at the root of your project.

2 : Add the phone code dictionary path in the .env of your project.
    
    #.env
    DICT_CODE="dict_name.txt"

Note: This file is important for checking phone numbers


For direct downloads on github you do not need to follow the process above

## Usage

   ### E-mail


    from phone_email_verifier.email_verifier import email_verifier as email_v


    email = email_v()

    email_list = ['test@mail.tx', 'demo@mail.test', 'e.mail@mailer.com']

    >>> email.set_email_list(email_list) 

    or

    >>> email.set_email_in_file(file_name)

    >>> email.exec()

    {'OK': ['test@mail.tx', 'e.mail@mailer.com'], 'ERROR': ['demo@mail.test']}

#### Remarque:
It is possible to make a restriction on the country by making:

    >>> email.set_email_list(email, 'FR')

    or

    >>> email.set_email_in_file(file_name, 'FR')

and this will make a filter on any email not ending
    
    .fr

if the file used is a CSV, indicate the column of email

    >>> email.set_email_in_file(file_name, colum=0)

    or

    >>> email.set_email_in_file(file_name, 'FR', 0)

##### Reamarque
    Les types de fichier utilisable sont:
    CSV et TXT
    

   ### Phone


    from phone_email_verifier.phone_verifier import phone_verifier as phone_v

    phone = phone_v()

    phone_list = ['+22547000000', '+225-47-00-00-00', '+225 47 00 00 00 00', '+33 00 25 00 11', '47 02 00 00']


#### simple use

    >>> filter.set_phone_list(phone_list)

    or

    >>> filter.set_phone_in_file(file_name)

    >>> filter.exec()

    {'OK': ['+22547000000', '+22547000000', '+2254700000000', '+3300250011'], 'ERROR': ['47020000']}


#### Advance use

It is possible to make a precision with the name of the country and is identifying code

    >>> filter.set_phone_list(phone_list, 'FR', '+33')

    or

    >>> filter.set_phone_in_file(name_list, 'FR', '+33', colum=0) # colum is column of numbers

    >>> filter.exec()

    {'OK': ['+3300250011'], 'ERROR': ['47020000', '+22547000000', '+22547000000', '+2254700000000']}


It is important to specify the number column when the file is a csv file.


# For code dictionary identify countries

You can add or reduce the list according to your usage.
I advise you to reduce according to your use, to make fast execution

## How to add

To add, go to the line and:

The name of the country, abbreviation of the name, identify code (+33 | 33 | 0033), length of the number without the identified code and the local code, the local code if it exists,

Example:

Country name
--------------
    France

Abbreviation country name
------------------
    FR

Identify code
----------------
    +33|33|0033

Length phone number
-----------------
    8

Note:

If the number can be several lengths, add it in ascending order with " | " as separator

    6|7|8|9

Local code
-------------
s'il existe 

    0

Note: if there are more than one, add with " | " as separator

    0|1|2

if it does not exist the line ends with a

    ','

in the end we have this line

    France,FR,+33|33|0033,8,0,



### Final note

    * The spaces between the values ​​are forbidden
    * The finished line always with a ";