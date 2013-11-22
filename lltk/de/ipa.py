#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from lxml import html
from functools32 import lru_cache as caching

@caching(maxsize =8)
def ipa(word):
	''' Try to scrape the IPA writing from de.wiktionary.org. '''

	word = unicode(word)
	page = requests.get('http://%s.wiktionary.org/wiki/%s' % ('de', word))
	tree = html.fromstring(page.text)

	result = tree.xpath('//span[@class="ipa"]/text()')
	result = filter(lambda x: x != u'\u2026', result)
	if len(result):
		if not result[0].startswith('/') and not result[0].endswith('/'):
			result[0] = '/' + result[0] + '/'
		return [result[0]]
	return [None]

if __name__ == "__main__":
	import sys
	if len(sys.argv) > 1:
		result = ipa(sys.argv[1].decode('utf-8'))
		if result[0] == '':
			print '-'
		elif result[0]:
			print ', '.join(result)
