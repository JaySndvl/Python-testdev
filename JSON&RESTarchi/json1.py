import json

data='''{
    "name" : "jay",
    "phone" : {
        "type" : "intl",
        "number" : "+1 123 456 7890"
        },
        "email" : {
        "hide" : "yes"
        }
}'''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])