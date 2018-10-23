from urllib.request import urlopen, Request
url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()
words = html.split()
print(len(words))