# vi: set foldmethod=indent: set tabstop=2: set shiftwidth=2:
from . import tld_regexpr
import re


TLD_RE = {}
def get_tld_re(tld):
  if tld in TLD_RE: return TLD_RE[tld]
  v = getattr(tld_regexpr, tld)
  extend = v.get('extend')
  if extend:
    e = get_tld_re(extend)
    tmp = e.copy()
    tmp.update(v)

  else:
    tmp = v

  if 'extend' in tmp: del tmp['extend']
  TLD_RE[tld] = dict((k, [ re.compile(v[0], re.IGNORECASE) if isinstance(v[0], str) else v[0], v[1] ]) for k, v in tmp.items())
  return TLD_RE[tld]


[get_tld_re(tld) for tld in dir(tld_regexpr) if tld[0] != '_']


from pprint import pprint


def do_parse(whois_str, tld):
  r = {}

  if whois_str.count('\n') < 5:
    s = whois_str.strip().lower()
    if s == 'not found': return
    if s.count('error'): return
    raise Exception(whois_str)

  sn = re.findall(r'Server Name:\s?(.+)', whois_str, re.IGNORECASE)
  if sn:
    whois_str = whois_str[whois_str.find('Domain Name:'):]

  for k, v in TLD_RE.get(tld, TLD_RE['com']).items():
    if v[0] is None:
      r[k] = [ v[1] ]
    else:
      r[k] = v[0].findall(whois_str) or [ v[1] ]

  return r
  """ touch file """
