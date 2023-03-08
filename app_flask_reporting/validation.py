
"""
     fonction de validation apres authentification 
     sur le protail de notre mini application
"""

import re

def validemail(email):
    """ retourne true ou false selon le format de l'email"""

    #validation email du format de l'email
    email_split =  re.split('\.|@', email)

    if len(email_split) > 2:
         #format correct
         return True
    else:
         return False
    
def valipwd(pwd_on_form):
     
     """ validation du  mot de passe """
     if pwd_on_form == "1234":
          return True
     else:
          return False
     

def validform(email, pwd_on_form):
     if validemail(email) and valipwd(pwd_on_form):
          return True
     else:
          return False