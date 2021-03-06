# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
com = {
    'extend' : None,
    'domain_name': [ r'Domain Name: \s?(.+)', '' ],
    'registrar': [ r'Registrar: \s?(.+)', '' ],
    'registrant': [ r'Registrant Name: \s*(.+)', '' ],
    'creation_date': [ r'Creation Date: \s?(.+)', '' ],
    'expiration_date': [ r'Expiration Date: \s?(.+)', '' ],
    'updated_date': [ r'Updated Date: \s?(.+)', '' ],
    'name_servers': [ r'Name Server: \s*(.+)\s*', '' ],
    'status': [ r'Status: \s?(.+)', '' ],
    'emails': [ r'[\w.-]+@[\w.-]+\.[\w]{2,4}', '' ],
}

net = {
    'extend' : 'com',
}

org = {
    'extend' : 'com',
    'creation_date': [ r'\nCreated On: \s?(.+)', '' ],
    'updated_date': [ r'\nLast Updated On: \s?(.+)', '' ],
    'expiration_date': [ r'Registry Expiry Date: \s*(.+)', '' ],
    'name_servers': [ r'Name Server: \s?(.+)\s*', '' ],
}

uk = {
    'extend' : 'com',
    'registrant': [ r'Registrant: \n\s*(.+)', '' ],
    'creation_date': [ r'Registered on: \s*(.+)', '' ],
    'expiration_date': [ r'Expiry Date: \s*(.+)', '' ],
    'updated_date': [ r'Last updated: \s*(.+)', '' ],
    'name_servers': [ r'Name Servers: \s*(.+)\s*', '' ],
    'status': [ r'Registration status: \n\s*(.+)', '' ],
}

pl = {
    'extend' : 'uk',
    'creation_date': [ r'\ncreated: \s*(.+)\n', '' ],
    'updated_date': [ r'\nlast modified: \s*(.+)\n', '' ],
    'name_servers': [ r'\nnameservers: \s*(.+)\n\s*(.+)\n', '' ],
    'status': [ r'\nStatus: \n\s*(.+)', '' ],
}

ru = {
    'extend' : 'com',
    'domain_name': [ r'\ndomain: \s*(.+)', '' ],
    'creation_date': [ r'\ncreated: \s*(.+)', '' ],
    'expiration_date': [ r'\npaid-till: \s*(.+)', '' ],
    'name_servers': [ r'\nnserver: \s*(.+)', '' ],
    'status': [ r'\nstate: \s*(.+)', '' ],
}

lv = {
    'extend' : 'ru',
    'creation_date': [ r'Registered: \s*(.+)\n', '' ],
    'updated_date': [ r'Changed: \s*(.+)\n', '' ],
    'status': [ r'Status: \s?(.+)', '' ],
}

jp = {
    'domain_name': [ r'\[Domain Name\]\s?(.+)', '' ],
    'registrar': [ None, '' ],
    'registrant': [ r'\[Registrant\]\s?(.+)', '' ],
    'creation_date': [ r'\[Created on\]\s?(.+)', '' ],
    'expiration_date': [ r'\[Expires on\]\s?(.+)', '' ],
    'updated_date': [ r'\[Last Updated\]\s?(.+)', '' ],
    'name_servers': [ r'\[Name Server\]\s*(.+)', '' ],
    'status': [ r'\[Status\]\s?(.+)', '' ],
    'emails': [ r'[\w.-]+@[\w.-]+\.[\w]{2,4}', '' ],
}

co_jp = {
    'extend' : 'jp',
    'creation_date': [ r'\[Registered Date\]\s?(.+)', '' ],
    'expiration_date': [ r'\[State\].+\((.+)\)', '' ],
    'updated_date': [ r'\[Last Update\]\s?(.+)', '' ],
}

de = {
    'extend' : 'com',
    'domain_name': [ r'\ndomain: \s*(.+)', '' ],
    'updated_date': [ r'\nChanged: \s?(.+)', '' ],
    'name_servers': [ r'Nserver: \s*(.+)', '' ],
    'registrar': [ r'Name: \s*(.+)', '' ],
}

at = {
    'extend' : 'com',
    'domain_name': [ r'domain: \s?(.+)', '' ],
    'updated_date': [ r'changed: \s?(.+)', '' ],
    'name_servers': [ r'nserver: \s*(.+)', '' ],
}

eu = {
    'extend' : 'com',
    'domain_name': [ r'\ndomain: \s*(.+)', '' ],
    'registrar': [ r'Name: \s?(.+)', '' ],
}

biz = {
    'extend' : 'com',
    'registrar': [ r'Registrar: \s?(.+)', '' ],
    'registrant': [ r'Registrant Organization: \s?(.+)', '' ],
    'creation_date': [ r'Domain Registration Date: \s?(.+)', '' ],
    'expiration_date': [ r'Domain Expiration Date: \s?(.+)', '' ],
    'updated_date': [ r'Domain Last Updated Date: \s?(.+)', '' ],
    'status': [ None, '' ],
}

info = {
    'extend' : 'biz',
    'expiration_date': [ r'Registry Expiry Date: \s*(.+)', '' ],
    'creation_date': [ r'Created On: \s?(.+)', '' ],
    'updated_date': [ r'Last Updated On: \s?(.+)', '' ],
    'registrar': [ r'Registrar: \s?(.+)', '' ],
    'status': [ r'Status: \s?(.+)', '' ],
}

name = {
    'extend' : 'com',
    'status': [ r'Domain Status: \s?(.+)', '' ],
}

us = {
    'extend' : 'name',
    'expiration_date': [ r'Registry Expiry Date: \s*(.+)', '' ],
}

co = {
    'extend' : 'biz',
    'status': [ r'Status: \s?(.+)', '' ],
}

me = {
    'extend' : 'biz',
    'creation_date': [ r'Domain Create Date: \s?(.+)', '' ],
    'expiration_date': [ r'Domain Expiration Date: \s?(.+)', '' ],
    'updated_date': [ r'Domain Last Updated Date: \s?(.+)', '' ],
    'name_servers': [ r'Nameservers: \s?(.+)', '' ],
    'status': [ r'Domain Status: \s?(.+)', '' ],
}

be = {
    'extend' : 'pl',
    'domain_name': [ r'\nDomain: \s*(.+)', '' ],
    'registrar': [ r'Registrar Technical Contacts: \s*\n\s*Name.*\n\sOrganisation: \s*(.+)', '' ],
    'creation_date': [ r'Registered: \s*(.+)\n', '' ],
    'registrant': [ r'Registrant: \s*\n\s*(.+)', '' ],
    'status': [ r'Status: \s?(.+)', '' ],
}

nz = {
    'extend' : None,
    'domain_name': [ r'domain_name: \s?(.+)', '' ],
    'registrar': [ r'registrar_name: \s?(.+)', '' ],
    'registrant': [ r'registrant_contact_name: \s?(.+)', '' ],
    'creation_date': [ r'domain_dateregistered: \s?(.+)', '' ],
    'expiration_date': [ r'domain_datebilleduntil: \s?(.+)', '' ],
    'updated_date': [ r'domain_datelastmodified: \s?(.+)', '' ],
    'name_servers': [ r'ns_name_[0-9]{2}: \s?(.+)', '' ],
    'status': [ r'query_status: \s?(.+)', '' ],
    'emails': [ r'[\w.-]+@[\w.-]+\.[\w]{2,4}', '' ],
}

cz = {
    'extend' : 'com',
    'domain_name': [ r'Domain: \s?(.+)', '' ],
    'registrar': [ r'registrar: \s?(.+)', '' ],
    'registrant': [ r'registrant: \s?(.+)', '' ],
    'creation_date': [ r'registered: \s?(.+)', '' ],
    'expiration_date': [ r'expire: \s?(.+)', '' ],
    'updated_date': [ r'changed: \s?(.+)', '' ],
    'name_servers': [ r'nserver: \s*(.+) ', '' ],
}

it = {
    'extend' : 'com',
    'domain_name': [ r'Domain: \s?(.+)', '' ],
    'registrar': [ r'Registrar: \s*Organization: \s*(.+)', '' ],
    'registrant': [ r'Registrant: \s?Name: \s?(.+)', '' ],
    'creation_date': [ r'Created: \s?(.+)', '' ],
    'expiration_date': [ r'Expire Date: \s?(.+)', '' ],
    'updated_date': [ r'Last Update: \s?(.+)', '' ],
    'name_servers': [ r'Nameservers: \s?(.+)\s?(.+)\s?(.+)\s?(.+)', '' ],
    'status': [ r'Status: \s?(.+)', '' ],
}

fr = {
    'extend' : 'com',
    'domain_name': [ r'domain: \s?(.+)', '' ],
    'registrar': [ r'registrar: \s*(.+)', '' ],
    'registrant': [ r'contact: \s*(.+)', '' ],
    'creation_date': [ r'created: \s?(.+)', '' ],
    'expiration_date': [ r'Expiry Date: \s*(.+)', '' ],
    'updated_date': [ r'last-update: \s?(.+)', '' ],
    'name_servers': [ r'nserver: \s*(.+)', '' ],
    'status': [ r'status: \s?(.+)', '' ],
}

re = {
    'extend' : 'fr',
    'expiration_date': [ r'Expiry Date: \s?(.+)', '' ],
}

yt = {
    'extend' : 're',
}

io = {
    'registrar': [ r'Registrar:\s+(.+)\r', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)\r', '' ],
    'creation_date': [ r'Creation Date:\s+(.+)\r', '' ],
    'updated_date': [ r'Updated Date:\s+([0-9\-:TZ]+)\r\n', '' ],
    'expiration_date': [ r'Registry Expiry Date:\s+(.+)\r', '' ],
    'registrant': [ r'Registrant Name:\s+(.+)\r*', 'Champ_absent_du_registre' ],
    'name_servers': [ r'Name Server:\s+(.+)\r+', '' ],
}

pw = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Creation Date:\s+(.+)', '' ],
    'updated_date': [ r'Updated Date:\s+(.+)', '' ],
    'expiration_date': [ r'Registry Expiry Date:\s+(.+)', '' ],
    'registrant': [ r'Registrant Name:\s+(.+)', '' ],
    'name_servers': [ r'Name Server:\s+(.+)', '' ],
}

com_br = {
    'registrar': [ r'owner:\s+(.+)', '' ],
    'domain_name': [ r'domain:\s+(.+)', '' ],
    'creation_date': [ r'created:\s+(.+)\s+#.*', '' ],
    'updated_date': [ r'changed:\s+(.*)$', '' ],
    'expiration_date': [ r'expires:\s+(.+)', '' ],
    'registrant': [ r'owner:\s+(.+)', '' ],
    'name_servers': [ r'nserver:\s+(.+)', '' ],
}

ae = {
    'registrar': [ r'Registrar Name:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ None, '1970-01-01T00:00:01' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ r'Registrant Contact Name:\s+(.+)', '' ],
    'name_servers': [ r'Name Server:\s+(.+)', '' ],
}

rs = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain name:\s+(.+)', '' ],
    'creation_date': [ r'Registration Date:\s+(.+)', '' ],
    'updated_date': [ r'Modification Date:\s+(.+)', '' ],
    'expiration_date': [ r'Expiration Date:\s+(.+)', '' ],
    'registrant': [ r'Registrant:\s+(.+)', '' ],
    'name_servers': [ r'DNS:\s+(.+) - [0-9.]+', '' ],
}

bg = {
    'registrar': [ None, 'Champ_absent_du_registre' ],
    'domain_name': [ r'DOMAIN NAME:\s+(.+)', '' ],
    'creation_date': [ None, '1970-01-01T00:00:01' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ r'REGISTRANT:\n(.+)', '' ],
    'name_servers': [ None, 'Champ_impossible_à_identifier_précisément' ],
}

ch = {
    'registrar': [ r'Registrar:\n(.+)', '' ],
    'domain_name': [ r'Domain name:\n(.+)', '' ],
    'creation_date': [ r'First registration date:\n(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ r'Holder of domain name:\n(.+)', '' ],
    'name_servers': [ r'(.+)\s+\[[0-9\.]+\]', '' ],
}

dk = {
    'registrar': [ None, 'Champ_absent_du_registre' ],
    'domain_name': [ r'Domain:\s+(.+)', '' ],
    'creation_date': [ r'Registered:\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ r'Expires:\s+(.+)', '' ],
    'registrant': [ None, 'Champ_impossible_à_identifier_précisément' ],
    'name_servers': [ r'Hostname:\s+(.+)', '' ],
}

fi = {
    'registrar': [ r'registrar\.+:\s+(.+)', '' ],
    'domain_name': [ r'domain\.+:\s+(.+)', '' ],
    'creation_date': [ r'created\.+:\s+(.+)', '' ],
    'updated_date': [ r'modified\.+:\s+(.*)$', '' ],
    'expiration_date': [ r'expires\.+:\s+(.+)', '' ],
    'registrant': [ r'name\.+:\s+(.+)', '' ],
    'name_servers': [ r'nserver\.+:\s+(.+)', '' ],
}

hr = {
    'registrar': [ None, 'Champ_absent_du_registre' ],
    'domain_name': [ r'domain:\s+(.+)', '' ],
    'creation_date': [ None, '1970-01-01T00:00:01' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ r'expires:\s+(.+)', '' ],
    'registrant': [ r'descr:\s+(.+)', '' ],
    'name_servers': [ None, 'Champ_absent_du_registre' ],
}

hu = {
    'registrar': [ None, 'Champ_absent_du_registre' ],
    'domain_name': [ r'domain:\s+(.+)', '' ],
    'creation_date': [ r'record created:\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ None, 'Champ_absent_du_registre' ],
    'name_servers': [ None, 'Champ_absent_du_registre' ],
}

lu = {
    'registrar': [ r'registrar-name:\s+(.+)', '' ],
    'domain_name': [ r'domainname:\s+(.+)', '' ],
    'creation_date': [ r'registered:\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ r'org-name:\s+(.+)', '' ],
    'name_servers': [ r'nserver:\s+(.+)', '' ],
}

no = {
    'registrar': [ r'Registrar Handle\.+:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name\.+:\s+(.+)', '' ],
    'creation_date': [ r'Created:\s+(.+)', '' ],
    'updated_date': [ r'Last updated:\s+(.+)', '' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ r'Legal-c Handle\.+:\s+(.+)', '' ],
    'name_servers': [ r'Name Server Handle\.+:\s+(.+)', '' ],
}

si = {
    'registrar': [ r'registrar:\s+(.+)', '' ],
    'domain_name': [ r'domain:\s+(.+)', '' ],
    'creation_date': [ r'created:\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ r'expire:\s+(.+)', '' ],
    'registrant': [ r'registrant:\s+(.+)', '' ],
    'name_servers': [ r'nameserver:\s+(.+)', '' ],
}

sk = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain:\s+(.+)', '' ],
    'creation_date': [ r'Created:\s+(.+)', '' ],
    'updated_date': [ r'Updated:\s+(.*)$', '' ],
    'expiration_date': [ r'Valid Until:\s+(.+)', '' ],
    'registrant': [ r'Registrant:\s+(.+)', '' ],
    'name_servers': [ r'Nameserver:\s+(.+)', '' ],
}

ro = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Registered On:\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ None, 'Champ_absent_du_registre' ],
    'name_servers': [ r'Nameserver:\s+(.+)', '' ],
}

ee = {
    'registrar': [ r'Registrar:\nname:\s+(.+)', '' ],
    'domain_name': [ r'Domain:\s*\nname:\s+(.+)', '' ],
    'creation_date': [ r'registered:\s+(.+)\s+\+.*', '' ],
    'updated_date': [ r'changed:\s+(.*)\s+\+.*', '' ],
    'expiration_date': [ r'expire:\s+(.+)', '' ],
    'registrant': [ r'Registrant:\nname:\s+(.+)', '' ],
    'name_servers': [ r'nserver:\s+(.+)', '' ],
}

lt = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain:\s+(.+)', '' ],
    'creation_date': [ r'Registered:\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ r'Expires:\s+(.+)', '' ],
    'registrant': [ None, 'Champ_absent_du_registre' ],
    'name_servers': [ r'Nameserver:\s+(.+)', '' ],
}

nl = {
    'registrar': [ r'Registrar:\s*\n\s+(.+)', '' ],
    'domain_name': [ r'Domain name:\s+(.+)', '' ],
    'creation_date': [ None, '1970-01-01T00:00:01' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ None, 'Champ_absent_du_registre' ],
    'name_servers': [ None, 'Champ_impossible_à_identifier_précisément' ],
}

li = {
    'registrar': [ r'Registrar:\n(.+)', '' ],
    'domain_name': [ r'Domain name:\n(.+)', '' ],
    'creation_date': [ r'First registration date:\n(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ r'Holder of domain name:\n(.+)', '' ],
    'name_servers': [ None, 'Champ_impossible_à_identifier_précisément' ],
}

es = {
    'registrar': [ None, 'Champ_absent_du_registre' ],
    'domain_name': [ None, 'Champ_absent_du_registre' ],
    'creation_date': [ None, '1970-01-01T00:00:01' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ None, '1970-01-01T00:00:01' ],
    'registrant': [ None, 'Champ_absent_du_registre' ],
    'name_servers': [ None, 'Champ_absent_du_registre' ],
}

hk = {
    'registrar': [ r'Registrar Name:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Domain Name Commencement Date:\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ r'Expiry Date:\s+(.+)', '' ],
    'registrant': [ r'Registrant Contact Information:\n\nCompany English Name .+:\s+(.+)', '' ],
    'name_servers': [ None, 'Champ_impossible_à_identifier_précisément' ],
}

se = {
    'registrar': [ r'registrar:\s+(.+)', '' ],
    'domain_name': [ r'domain:\s+(.+)', '' ],
    'creation_date': [ r'created:\s+(.+)', '' ],
    'updated_date': [ r'modified:\s+(.+)', '' ],
    'expiration_date': [ r'expires:\s+(.+)', '' ],
    'registrant': [ None, 'Champ_absent_du_registre' ],
    'name_servers': [ r'nserver:\s+(.+)', '' ],
}

sg = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Creation Date:\s+(.+)', '' ],
    'updated_date': [ r'Modified Date:\s+(.+)', '' ],
    'expiration_date': [ r'Expiration Date:\s+(.+)', '' ],
    'registrant': [ r'\n\s+Name:\s+(.+)', '' ],
    'name_servers': [ None, 'Champ_impossible_à_identifier_précisément' ],
}

mobi = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Creation Date:\s+(.+)', '' ],
    'updated_date': [ r'Updated Date:\s+(.+)', '' ],
    'expiration_date': [ r'Registry Expiry Date:\s+(.+)', '' ],
    'registrant': [ r'Registrant Name:\s+(.+)', '' ],
    'name_servers': [ r'Name Server:\s+(.+)', '' ],
}

pt = {
    'registrar': [ None, 'Champ_absent_du_registre' ],
    'domain_name': [ r'.+Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'.+Creation Date \(dd/mm/yyyy\):\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ r'.+Expiration Date \(dd/mm/yyyy\):\s+(.+)', '' ],
    'registrant': [ r'.+Registrant\n\s+(.+)', 'TODO' ],
    'name_servers': [ r'.+Nameserver:\s+.+NS\s+(.+)\.', '' ],
}

tech = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Creation Date:\s+(.+)', '' ],
    'updated_date': [ r'Updated Date:\s+(.+)', '' ],
    'expiration_date': [ r'Registry Expiry Date:\s+(.+)', '' ],
    'registrant': [ r'Registrant Name:\s+(.+)', '' ],
    'name_servers': [ r'Name Server:\s+(.+)', '' ],
}

ie = {
    'registrar': [ None, 'Champ_absent_du_registre' ],
    'domain_name': [ r'domain:\s+(.+)', '' ],
    'creation_date': [ r'registration:\s+(.+)', '' ],
    'updated_date': [ None, '1970-01-01T00:00:01' ],
    'expiration_date': [ r'renewal:\s+(.+)', '' ],
    'registrant': [ None, 'Champ_absent_du_registre' ],
    'name_servers': [ r'nserver:\s+(.+)', '' ],
}

paris = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Creation Date:\s+(.+)', '' ],
    'updated_date': [ r'Updated Date:\s+(.+)', '' ],
    'expiration_date': [ r'Registry Expiry Date:\s+(.+)', '' ],
    'registrant': [ r'Registrant Name:\s+(.+)', '' ],
    'name_servers': [ r'Name Server:\s+(.+)', '' ],
}

pro = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Creation Date:\s+(.+)', '' ],
    'updated_date': [ r'Updated Date:\s+(.+)', '' ],
    'expiration_date': [ r'Registry Expiry Date:\s+(.+)', '' ],
    'registrant': [ r'Registrant Name:\s+(.+)', '' ],
    'name_servers': [ r'Name Server:\s+(.+)', '' ],
}

kz = {
    'registrar': [ r'Current Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Domain created:\s+(.+)\s+.*$', '' ],
    'updated_date': [ r'Last modified:\s+(.*)\s+.*$', '' ],
    'expiration_date': [ None, '' ],
    'registrant': [ r'Name\.+:\s+(.+)', '' ],
    'name_servers': [ r'^.+server\.+:\s+(.+)', '' ],
}

immo = {
    'registrar': [ r'Registrar:\s+(.+)', '' ],
    'domain_name': [ r'Domain Name:\s+(.+)', '' ],
    'creation_date': [ r'Creation Date:\s+(.+)', '' ],
    'updated_date': [ r'Updated Date:\s+(.*)$', '' ],
    'expiration_date': [ r'Registry Expiry Date:\s+(.+)', '' ],
    'registrant': [ r'Regitrant Name:\s+(.+)', '' ],
    'name_servers': [ r'Name Server:\s+(.+)', '' ],
}
