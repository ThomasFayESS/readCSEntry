#!/usr/bin/python3
import json
import argparse



parser = argparse.ArgumentParser()
parser.add_argument('inFile', help = 'Input file containing entries from CSEntry.')
parser.add_argument('--showKeys', action="store_const", const=True, help = "Show the valid key options for the fields of these entries.")
parser.add_argument('--peekFirst', action="store_const", const=True, help = "Show the first entry of the input file.")
parser.add_argument('--match', help="Return all entries where match is true. Format is 'field operator value'")
parser.add_argument('--looseMatch', help="Return all entries where any field contains this value'")
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

if 'name' in validKeys:
    mainKey = 'name'
else:
    for elKey in validKeys:
        if 'name' in elKey:
            mainKey = elKey


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
    if len(mainKey) > 0:
        print(entry[mainKey])
    else:
        print("***New Entry***")

    if full is not None:
        for field in validKeys:
            print("---" + field + ": " + str(entry[field]))
    elif field is not None:
        if field in validKeys: 
            print("---" + field + ": " + str(entry[field]))
        else:
            print("---field not found: " + field)

if match is not None and field is not None:
    for entry in listEntries:
        if match in entry[field]:
            getFields(entry, full, field)

if field is not None and match is None:
    for entry in listEntries:
        getFields(entry, full, field)

if looseMatch is not None:
    for entry in listEntries:
        for elKey in validKeys:
            if looseMatch in str(entry[elKey]):
                getFields(entry, full, elKey)

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
