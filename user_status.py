#!/usr/bin/python

users = [
	{'admin': True, 'active': True, 'name': 'Devi'},
    {'admin': True, 'active': False, 'name': 'Amit'},
	{'admin': False, 'active': True, 'name': 'Vivek'},
	{'admin': False, 'active': False, 'name': 'Jyothi'},
	{'admin': True, 'active': True, 'name': 'Smitha'},
	{'admin': False, 'active': True, 'name': 'Sunil'},
	{'admin': True, 'active': True, 'name': 'Ravi'},
	{'admin': True, 'active': True, 'name': 'thisistheuser'},
]

line = 1
for user in users: 
	if user['admin'] and user['active']:
		print("%s ACTIVE - (ADMIN) %s" % (line, user['name']))
	elif user['admin']:
		print("%s (ADMIN) %s" % (line, user['name']))
	elif user['active']:
		print("%s ACTIVE - %s" % (line, user['name']))
	else:
		print("%s %s" % (line, user['name']))
	line += 1


