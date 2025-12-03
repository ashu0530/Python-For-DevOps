#Python dictionary as a json file by using the json.dump method this is how you would update the policy file you just modified
import json
import re
from pprint import pprint
with open(r'c:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\iam.json','r') as openfiled:
    policy = json.load(openfiled)
    print(policy,type(policy))
    pprint(policy)

    policy['Statement']['Resource'] = 'EC2'
    policy['Version'] = "v2"
    print(policy)
    pprint(policy)


'''
The most commonly used library for parsing YAML files in Python is PyYAML. It is
 not in the Python Standard Library, but you can install it using pip:
 $ pip install PyYAML
'''

import yaml
with open (r'c:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\playbook.yml','r') as playbook:
    yamlfile = yaml.safe_load(playbook)
    print(yamlfile,type(yamlfile))


with open (r'c:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\playbook.yml','w') as playbook2:
    yaml.dump(yamlfile,playbook2)
    print(playbook2)