import sys
import random
import string
import urllib.request as urllib2
import time

# Parameters
length = 3
tldlist = ["net","org"]

i = 1
while i < 2:

	# Pick domain
	tld = random.choice(tldlist)
	name = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
	domain = str(name) + "." + str(tld)
	print("Attempting " + domain)

	# Query API
	apikey = "*** PLACE API KEY HERE ***"
	url = "http://api.whoapi.com/?apikey=" + apikey + "&r=taken&domain=" + domain
	s = urllib2.urlopen(url)
	contents = str(s.read())
	#print(contents)

	# Parse XML
	splitp = contents.split('"taken":')
	splits = str(splitp[1]).split('}')
	taken = splits[0]

	# Write result to file
	f = open('domains.txt', 'a')
	result = domain + ' ' + str(taken)
	print(result)
	f.write(result)
	f.close()

	if taken == 0:
		i = i + 1
		print("Found free domain at:" + domain)
	else:
		time.sleep(62)
