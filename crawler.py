# 技術參照：https://youtu.be/9Z9xKWfNo7k
# 去除ssl憑證：https://clay-atlas.com/us/blog/2021/09/26/python-en-urllib-error-ssl-certificate/


from fileinput import close
import bs4
import urllib.request as req
import ssl

# step1:取得原始碼

ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.learncodewithmike.com/"

# 看起來像正常人連線
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
r = open("crawler_source_code", "w")
r.write(data)
r.close

# TERMINAL: pip3 install beautifulsoup4
soup = bs4.BeautifulSoup(data, "html.parser")
p = open("crawler_prettify_source_code", "w")
p.write(soup.prettify())
p.close

# step2:解析原始碼ß
titles = soup.find_all(
    "h3", class_="post-title entry-title")
for title in titles:
    print(title.a.string)
