import requests

response = requests.get('https://xkcd.com/353/')
# print(response)

##Let's say we wanted to download an image from the above website and we have the url as
##https://imgs.xkcd.com/comics/python.png.

response_image = requests.get('https://imgs.xkcd.com/comics/python.png')
##If we print the above value we will get the actual image in bytes format
# print(response_image.content)
##Which would look something like a very long bytes content
#\\.\x0b@\xa0X_6\x1b\xf7\xe8s\xa7\xff\xa0FH\x8a+\xf5\xf7\x10\

##Now to save the image in the same folder we can do the following:
with open('response_img.png','wb')as file:
    file.write(response_image.content)

##To check successfull connectivity we have to methods.
print(response.status_code)
print(response.ok)

# Output
# 200
# True

##How to get headers of the above response_img
print(response_image.headers)

##Output
# {'Connection': 'keep-alive', 'Content-Length': '90835', 'Server': 'nginx', 'Content-Type': 'image/png',
#  'Last-Modified': 'Mon, 01 Feb 2010 13:07:49 GMT', 'ETag': '"4b66d225-162d3"', 
#  'Expires': 'Sun, 05 Feb 2023 15:29:29 GMT', 'Cache-Control': 'max-age=300', 'Accept-Ranges': 'bytes',
#   'Date': 'Sun, 05 Feb 2023 15:24:30 GMT', 'Via': '1.1 varnish', 'Age': '0', 
#   'X-Served-By': 'cache-del21733-DEL', 'X-Cache': 'MISS', 'X-Cache-Hits': '0', 
#   'X-Timer': 'S1675610669.109298,VS0,VE1266'}