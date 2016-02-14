import urllib2
import re

urls = ["http://nytimes.com","http://www.theatlantic.com"]
i = 0
regex = '<title>(.+?)</title>'
pattern = re.compile(regex)

while i < len(urls): 
	htmlfile = urllib2.urlopen(urls[i])
	htmltext = htmlfile.read()
	titles = re.findall(pattern,htmltext)
	print titles
	i += 1