from ldap3 import Server, Connection, ALL, NTLM
from account import models as amod

def test_connection(username, password):
    s = Server('www.familymusic.me', get_info=ALL)
    c = Connection(s, user=("FAMILYMUSIC\\" + str(username)), password=password, authentication=NTLM)
    return c.bind()

def createAdAccount(username, password):
    s = Server('www.familymusic.me', get_info=ALL)
    c = Connection(s, user=("FAMILYMUSIC\\" + str(username)), password=password, authentication=NTLM)
    c.bind()
    c.search('dc=familymusic,dc=me,dc=local', '(sAMAccountName=' + str(username) + ')', attributes=['mail','sn','givenName'])
    user = amod.User()
    user.email = c.entries[0].mail
    user.username = c.entries[0].givenName
    user.first_name = c.entries[0].givenName
    user.last_name = c.entries[0].sn
    user.set_password(password)
    user.is_superuser = True
    user.save()
    return user
    
