# hacker-generator
Generates Hollywood hacking lingo

#### ip.py

This script is for generating a random IP address, which can be specified as either a valid IP or an invalid one. Specifying an invalid IP address causes a random chunk of the IP address to be >255, making it a non-existent address.

**Usage:** `python3 ip.py valid|invalid`

**Example:**
```
$ python3 ip.py valid
166.144.168.186
$ python3 ip.py invalid
52.62.215.312
```
