# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import urllib
import http.cookiejar
import urllib.request
import urllib.parse
import re
import json
import database
from bs4 import BeautifulSoup
import appGlobal
import time
import bs4
import xml.etree.ElementTree as eTree


class GetHtml:
    header = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET4.0C; .NET4.0E)',
        'Connection': 'keep-alive'}
    cookie = None

    EPON_User = ''
    EPON_Pass = ''

    def __init__(self):
        # cookie设置
        self.cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))
        urllib.request.install_opener(opener)
        data = database.Database()

        result = data.ExecSelect('select * from loginInfo', [])
        if len(result) > 0:
            login_info = json.loads(result[0]['loginInfo'])
            self.User = login_info['EPON']['account']
            self.Pass = login_info['EPON']['password']

    def login(self):
        bLogin = False
        #登录失败判断
        count_i = 0
        while count_i < 5:
            try:
                req = urllib.request.Request(
                    url='http://jjjjj/login.aspx',
                    data=bytes(param, 'utf-8'),
                    headers=self.header
                )
                result = urllib.request.urlopen(req)
                ret = (result.read()).decode('gb2312')
                soup = BeautifulSoup(''.join(ret))
                if red_str.find('欢迎') < 0:
                    count_i += 1
                else:
                    bLogin = True
                    break
            except Except as er:
                count_i += 1
                time.sleep(30)
                print('登录失败!' + er)

        #根据true或者false判断下一步
        if bLogin:
            return True
        else:
            appGlobal.add_error('EPON登录失败!', 1)
            return False

    # 登录
    def another_login(self, work_id):
        return_data = {'status': 0, 'params': {}}

        bLogin = True
        iLogin = 5
        while iLogin > 0:
            bLogin = True
            try:
                result = urllib.request.urlopen(req)
                tmpStr = (result.read()).decode('utf-8')

                #获取area_id
                root = etree.fromstring(tmpStr)
                area_id = root[0].attrib['area_id']
                time.sleep(1)

                #获取验证码
                captcha = checkAuthCode.AuthCode()

                if redStr.find('登录成功') < 0:
                    bLogin = False
                else:
                    break
                iLogin -= 1
            except Exception as er:
                if iLogin < 1:
                    bLogin = False


        if bLogin:
            bShow = True
            iQuery = 5
            while iQuery > 0:
                if bShow:
                    reqMac = urllib.request.Request(
                        url='http://js.resb.jsoss.net/resweb/mainFrame.spr?method=basicframe',
                        headers=self.header
                    )
                    try:
                        resultM = urllib.request.urlopen(reqMac)
                        tmpStr = (resultM.read()).decode('utf-8')
                        if tmpStr.find('退出') >= 0 and tmpStr.find('更改密码') >= 0:
                            # 登录成功
                            bShow = False
                            break
                        else:
                            time.sleep(1)
                            iQuery -= 1
                    except:
                        iQuery -= 1

            # 登录成功
            if not bShow:
                # 查询
                timeParam = str(int(time.time()*1000))
                 #发起请求
                req1 = urllib.request.Request()
                result1 = urllib.request.urlopen(req1)
                ret = (result1.read()).decode('utf-8')
                if ret.find('忘记密码') >= 0:
                    #登录失败
                    time.sleep(1)
                    bRet = self.validLogin()
                    if not bRet:
                        return return_data
                soup = BeautifulSoup(ret)
                for row in soup.find('rows').children:
                    cells = row('cell')
                    #进行下一步的查询
                    if '服务定单已生成变更单' == cells[9].string:
                    # if True:
                        return self.search_data(cells[0].string, work_id, cells[1].string)
                return return_data
            else:
                # 登录失败
                appGlobal.add_error('登录OSS系统失败!', 1)
                return return_data

    def care(self):
        work_info = r.text.replace('%u', "\\u").encode('utf-8').decode('unicode_escape')
        ord_txt = urllib.parse.unquote(work_info).split(',')
        time_cr = ord_txt[2]
        if len(ord_txt) < 10:
            continue
        bFind = False
        iFlag = 0
        net_element = 'GXCYW'
        order_type = ''
        business_type = ''

        for i in range(0, len(ord_txt)):
            if bFind:
                if ord_txt[i].isdigit():
                    iFlag = i
                    break
            else:
                bFind = self.search_work_flag(ord_txt[i])
                if bFind:
                    order_type = ord_txt[i]
                    business_type = self.get_business_type(ord_txt[i])

    def search_work_flag(self, ord_txt):
        if ord_txt.find('服务信息变动') >= 0:
            return True
        elif ord_txt.find('移机') >= 0:
            return True

    def get_business_type(self, ord_txt):
        if ord_txt.find('服务信息变动') >= 0 or ord_txt.find('移机') >= 0 or ord_txt.find('割接改局向') >= 0:
            return '移机'
        else:
            return ord_txt
        data = database.INASDatabase()
        result = data.ExecSelect('select * from workorder where workID=%s and deleted=0', [work_id])
        print('----1----')
        if len(result) > 0 and result[0]['state'] != 8:
            ''

    def getHTMLText(self, url):
        try:
            r = requests.get(url)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return ""

    def getList(self, lst, URL):
        html = getHTMLText(URL)
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find_all('a')
        for i in a:
            try:
                href = i.attrs['href']
                lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
            except:
                continue


    def getStockInfo(self, lst, stockURL, fpath):
        result_data = {'status': 0, 'params': {}, 'desc': '成功'}
        for stock in lst:
            url = stockURL + stock + ".html"
            html = getHTMLText(url)
            try:
                if html == "":
                    continue
                infoDict = {}
                soup = BeautifulSoup(html, 'html.parser')
                stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

                name = stockInfo.find_all(attrs={'class': 'bets-name'})[0]
                infoDict.update({'': name.text.split()[0]})

                keyList = stockInfo.find_all('dt')
                valueList = stockInfo.find_all('dd')
                for i in range(len(keyList)):
                    key = keyList[i].text
                    val = valueList[i].text
                    infoDict[key] = val

                with open(fpath, 'a', encoding='utf-8') as f:
                    f.write(str(infoDict) + '\n')
            except:
                traceback.print_exc()
                continue