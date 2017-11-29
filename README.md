# WHOIS

Module `python` permettant de récupérer & parser les informations WHOIS des domaines. Basé sur le travail de [DDarko](http://ddarko.org)

# Fonctionnalités

  * Module `python` simulant la commande `whois`.
  * Interface d'accès simple et homogène des informations de WHOIS pour un domaine donné.
  * Récupère les informations pour un grand nombre de TLDs : 
    * `.com`
    * `.net`
    * `.org`
    * `.uk`
    * `.pl`
    * `.ru`
    * `.lv`
    * `.jp`
    * `.de`
    * `.at`
    * `.eu`
    * `.biz`
    * `.info`
    * `.name`
    * `.us`
    * `.co`
    * `.me`
    * `.be`
    * `.nz`
    * `.cz`
    * `.it`
    * `.fr`
    * `.re`
    * `.yt`
 * Fait une vraie requête WHOIS plutôt que de scrapper une interface web.
 * Conversion des dates dans des objets de type `datetime`.
 * Possibilité théorique de cacher les informations; voir si nécessaire à notre besoin.

# Exemples d'utilisation

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
  * 2017-10-26 : Passage en socket des appels, levée d'exception en cas de réponse vide & traduction en Français du `README.md`.
  * 2017-11-29 : On lève une exception différenciable en cas de TLD inconnu.
