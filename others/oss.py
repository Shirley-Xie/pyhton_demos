# -*- coding:utf-8 -*-
# inas
import checkAuthCode
import urllib,re
import http.cookiejar
import urllib.request
import urllib.parse
import time
from bs4 import BeautifulSoup
import xml.etree.ElementTree as etree

class LoginOSS:
    #请求设置头
    header = {
        'Mozilla/4.0': '(compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.879897)',
        'Connection': 'keep-alive'
    }
    cookie = None
    OSS_User = ''
    OSS_Pass = ''

    def __init__(self, oss_pass, oss_user):
        #cookie设置
        self.cookie = http.cookiejar.CookieJar()
        opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookie))
        urllib.request.install_opener(opener)
        self.OSS_User = oss_user
        self.OSS_Pass = oss_pass

    #登录
    def login(self, id):
        bLogin = True
        iLogin = 5
        while iLogin > 0:
            bLogin = True
            param = 'username=' + self.OSS_User
            #发起请求 获取地区编码和地区名称  发送参数   用户id
            req = urllib.request.Request(
                url='htttition.htm',
                data=bytes(param, 'utf-8'),
                headers=self.header
            )
            try:
                result = urllib.request.urlopen(req)
                tmpStr = (result.read()).decode('utf-8')

                #获取area_id
                root = etree.fromstring(tmpStr)
                print(root)
                #.attrib.get('area_id')
                area_id = root[0].attrib['area_id']
                area_name = root[0].attrib['name']

                time.sleep(1)

                #获取验证码
                captcha = checkAuthCode.AuthCode()

                #保存用户
                req = urllib.request.Request(
                    url='http:/user.htm',
                    data=bytes('username=' + self.OSS_User + '&password=&partitionid=15&partitionName=%E6%97%A0%E9%94%A1', 'utf-8'),
                    headers=self.header
                )
                result = urllib.request.urlopen(req)
                tmpStr = (result.read()).decode('utf-8')

                time.sleep(1)

                param = 'username=' + self.OSS_User
                #发起请求 获取地区编码和地区名称  发送参数   用户id
                req = urllib.request.Request(
                    url='http://js.cas.jsoss.net/sso/partition.htm',
                    data=bytes(param, 'utf-8'),
                    headers=self.header
                )
                result = urllib.request.urlopen(req)
                tmpStr = (result.read()).decode('utf-8')

                time.sleep(1)

                param = 'userName=' + self.OSS_User + '&partitionid=0'
                req = urllib.request.Request(
                    url='http://htm',
                    data=bytes(param, 'utf-8'),
                    headers=self.header
                )
                result = urllib.request.urlopen(req)
                tmpstr = (result.read()).decode('utf-8')

                time.sleep(1)

                param = 'userName=' + self.OSS_User + '&partitionid=15'
                req = urllib.request.Request(
                    url='htthtm',
                    data=bytes(param, 'utf-8'),
                    headers=self.header
                )
                result = urllib.request.urlopen(req)
                tmpstr = (result.read()).decode('utf-8')
                time.sleep(1)

                param = 'passwordSwitch=' + area_id
                req = urllib.request.Request(
                    url='htt.htm',
                    data=bytes(param, 'utf-8'),
                    headers=self.header
                )
                result = urllib.request.urlopen(req)
                tmpStr = (result.read()).decode('utf-8')

                time.sleep(1)

                try:
                    #登录
                    req = urllib.request.Request(
                        url='http://js.cas.jsoss.net/sso/login',
                        headers=self.header
                    )
                    result = urllib.request.urlopen(req)
                    tmpStr = (result.read()).decode('utf-8')

                    #获取lt
                    soup = BeautifulSoup(''.join(tmpStr))
                    inputTag = soup.findAll(attrs={"name": "lt"})
                    lt = inputTag[0]['value']

                    param = 'clientMac=&passwordSwitch=15&webpassword=&username=' + self.OSS_User + '&password=' + self.encode64(self.OSS_Pass) + '&partitionId=15' + '&captcha=' + captcha + '&lt=' + lt + '&_eventId=submit'
                    #cparam = 'clientMac=&passwordSwitch=15&webpassword=&username=' + self.OSS_User + '&password=MTIxMjEy&partitionId=15' + '&captcha=' + captcha + '&lt=' + lt + '&_eventId=submit'
                    req = urllib.request.Request(
                        url='http://js.cas.jsoss.net/sso/login?service=http%3A%2F%2Fjs.resb.jsoss.net%3A9080%2Fresweb%2FmainFrame.spr%3Fmethod%3DmainView',
                        data=bytes(param, 'utf-8'),
                        headers=self.header
                    )
                    result = urllib.request.urlopen(req)
                    redStr = (result.read()).decode('utf-8')
                    #print(redStr)

                    if (redStr.find('登录成功') < 0):
                        bLogin = False
                    else:
                        break
                    iLogin -= 1
                except Exception as er:
                    print(er.args)
                    if iLogin < 1:
                        return '-1'
            except Exception as er:
                print(er.args)
                if iLogin < 1:
                    return ''

        if bLogin:
            bShow = True
            iQuery = 5
            while iQuery > 0:
                if bShow:
                    reqMac = urllib.request.Request(
                        url='http://jet',
                        headers=self.header
                    )
                    try:
                        resultM = urllib.request.urlopen(reqMac)
                        tmpStr = (resultM.read()).decode('utf-8')
                        #print(tmpStr)
                        if tmpStr.find('退出') >= 0 and tmpStr.find('更改密码') >= 0:
                            #登录成功
                            bShow = False
                        else:
                            time.sleep(1)
                            iQuery -= 1
                    except:
                        if iQuery < 0:
                            return '-1'
                        else:
                            iQuery -= 1
                else:
                    try:
                        #查询
                        reqParam = '<?xml irelationId><ipropertyId>23033</ipropertyId><iqueryPropertyId>94481</iqueryPropertyId><iresTypeId>0</iresTypeId>' \
                            ightId>0</irightId><nrelation/><nrelationshipType/><nlinkName/><nvalue/><scondition>=</scondition>' \
                                        '<sifrunning_val>1</sifrunning_val><ndefultValue/><ssearchInfo></ssearchInfo><npropSpecId/><nresRelationVo/>' \
                                 '</oItem>' \
                                 '</Param><Param type=\'i\'>11861</Param><Param type=\'i\'>-3</Param><Param type=\'i\'>20</Param></Function>'
                         #发起请求
                        req1 = urllib.request.Request(
                            url='http://js.resb.jsoss.net/resweb/component/busiFacade.spr?onTypeFilterExt=dynamicCommonOperation&resTypeId=11861&method=query',
                            data=bytes(reqParam, 'utf-8'),
                            headers={'Content-Type': 'text/xml'}
                        )

                        result1 = urllib.request.urlopen(req1)
                        ret = (result1.read()).decode('utf-8')

                        if ret.find('忘记密码') >= 0:
                            #登录失败
                            time.sleep(1)
                            bRet = self.validLogin()
                            if bRet:
                                continue
                            else:
                                return '-1'
                        print(ret)

                        root = etree.fromstring(ret)
                        nodes = root[0].text

                        decode = json.loads(nodes)

                        return decode.get('rows')[0]['data'][12]
                    except Exception as er:
                        print(er.args)
                        if iQuery < 0:
                            return '-1'
                        else:
                            iQuery -= 1
            else:
                return '-1'
        else:
            return '-1'