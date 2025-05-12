# load necessary components
from trafilatura import fetch_url, extract
# download a web page
url = 'https://github.blog/2019-03-29-leader-spotlight-erin-spiceland/'
downloaded = fetch_url(url)
downloaded is None
# assuming the download was successfulFalse# extract information from HTML
result = extract(downloaded)
print(result)
