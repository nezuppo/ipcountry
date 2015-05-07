#!/usr/bin/env python3

'A filter script which inserts the country codes or names of ip addresses in a text.'

__author__	= 'Nezuppo'
__version__	= '0.0.1'
__date__	= '7 May 2015'

import re
import sys
import GeoIP
import argparse

def insertCountry(sLine, bUseName=False, oGeoIP=None, oRe=None):
	if oGeoIP == None:
		oGeoIP = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
	
	if oRe == None:
		oRe = re.compile(
			'(^|[^\.\d])'
			'(?P<IpLike>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
			'([^\.\d]|$)'
		)
	
	oMatch = oRe.search(sLine)
	if oMatch == None:
		return sLine
	
	getter = (
		oGeoIP.country_code_by_addr
		if bUseName == False else
		oGeoIP.country_name_by_addr
	)
	
	sIpLike = oMatch.group('IpLike')
	sCountry = getter(sIpLike)
	
	iStart	= oMatch.start('IpLike')
	iEnd	= oMatch.end('IpLike')
	
	sInserted = insertCountry(sLine[:iStart], bUseName, oGeoIP, oRe)
	sInserted += (
		'[{}:{}]'.format(sCountry, sIpLike)
		if sCountry != None else
		sIpLike
	)
	sInserted += insertCountry(sLine[iEnd:], bUseName, oGeoIP, oRe)
	
	return sInserted

def main():
	oParser = argparse.ArgumentParser(description=__doc__)
	oParser.add_argument('-n', '--country-name', action='store_true',
		help='insert the country names instead of the country codes')
	oParser.add_argument('--version', action='version',
		version='%(prog)s {}'.format(__version__))
	oParser.add_argument('file', nargs='?',
		help='if omitted, a text is read from standard input')
	oParsed = oParser.parse_args()
	
	oFile = sys.stdin if oParsed.file == None else open(oParsed.file)
	for sLine in oFile:
		print(insertCountry(sLine, oParsed.country_name), end='')

if __name__ == '__main__':
	try:
		main()
	except BrokenPipeError:
		pass
	except KeyboardInterrupt:
		pass
