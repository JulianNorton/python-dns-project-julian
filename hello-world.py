import dns.resolver
import dns
print('\n hello world \n')

# https: // github.com/rthalley/dnspython/blob/master/examples/mx.py
answers = dns.resolver.query('julian.nyc', 'MX')
answers_more = dns.resolver.query('juliannorton.com', 'MX')
for rdata in answers:
    print('Host', rdata.exchange, 'has preference', rdata.preference)
    
for rdata in answers_more:
    print('Host', rdata.exchange, 'has preference', rdata.preference)

