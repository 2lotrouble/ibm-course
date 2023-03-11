# !pip install randomuser

from randomuser import RandomUser
import pandas as pd

r = RandomUser()
some_list = r.generate_users(10)

print(some_list)
name = r.get_full_name()

for user in some_list:
    print (user.get_full_name()," ",user.get_email())