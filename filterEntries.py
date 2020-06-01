#!/usr/bin/python3
import json
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('inFile', help = 'Input file containing entries from CSEntry.')
parser.add_argument('--showKeys', action="store_const", const=True, help = "Show the valid key options for the fields of these entries.")
parser.add_argument('--peekFirst', action="store_const", const=True, help = "Show the first entry of the input file.")
parser.add_argument('--match', help="Return all entries where match is true. Format is 'field operator value'")
parser.add_argument('--looseMatch', help="Return all entries where any field contains this value'")
parser.add_argument('--user', help="Match specified user.")
parser.add_argument('--all', action='store_const', const=True, help = "Return all fields for all hosts.")
parser.add_argument('--ioc', action="store_const", const=True, help = "Return all IOC server hosts.")
parser.add_argument('--name', nargs='?', const = "all", help = "Return all hosts matching name.")
parser.add_argument('--device', help = "Return all hosts matching specified device type.")
parser.add_argument('--created_after', help = "Return all hosts created on or after date in format yyyy-mm-dd hh:mm.")
parser.add_argument('--created_before', help = "Return all hosts created on or before date in format yyyy-mm-dd hh:mm.")
parser.add_argument('--updated_after', help = "Return all hosts updated on or after date in format yyyy-mm-dd hh:mm.")
parser.add_argument('--updated_before', help = "Return all hosts updated on or before date in format yyyy-mm-dd hh:mm.")
parser.add_argument('--full', action='store_const', const=True, help = "Flag to return all fields of matching hosts.")
parser.add_argument('--field', help = "Return specified field for all matching hosts.")

args = parser.parse_args()
inFile = args.inFile

showKeys = args.showKeys
peekFirst = args.peekFirst

match = args.match
looseMatch = args.looseMatch

user = args.user
all = args.all
ioc = args.ioc
name = args.name
device = args.device

full = args.full
field = args.field
created_after = args.created_after
created_before = args.created_before
updated_after = args.updated_after
updated_before = args.updated_before

with open(inFile,'r') as f:
    listEntries=json.load(f)


if len(listEntries) < 1:
    print("No valid entries found in input field.")
    exit(1)

# Get valid keys based on first element
validKeys = []
validKeys = listEntries[0].keys()
if len(validKeys) < 1:
    print("No valid keys found for this entry.")
    exit(1)

if match is not None:
    if len(match.split(' ')) < 3:
        print("Match must be of form 'value operator field'.")
        print("For example --match 'thomas in user' is valid expression.")
        exit(1)
    else:
        listMatch = match.split(' ')
        matchOperator = listMatch[1]
        matchValue = listMatch[0]
        matchField = listMatch[2]
        if matchField not in validKeys:
            print("Field to match against is invalid: " + matchField)
            exit(1)


if showKeys is not None:
    print("Valid keys:")
    for el in validKeys:
        print("->" + str(el))

if peekFirst is not None:
    entry = listEntries[0]
    print("First entry:")
    for el in entry.keys():
        print("---" + str(el) + ": " + str(entry[el]))

def getFields(entry, full, field):
    print(entry['name'])
    if full is not None:
        for field in validKeys:
            print("---" + field + ": " + str(entry[field]))
    elif field is not None:
        if field in validKeys: 
            print("---" + field + ": " + str(entry[field]))
        else:
            print("---field not found: " + field)

if match is not None:
    for entry in listEntries:
        if matchOperator == "in":
            if matchValue in entry[matchField]:
                getFields(entry, full, matchField)
        elif matchOperator == "==":
            if matchValue == entry[matchField]:
                getFields(entry, full, matchField)
        elif matchOperator == "<=":
            if matchValue <= entry[matchField]:
                getFields(entry, full, matchField)
        elif matchOperator == ">=":                
            if matchValue >= entry[matchField]:
                getFields(entry, full, matchField)

if looseMatch is not None:
    for entry in listEntries:
        for elKey in validKeys:
            if looseMatch in str(entry[elKey]):
                getFields(entry, full, elKey)

if all is not None:
    for entry in listEntries:
        getFields(entry, full, field)

if name is not None:
    for entry in listEntries:
        if name in entry['name'] or name == "all":
            getFields(entry, full, field)

if user is not None:
    for entry in listEntries:
        if user in entry['user']:
            getFields(entry, full, field)

if user is not None:
    for entry in listEntries:
        if user in entry['user']:
            getFields(entry, full, field)

if ioc is not None:
    for entry in listEntries:
        if entry['is_ioc'] == True:
            getFields(entry, full, field)

if device is not None:
    for entry in listEntries:
        if device in entry['device_type']:
            getFields(entry, full, field)

if created_after is not None:
    for entry in listEntries:
        if entry['created_at'] >= created_after:
            getFields(entry, full, field)

if created_before is not None:
    for entry in listEntries:
        if entry['created_at'] <= created_before:
            getFields(entry, full, field)

if updated_after is not None:
    for entry in listEntries:
        if entry['updated_at'] >= updated_after:
            getFields(entry, full, field)

if updated_before is not None:
    for entry in listEntries:
        if entry['updated_at'] <= updated_before:
            getFields(entry, full, field)

if ioc is not None:
    for entry in listEntries:
        if entry['is_ioc'] == True:
            getFields(entry, full, field)

if created_after is not None:
    for entry in listEntries:
        if entry['created_at'] >= created_after:
            getFields(entry, full, field)

if created_before is not None:
    for entry in listEntries:
        if entry['created_at'] <= created_before:
            getFields(entry, full, field)

if updated_after is not None:
    for entry in listEntries:
        if entry['updated_at'] >= updated_after:
            getFields(entry, full, field)

if updated_before is not None:
    for entry in listEntries:
        if entry['updated_at'] <= updated_before:
            getFields(entry, full, field)
