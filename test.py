from urllib.request import urlopen, Request
url = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()
words = html.split()
print(len(words))

"""def get_page(url):
    try: 
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
    
words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
print (len(words))"""