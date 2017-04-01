import requests
import json

inputdict = {"userId": 11,
            "id": 1,
			"title": "New account",
			"body": "Hi!! THis is a newly created record, please verify"}
requests.post('http://jsonplaceholder.typicode.com/posts',data = inputdict)

r = requests.get('http://jsonplaceholder.typicode.com/posts?userId=11')


print "Status , Header, text", r.status_code,"\n",r.headers,"\n",r.text

