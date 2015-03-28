
MONGO_USERNAME = 'root'
MONGO_PASSWORD = 'garage48'
MONGO_DBNAME = 'cityEYE'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

user = {
		'firstname': {
				'type':'string',
			},
		'lastname': {
				'type': 'string',
				'required': True
			},
		'age': {
				'type': 'string'
			},
		'address': {
				'type': 'string',
				'required': True
			},
		'role': {
				'type': 'list',
				'allowed': '["user", "advertiser", "admin"]',
				'required': True
			}
	}


product = {
		'name'
		}
people = {
		'schema': user
		}


DOMAIN = {'people': people,
	  'users': people		
		}

