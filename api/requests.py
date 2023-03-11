import requests

import os
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

print(r.status_code)

print(r.request.headers)

print("request body:", r.request.body)

header=r.headers
print(r.headers)

header['date']
header['Content-Type']

r.encoding
r.text[0:100]

# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'
r=requests.get(url)
print(r.headers)
print(r.headers['Content-Type'])

path=os.path.join(os.getcwd(),'image.png')
print(path)

with open(path,'wb') as f:
    f.write(r.content)
print(Image.open(path))