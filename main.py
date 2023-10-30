import sys
import json
import ast

data_to_pass_back = "received :"

input = sys.argv[1]
output = data_to_pass_back + input

print(output)
sys.stdout.flush()