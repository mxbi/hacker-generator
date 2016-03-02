# python-collection
Collection of all my miscellaneous python scrips and various bits and bobs.

### ip_generator.py

This script is for generating a random IP address, which can be specified as either a valid IP or an invalid one. Specifying an invalid IP address causes a random chunk of the IP address to be >255, making it a non-existent address.

**Usage:** `python3 ip.py valid|invalid`

**Example:**
```
$ python3 ip.py valid
166.144.168.186
$ python3 ip.py invalid
52.62.215.312
```
### random_domain_finder.py

This script randomly searches for domain names which match the length and TLDs you specify. There are no input arguments, however at the top of the file you can choose the tlds you want to search by adding them to **'tldlist'** and change the length of the string to search with by changing **'length'**. You also need a [Whoapi API key](whoapi.com) as the variable **'apikey'** for the script to work. I use this whenever I'm looking for available 3-letter domain names.