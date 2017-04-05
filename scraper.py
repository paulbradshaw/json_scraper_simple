#import our libraries
import json
import requests
import urllib
import scraperwiki

#some JSON files
jsonurl = 'https://petition.parliament.uk/petitions/178844.json'

#fetch the json from the URL
response = urllib.urlopen(jsonurl)
#load it into variable called x
x = json.loads(response.read())
#let's see what we have
print x
print len(x)
#drill down a bit into the 'posts' branch which contains everything
print x['data']['type']
print x['data']['attributes']['action']
print x['data']['attributes']['signature_count']

#store that in a new variable
signatures = x['data']['attributes']['signature_count']
record = {}
record['signatures'] = signatures
record['id'] = jsonurl
scraperwiki.sql.save(['id'], record)
