import sys
import string
import DNS
from IPy import *

DNS.ParseResolvConf()
r = DNS.DnsRequest(name = sys.argv[1], qtype='A')

a = r.req()

if len(a.answers) == 0:
	sys.exit()

if len(sys.argv) > 2:
   domain = sys.argv[2]
else:
   domain = sys.argv[1]

i = IP(a.answers[0]['data'])
l = domain

while (l[-len(domain):len(l)] == domain):
   s = string.split(i.strNormal(),'.')
   s.reverse()
   r = DNS.DnsRequest(name = string.join(s,'.')+'.in-addr.arpa', qtype='PTR')
   b = r.req()
   i = IP(i.int() + 1)
   if len(b.answers) != 0:
      l = b.answers[0]['data']
      print l

i = IP(a.answers[0]['data'])
l = domain

while (l[-len(domain):len(l)] == domain):
   s = string.split(i.strNormal(),'.')
   s.reverse()
   r = DNS.DnsRequest(name = string.join(s,'.')+'.in-addr.arpa', qtype='PTR')
   b = r.req()
   i = IP(i.int() - 1)
   if len(b.answers) != 0:
      l = b.answers[0]['data']
      print l
