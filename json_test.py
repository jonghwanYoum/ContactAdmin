import json

python_data = ['foo', {'bar': ('baz', None, 1.0, 2)}]

to_json_data = json.dumps(python_data,separators=(',',':'))
to_json_data = json.dump(python_data,indent=4)

print(to_json_data)