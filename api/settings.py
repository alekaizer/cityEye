
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
				'allowed': '["user", "admin"]',
				'required': True
			}
	}

advertiser = {
		'companyName': {
				'type': 'string',
				'required': True
			},
		'type': {
			'type':'list',
			'required': True
			},
		'logo': {
			'type': 'string'
			},
		'address': {
			'type': 'string',
			'required': True
			},
	}

product = {
		'image':{
			'type': 'string',
			},
		'title': {
			'type': 'string',
			'required': True
			},
		'description': {
			'type': 'string',
			'required': True
			},
		'beginingDate': {
			'type': 'datetime',
			'required': True
			},
		'endingDate': {
			'type': 'datetime',
			'required': True
			},
		'city': {
			'type': 'string',
			'required': True
			},
		}
people = {
		'schema': user
		}

users = {
		'schema': user
		}
advertisers = {
		'schema': advertiser
		}

feed = {
		'schema': product
		}
DOMAIN = {'people': people,
	  'users': users,
	  'advertisers': advertisers,
	  'feed': product
		}

