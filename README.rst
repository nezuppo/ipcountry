ipcountry
=========

A filter script which inserts the country codes or names of ip addresses
in a text.


Install
-------------------

The installation procedure in case of Ubuntu is as follows.

#. Install packages. ::
	
	$ sudo apt-get install python3 python3-geoip geoip-database-contrib

#. Download the latest version of the MaxMind GeoIP Lite database. ::
	
	$ sudo geoip-database-contrib_update

#. Put ipcountry.py somewhere.


Usage
-------------------

To insert the country codes.
	::
		
		$ dig gitub.com | ./ipcountry.py 
		... snip ...
		;; ANSWER SECTION:
		gitub.com.		300	IN	A	[CH:141.8.224.239]
		
		;; AUTHORITY SECTION:
		gitub.com.		3278	IN	NS	ns100.rookdns.com.
		gitub.com.		3278	IN	NS	ns99.rookdns.com.
		
		;; ADDITIONAL SECTION:
		ns99.rookdns.com.	231	IN	A	[CH:141.8.224.239]
		ns100.rookdns.com.	231	IN	A	[CH:141.8.224.240]
		... snip ...
	
	The country code 'CH' (which means 'Switzerland') is inserted.

To insert the country names instead of the codes.
	::
		
		$ dig gitub.com | ./ipcountry.py -n
		... snip ...
		;; ANSWER SECTION:
		gitub.com.		289	IN	A	[Switzerland:141.8.224.239]
		... snip ...
	
	The country name 'Switzerland' is inserted.

See also help message.
	::
		
		$ ./ipcountry.py --help
		usage: ipcountry.py [-h] [-n] [--version] [file]
		
		A filter script which inserts the country codes or names of ip addresses in a text.
		
		positional arguments:
		  file                if omitted, a text is read from standard input
		
		optional arguments:
		  -h, --help          show this help message and exit
		  -n, --country-name  insert the country names instead of the country codes
		  --version           show program's version number and exit
