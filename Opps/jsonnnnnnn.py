# json = javascript object notation 
import json

a={"name":"anees","age":23,"languages":"python","boolean":True}

print(type(a))
# convert this into json file

b=json.dumps(a)
print(b)
print(type(b))
parsed=json.loads(b)
print(parsed)
print(type(parsed))