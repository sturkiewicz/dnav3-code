#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os
from pprint import pprint

# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    json_data = json.loads(file.read())
    

# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.


for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
    print ('Interface name is {}, the IP addresses for this interface are:'.format(interface["name"],))
    for address_type, address in interface["ietf-ip:ipv4"]["address"][0].items():
        print('{} : {}'.format(address_type, address))