# PHONE & EMAIL Verifier

## Description
 Validation of the email or international or local telephone number.

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

E-mail list

    from phone_email_verifier.email_verifier import email_verifier as email_v


    email = email_v()

    email_list = ['test@mail.tx', 'demo@mail.test', 'e.mail@mailer.com']

    >>> email.set_email_list(email_list) 

    or

    >>> email.set_email_in_file(file_name)

    >>> email.exec()

    {'OK': ['test@mail.tx', 'e.mail@mailer.com'], 'ERROR': ['demo@mail.test']}

#### Remarque:
Il est possible de faire une restricrion sur le pays en faisant:

    >>> email.set_email_list(email, 'FR')

    or

    >>> email.set_email_in_file(file_name, 'FR')

et célà ferra un filtre sur tous email se terminant pas 
    
    .fr

si le fichier utiliser est un CSV indique la colonne ou trouver le email

    >>> email.set_email_in_file(file_name, colum=0)

    or

    >>> email.set_email_in_file(file_name, 'FR', 0)

##### Reamarque
    Les types de fichier utilisable sont:
    CSV et TXT
    

   ### Phone

Number phone list 
    

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

Il est possible d'apporté une précision avec le nom du pays et sont code indentifiant

    >>> filter.set_phone_list(phone_list, 'FR', '+33')

    or

    >>> filter.set_phone_in_file(name_list, 'FR', '+33', colum=0) # colum is column of numbers

    >>> filter.exec()

    {'OK': ['+3300250011'], 'ERROR': ['47020000', '+22547000000', '+22547000000', '+2254700000000']}


It is important to specify the number column when the file is a csv file.


# Pour le dictionnaire de code identifient des pays

Vous pourvez ajouté ou reduire la liste en function de votre utilisation.
Je vous conseille de reduire en fonction de votre utilisation, pour rendre rapide l'execution

## Comment ajouter

Pour ajouter, aller a la ligne et

le nom du pays,abreviation du nom,code identifient (+225|225|0225), longuer du numéro sans le code identifient et le code local, le code local s'il existe,

Exemple:
Nom du pays
--------------
    France

Abreviation du nom
------------------
    FR

Code identifient
----------------
    +33|33|0033

Longueur du numéro
-----------------
    8

Remarque: si le numéro peux avoir plusieurs longueur, ajouter le du plus petit au plus grand ave '|' comme separateur

    6|7|8|9

Le code local
-------------
s'il existe 

    0

Remarque: s'il en a plusieurs, ajouter avec '|' comme separateur

    0|1|2

s'il existe pas la ligne se termie pas une 

    ','

au final on a cette ligne 

    France,FR,+33|33|0033,8,0,



### Remarque final

    *Les espaces entre les valeur sont interdite
    *La ligne finir toujour avec un ','