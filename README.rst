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
		
		$ dig github.com | ./ipcountry.py
		... snip ...
		;; ANSWER SECTION:
		github.com.		30	IN	A	[US:192.30.252.131]
		
		;; AUTHORITY SECTION:
		github.com.		1511	IN	NS	ns2.p16.dynect.net.
		github.com.		1511	IN	NS	ns3.p16.dynect.net.
		github.com.		1511	IN	NS	ns4.p16.dynect.net.
		github.com.		1511	IN	NS	ns1.p16.dynect.net.
		
		;; ADDITIONAL SECTION:
		ns1.p16.dynect.net.	3097	IN	A	[US:208.78.70.16]
		ns2.p16.dynect.net.	3097	IN	A	[US:204.13.250.16]
		ns3.p16.dynect.net.	3097	IN	A	[US:208.78.71.16]
		ns4.p16.dynect.net.	3097	IN	A	[US:204.13.251.16]
		... snip ...
	
	The country code 'US' (which means 'United States') is inserted.

To insert the country names instead of the codes.
	
	::
		
		$ dig github.com | ./ipcountry.py -n
		... snip ...
		;; ANSWER SECTION:
		github.com.		30	IN	A	[United States:192.30.252.128]
		... snip ...
	
	The country name 'United States' is inserted.

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
