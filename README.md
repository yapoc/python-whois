# WHOIS

Python module/library for retrieving WHOIS information of domains.
By DDarko  http://ddarko.org/

# Features

 * Python wrapper for Linux "whois" command
 * simple interface to access parsed WHOIS data for a given domain
 * able to extract data for all the popular TLDs (com, org, net, biz, info, pl, jp, uk, nz,  ...)
 * query a WHOIS server directly instead of going through an intermediate web service like many others do
 * works with Python 2.4+ and Python 3.x
 * all dates as datetime objects
 * possibility to cache results


# Usage example

```
>>> import whois
>>> domain = whois.query('google.com')

>>> print(domain.__dict__)
{
	'expiration_date': datetime.datetime(2020, 9, 14, 0, 0),
	'last_updated': datetime.datetime(2011, 7, 20, 0, 0),
	'registrar': 'MARKMONITOR INC.',
  'registrant': 'DNS Admin',
	'name': 'google.com',
	'creation_date': datetime.datetime(1997, 9, 15, 0, 0)
}

>>> print(domain.name)
google.com

>>> print(domain.expiration_date)
2020-09-14 00:00:00
```

# ChangeLog

  * 2017-10-24 : Première récupération du code & adaptation à mes besoins personnels pour alimenter les champs dont j'ai besoin.
