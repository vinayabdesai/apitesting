import requests

r = requests.get('https://api.github.com/events')
Event_list = []
python_obj = r.json()
count =0

for obj in python_obj:
	Event_list.append(obj['type'])
	if(obj['type'] == 'PushEvent'):
		print(obj['payload']['commits'][0]['url'])
		count = count+1
		print "count = ", count 
	else:
		print "No Message"

print "Event List =", Event_list
Sublist_type = set(Event_list)
print "\n \n Sub Set of Event list",Sublist_type


for lst in Sublist_type:
	if (lst == 'PushEvent'):
		print "Its push event hurray!!"
	else: 
		print "OK event", lst
		
