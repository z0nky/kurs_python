import json

data =  {
    'username': 'ritaly',
    'position': 'software developer',
    'company': 'beta district',
    'tech': {
        'frontend': ['html', 'css', 'sass', 'bootstrap', 'js', 'es6', 'angular', 'react'],
        'backend': ['python', 'flask', 'django', 'ruby', 'rails', 'elixir', 'go'],
        'databases': ['oracle', 'mysql', 'psql', 'aerospike', 'mongodb'],
        'other': ['gimme more coffee', 'code as beautiful as unicorns & glitter']
    }
}

filename = 'users.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)