#!/usr/bin/python3
from csentry import CSEntry
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--hosts', action = 'store_const', const = True, help = 'Fetch host entries from CSEntry.')
parser.add_argument('--interfaces', action = 'store_const', const = True, help = 'Fetch interface entries from CSEntry.')
parser.add_argument('--networks', action = 'store_const', const = True, help = 'Fetch network entries from CSEntry.')
parser.add_argument('--domains', action = 'store_const', const = True, help = 'Fetch domain entries from CSEntry.')

args = parser.parse_args()
hosts = args.hosts
interfaces = args.interfaces
networks = args.networks
domains = args.domains

def fetchEntries(funcGetter):

    listEntries=[]
    entries = funcGetter()
    for x in entries:
        listEntries.append(x)
    if funcGetter == csentry.get_hosts:
        outFile = "hosts.json"
    elif funcGetter == csentry.get_interfaces:
        outFile = "interfaces.json"
    elif funcGetter == csentry.get_networks:
        outFile = "networks.json"
    elif funcGetter == csentry.get_domains:
        outFile = "domains.json"
    else:
        print("Getter function: "  + funcGetter + " unsupported.")

    with open(outFile, 'w') as f:
        json.dump(listEntries,f)

if hosts is not None or interfaces is not None or networks is not None or domains is not None:
    csentry = CSEntry(token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1OTEwMDY3NTEsIm5iZiI6MTU5MTAwNjc1MSwianRpIjoiMTBkYWM3Y2MtM2UzNi00ZjBhLWIyNTctMWU5YmE1NjczOTRkIiwiaWRlbnRpdHkiOjIwLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.rKXbr66DIDdL58Gu20P07WXdI1JN8trJy15glI4UdEM')

if hosts is not None:
    fetchEntries(csentry.get_hosts)

if interfaces is not None:
    fetchEntries(csentry.get_interfaces)

if networks is not None:
    fetchEntries(csentry.get_networks)

if domains is not None:
    fetchEntries(csentry.get_domains)
