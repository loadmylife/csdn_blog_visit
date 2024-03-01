import requests
from bs4 import BeautifulSoup
import lxml
import random
import time
from lxml import etree

# 可以通过抓包工具获取,模拟浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"}


# 要刷的文章
url01 = 'https://blog.csdn.net/weixin_43608153/article/details/128432335?spm=1001.2014.3001.5501'
url02 = 'https://download.csdn.net/download/weixin_43608153/87343781?spm=1001.2014.3001.5501'
url03 = 'https://blog.csdn.net/weixin_43608153/article/details/127747672?spm=1001.2014.3001.5501'
url04 = 'https://blog.csdn.net/weixin_43608153/article/details/124877250?spm=1001.2014.3001.5501'
url05 = 'https://blog.csdn.net/weixin_43608153/article/details/123934289?spm=1001.2014.3001.5501'
url06 = 'https://download.csdn.net/download/weixin_43608153/85072286?spm=1001.2014.3001.5501'
url07 = 'https://download.csdn.net/download/weixin_43608153/85072011?spm=1001.2014.3001.5501'
url08 = 'https://download.csdn.net/download/weixin_43608153/83956106?spm=1001.2014.3001.5501'
url09 = 'https://blog.csdn.net/weixin_43608153/article/details/123318675?spm=1001.2014.3001.5501'
url10 = 'https://blog.csdn.net/weixin_43608153/article/details/115658601?spm=1001.2014.3001.5501'
url11 = 'https://download.csdn.net/download/weixin_43608153/12736492?spm=1001.2014.3001.5501'
url12 = 'https://blog.csdn.net/weixin_43608153/article/details/107177747?spm=1001.2014.3001.5501'
url13 = 'https://blog.csdn.net/weixin_43608153/article/details/106887851?spm=1001.2014.3001.5501'
url14 = 'https://download.csdn.net/download/weixin_43608153/12023674?spm=1001.2014.3001.5501'
url15 = 'https://download.csdn.net/download/weixin_43608153/11835148?spm=1001.2014.3001.5501'
url16 = 'https://blog.csdn.net/weixin_43608153/article/details/98778480?spm=1001.2014.3001.5501'
url17 = 'https://blog.csdn.net/weixin_43608153/article/details/90946327?spm=1001.2014.3001.5501'
url18 = 'https://blog.csdn.net/weixin_43608153/article/details/90811132?spm=1001.2014.3001.5501'
url19 = 'https://blog.csdn.net/weixin_43608153/article/details/90732106?spm=1001.2014.3001.5501'
url20 = 'https://blog.csdn.net/weixin_43608153/article/details/90726754?spm=1001.2014.3001.5501'
url21 = 'https://blog.csdn.net/weixin_43608153/article/details/90707272?spm=1001.2014.3001.5501'
url22 = 'https://blog.csdn.net/weixin_43608153/article/details/90704366?spm=1001.2014.3001.5501'
url23 = 'https://blog.csdn.net/weixin_43608153/article/details/90678872?spm=1001.2014.3001.5501'
url24 = 'https://blog.csdn.net/weixin_43608153/article/details/88880366?spm=1001.2014.3001.5501'
url25 = 'https://blog.csdn.net/weixin_43608153/article/details/88858500?spm=1001.2014.3001.5501'
url26 = 'https://blog.csdn.net/weixin_43608153/article/details/88728683?spm=1001.2014.3001.5501'
url27 = 'https://blog.csdn.net/weixin_43608153/article/details/88808480?spm=1001.2014.3001.5501'
url28 = 'https://blog.csdn.net/weixin_43608153/article/details/88630098?spm=1001.2014.3001.5501'
url29 = 'https://blog.csdn.net/weixin_43608153/article/details/134557719?spm=1001.2014.3001.5501'
#url01 = 'https://m.tb.cn/h.5GXY0Sz?tk=jdSlWk5cArT CZ3460'
# url01 = 'https://h5.m.goofish.com/item?id=755301370265&ut_sk=1.YL6ESJku4kgDACsKcDYRBY9T_12431167_1708233939663.Copy.detail.755301370265.783971192&forceFlush=1&ownerId=ce80d2f2362d8f048dd8033c7ab08c85&un=61fd7e027b47b254132b0f6991806569&share_crt_v=1&un_site=77&spm=a2159r.13376460.0.0&sp_abtk=common_xianyu_commonInfo&sp_tk=amRTbFdrNWNBclQ%3D&cpp=1&shareurl=true&short_name=h.5GXY0Sz&bxsign=scdwVd48u7pv3nqQk5i-8oxbNN3-s0m9EN7kkSqgNRixpkZNwShKutFjWJAtlPcT2Z31oxObUoEZ6Qr5Xqo8LfCHsc9WuG00hztAMProDuStL4HzeMQKvg2isEHhynwxk9s&tk=jdSlWk5cArT%20CZ3460&app=chrome'
Url = [url01, url02, url03, url04, url05, url06, url07, url08, url09, url10, url11, url12, url13, url14, url15, url16,
       url17, url18, url19, url20, url21, url22, url23, url24, url25, url26, url27, url28,url29]
# Url = [url01]


proxy01={'http' : '109.197.188.12:8080'}
proxy02={'http' : '183.247.221.119:30001'}
proxy03={'http' : '61.160.223.141:7302'}
proxy04={'http' : '222.135.31.84:8060'}
proxy05={'http' : '39.175.92.35:30001'}
proxy06={'http' : '39.108.71.54:8088'}
proxy07={'http' : '39.108.71.54:8088'}
proxy08={'http' : '58.220.95.31:10174'}
proxy09={'http' : '59.125.177.31:8080'}
proxy10={'http' : '116.9.163.205:58080'}
proxy11={'http' : '113.214.48.5:8000'}
proxy12={'http' : '183.245.6.48:8080'}
proxy13={'http' : '61.216.185.88:60808'}


#获取代理池
class ProxyPool:
    def __init__(self):
        self.proxies = [proxy01 ,proxy02 ,proxy03 ,proxy04 ,proxy05 ,proxy06 ,proxy07 ,proxy08 ,proxy09 ,proxy10 ,proxy11 ,proxy12 ,proxy13]
    def get_proxies(self):
        url = 'https://www.zdaye.com/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        html = requests.get(url, headers=headers).text
        soup = BeautifulSoup(html, 'lxml')
        trs = soup.find_all('tr')
        for tr in trs[1:]:
            tds = tr.find_all('td')
            proxy = {'ip': tds[1].text, 'port': tds[2].text}
            self.proxies.append(proxy)
    def verify_proxy(self, proxy):
        try:
            ip = str(proxy['ip'])
            port = str(proxy['port'])
            proxies = {'http': 'http://%s:%s' % (ip, port)}
            url = 'http://www.baidu.com'
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
            response = requests.get(url, proxies=proxies, headers=headers, timeout=5)
            if response.status_code == 200:
                print('验证通过：', proxy)
                return True
            else:
                print('连接失败:', proxy)
                return False
        except:
            print('验证失败:', proxy)
            return False
    def check_proxies(self):
        valid_proxies = []
        print('开始检查%d个代理IP...' % len(self.proxies))
        for proxy in self.proxies:
            if self.verify_proxy(proxy):
                valid_proxies.append(proxy)
            time.sleep(1)
        self.proxies = valid_proxies
        print('剩余%d个有效的代理IP！' % len(self.proxies))
    def get_random_proxy(self):
        if not self.proxies:
            self.get_proxies()
            self.check_proxies()
        return random.choice(self.proxies)

if __name__ == '__main__':
    proxy_pool = ProxyPool()
    while True:
        proxy = proxy_pool.get_random_proxy()
        print("proxy:" , proxy)

        url = random.choice(Url)  # 随机随机访问上面的文章
        #proxyy = random.choice(proxy)
        print(url, "*" * 1)
        response = requests.get(url, headers=headers, proxies=proxy).content.decode('utf-8')

        mytree = lxml.etree.HTML(response)
        csdnlist = mytree.xpath('//div[@class="article-list"]/div')
        for i in csdnlist:
            try:
                iUrl = i.xpath('./h4/a/@href')[0]

            except:
                response = requests.get(url=iUrl, headers=headers, proxies=proxy).content.decode('utf-8')
                time.sleep(0.8)

                urll = random.choice(Url)
                response1 = requests.get(url=urll, headers=headers, proxies=proxy).content.decode('utf-8')
                print(response1)
                print(response)
                print(urll, "$" * 30)
                print(iUrl, "@" * 30)

        time.sleep(5)