# write a code that selects a random number between 1 and 1000. The number will be the file name.

import random
file_name = str(random.randint(1,1000))+ ".png"
#print(file_name)

import urllib.request 
image_url = 'https://she-codes.org/wp-content/uploads/2019/04/shecodesLogoInLine-1.png'
urllib.request.urlretrieve(url=image_url, filename = file_name)
