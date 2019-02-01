from ldap3 import Server, Connection, ALL, ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES
import os
import csv
import datetime


def main():
    ldap_server = input('LDAP url (eg. example.com): ')
    server = Server(ldap_server, get_info=ALL)
    ldap_user = input('LDAP USER (eg. KAIDO89): ')
    ldap_pass = input('LDAP PASSWORD (eg. KAIDO89_PASSWORD): ')
    forest = input('LDAP FOREST (eg. COMPANY_NAME): ')
    conn = Connection(server, user=forest+"\\"+ldap_user, password=ldap_pass, auto_bind=True)
    search_user = input('SEARCH USER in LDAP (eg. KAIDO89_FRIEND): ')
    search_user_result = conn.search('dc='+str(forest).lower()+',dc=com',
                                     '(&(objectclass=person)(mailNickname=' + search_user + '))',
                                     attributes=[ALL_ATTRIBUTES, ALL_OPERATIONAL_ATTRIBUTES])
    print(search_user_result)
    print(conn.entries)


main()
