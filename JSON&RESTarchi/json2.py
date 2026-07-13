import json

input = '''[
  { "id" : "001",
    "x" : "2",
    "name" : "jay"
  },
  { "id" : "002",
    "x" : "7",
    "name" : "jane"
  }
]'''

info = json.loads(input)
for item in info:
    print('ID:', item["id"])
    print('Name:', item["name"])
    print('Attributes:', item["x"])