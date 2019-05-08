__author__ = 'Administrator'

import urllib
import http.cookiejar
import os

def get_file(url):
    header = {'User-Agent': 'Mozilla/4.0 (compatible;' 'MSIE 8.0;' 'Windows NT 6.1;WOW64;Trident/4.0;SLCC2; .NET CLR 2.0.50727)', 'Content-Type': 'text/xml'}
    cookie = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
    urllib.request.install_opener(opener)

    path = os.getcwd() + '\image'

    try:
        req = urllib.request.Request(
            url='http://js.cas.jsoss.net/sso/captcha.htm',
            headers=header
        )
        result = urllib.request.urlopen(req)
        data = result.read()

        filename = 'authCode.jpg'
        file = open(path + '\\' + filename, 'wb')
        file.write(data)
        file.flush()
        file.close()
    except:
        return None