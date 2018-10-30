from urllib.request import urlopen, Request
def get_page(url):
    url = "https://udacity.github.io/cs101x/urank/"
    request = Request(url)
    response = urlopen(request)
    html = response.read()
    response.close()

print(get_page('https://udacity.github.io/cs101x/urank/'))

