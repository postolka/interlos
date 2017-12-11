from pprint import pprint
from urllib.request import urlopen
from urllib.error import URLError
import os.path

import re

# src = "https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/Moose.html"
import sys

# tgt = 'Moose'
tgt = 'Computer_programming'
pattern = "https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/{}.html"


def get_links(word):
	pprint('Opening: {}'.format(pattern.format(word)))
	f = urlopen(pattern.format(word))
	return set(re.findall('href="([A-Z]\S+).html', str(f.read())))


limit = 10
path = 'Moose'
# path = 'Computer_programming'
src = {'': set([path])}
pprint(src)
l = 0
while True:
	l += 1
	# if l > limit:
	# 	break

	print('Level {}'.format(l))
	new_set = {}
	for path, words in src.items():
		for word in words:
			try:
				cache_file = 'cache/' + word
				if os.path.isfile(cache_file):
					f = open(cache_file)
					html = str(f.read())
					f.close()
				else:
					# print('Cache miss: [{}]'.format(cache_file))
					# print('Opening: {}'.format(pattern.format(word)))
					f = urlopen(pattern.format(word))
					html = str(f.read())
					f.close()
					fh = open(cache_file, "w")
					fh.write(html)
					fh.close()

				new_words = set(re.findall('href="([A-Z]\S+).html', html))

				for test_word in new_words:
					if test_word == tgt:
						print('Got it!')
						print(path + word + test_word)
						sys.exit()
				new_set[path + word] = new_words
			except URLError as e:
				pass

	if l > limit:
		pprint(new_set)
	src = new_set
