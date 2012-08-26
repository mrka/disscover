#!/usr/bin/python

import sys
import string
import DNS
from IPy import *

# Prepare DNS resolver
DNS.ParseResolvConf()

# Request IP for host name given in first argument
dnsAnswer = DNS.DnsRequest(name=sys.argv[1], qtype='A').req()

# Exit if no DNS A record was found for the host name
if len(dnsAnswer.answers) == 0:
    sys.exit()

# Either use the host name as domain name or use the second argument if given
if len(sys.argv) > 2:
    domainNameGiven = sys.argv[2]
else:
    domainNameGiven = sys.argv[1]

firstIPForHostname = IP(dnsAnswer.answers[0]['data'])
domainNameSearched = domainNameGiven

# Keep iterating as long as we stay inside the given domain
while (domainNameSearched[-len(domainNameGiven):len(domainNameSearched)]
        == domainNameGiven):
    reversedIPArray = string.split(firstIPForHostname.strNormal(), '.')
    reversedIPArray.reverse()
    dnsAnswerTwo = DNS.DnsRequest(name=string.join(reversedIPArray, '.') +
                                  '.in-addr.arpa', qtype='PTR').req()
    firstIPForHostname = IP(firstIPForHostname.int() + 1)
    if len(dnsAnswerTwo.answers) != 0:
        domainNameSearched = dnsAnswerTwo.answers[0]['data']
        print domainNameSearched
