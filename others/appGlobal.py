# -*- coding:utf-8 -*-
#公用函数
__author__ = 'Administrator'

import database
import json
import time
import datetime
import configparser

#获取onu设备的版本信息
def get_version_info():
    version = []
    try:
        config = configparser.ConfigParser()
        config.read('version.conf')
        version = str(config.get('Version', 'version_info')).split(',')
        return version
    except:
        return version

#判断重启是否满足时间条件
def compare_time(begin_time, stop_time):
    try:
        cur_time = datetime.datetime.now().strftime('%H:%M')
        curDate = datetime.datetime.now().strftime('%Y-%m-%d')
        nextDate = (datetime.datetime.now() + datetime.timedelta(days = 1)).strftime('%Y-%m-%d')
        if datetime.datetime.strptime(curDate + ' ' + stop_time, '%Y-%m-%d %H:%M') >= datetime.datetime.strptime(curDate + ' ' + begin_time, '%Y-%m-%d %H:%M'):
            if datetime.datetime.strptime(curDate + ' ' + cur_time, '%Y-%m-%d %H:%M') >= datetime.datetime.strptime(curDate + ' ' + begin_time, '%Y-%m-%d %H:%M'):
                if datetime.datetime.strptime(curDate + ' ' + cur_time, '%Y-%m-%d %H:%M') <= datetime.datetime.strptime(curDate + ' ' + stop_time, '%Y-%m-%d %H:%M'):
                    return True
        else:#跨日期
            #时间段   开始时间 < 当前时间 < 截止时间
            if datetime.datetime.strptime(curDate + ' ' + cur_time, '%Y-%m-%d %H:%M') <= datetime.datetime.strptime(curDate + ' ' + begin_time, '%Y-%m-%d %H:%M'):
                if datetime.datetime.strptime(nextDate + ' ' + cur_time, '%Y-%m-%d %H:%M') >= datetime.datetime.strptime(curDate + ' ' + begin_time, '%Y-%m-%d %H:%M'):
                    if datetime.datetime.strptime(nextDate + ' ' + cur_time, '%Y-%m-%d %H:%M') <= datetime.datetime.strptime(nextDate + ' ' + stop_time, '%Y-%m-%d %H:%M'):
                        return True
                #当前时间 加上一天
            else:#当前时间大于开始时间
                #当前时间小于结束时间  同一天
                if datetime.datetime.strptime(curDate + ' ' + cur_time, '%Y-%m-%d %H:%M') <= datetime.datetime.strptime(curDate + ' ' + stop_time, '%Y-%m-%d %H:%M'):
                    return True
                else:
                    if datetime.datetime.strptime(curDate + ' ' + cur_time, '%Y-%m-%d %H:%M') <= datetime.datetime.strptime(nextDate + ' ' + stop_time, '%Y-%m-%d %H:%M'):
                        return True
        return False
    except:
        return False

#获取正在执行的信息
def get_run_flag():
    iCount = 0
    try:
        data = database.IOMDatabase()
        result = data.ExecSelect('select count(*) as iCount from dutylist', [])
        iCount = result[0]['iCount']
        return iCount
    except:
        return iCount

#获取oltip的数量 bFlag -1:停止,0:未执行,1:正在执行,2:执行完成
def get_olt_count():
    iCount = 0
    try:
        data = database.IOMDatabase() #查询未执行的,以及没执行完的
        result = data.ExecSelect('select * from duty where bFlag in (0,1) and begin_date<=%s and stop_date>=%s', [datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%Y-%m-%d')])
        if len(result) > 0:
            for i in range(0, len(result)):
                #判断时间
                if compare_time(result[i]['begin_time'], result[i]['stop_time']):
                    iCount += len(json.loads(result[i]['olt_list']))
        return iCount
    except:
        return iCount

#获取任务IP列表 第num开始,iLimit结束
def get_olt_list(num, iLimit):
    retParam = []
    iBegin = 0
    iCnt = 0
    try:
        data = database.IOMDatabase()
        #0:没有执行 1:正在执行  -1：停止任务  2:完成任务 (1:可能上次没有执行完,所有状态为1)
        result = data.ExecSelect('select olt_list,duty_id,begin_time,stop_time from duty where bFlag in(0,1) and begin_date<=%s and stop_date>=%s order by duty_id', [datetime.datetime.now().strftime('%Y-%m-%d'), datetime.datetime.now().strftime('%Y-%m-%d')])
        if len(result) > 0:
            for i in range(0, len(result)):
                if compare_time(result[i]['begin_time'], result[i]['stop_time']):
                    iCnt += len(json.loads(result[i]['olt_list']))
                    if iCnt < num:
                        continue
                    elif iCnt > (num + iLimit):
                        break
                    else:
                        if len(retParam) < iLimit:
                            for k in range(0, len(json.loads(result[i]['olt_list']))):
                                iBegin += 1
                                if iBegin < num:
                                    continue
                                elif iBegin >= iLimit:
                                    break
                                else:
                                    oltip = json.loads(result[i]['olt_list'])[k]
                                    #判断 ip 已经在运行
                                    retolt = data.ExecSelect('select * from oltlist where pon_ip=%s', [oltip])
                                    if len(retolt) > 0:
                                            tmp = {}
                                            tmp['duty_id'] = result[i]['duty_id']
                                            tmp['begin_time'] = result[i]['begin_time']
                                            tmp['stop_time'] = result[i]['stop_time']
                                            tmp['pon_ip'] = retolt[0]['pon_ip']
                                            tmp['pon_type'] = retolt[0]['pon_type']
                                            tmp['log_user'] = retolt[0]['log_user']
                                            tmp['log_pass'] = retolt[0]['log_pass']
                                            flaglist = data.ExecSelect('select count(*) as iCount from dutylist where duty_id=%s and olt_ip=%s', [result[i]['duty_id'], retolt[0]['pon_ip']])
                                            if flaglist[0]['iCount'] < 1: #修改任务的状态,标示已经在执行中
                                                data.ExecInsert('insert into dutylist(duty_id, olt_ip) values(%s,%s)', [result[i]['duty_id'], retolt[0]['pon_ip']])
                                                data.ExecUpdate('update duty set bFlag=%s where duty_id=%s', ['1', result[i]['duty_id']]) #开始运行
                                                retParam.append(tmp)
        return retParam
    except:
        return retParam

#华为使用另外一个密码登录
def huaweilogin(tn, prompt):
    #用户名
    if prompt.find('>>User name:') >= 0:
        tn.write(('root').encode('UTF-8') + b'\n')
    else:
        return False

    #输入密码
    try:
        while True:
            ret = tn.read_very_eager()
            if (ret.decode('utf-8')).find('>>User password:') >= 0:
                tn.write(('admin2013').encode('UTF-8') + b'\n')
                #退出循环
                break
            else:
                time.sleep(1)
    except:
        return False

    return True

#中兴使用另外一个账号登录
def ztelogin(tn, prompt):
    #用户名
    if prompt.find('Username:') >= 0:
        tn.write(('zte').encode('UTF-8') + b'\n')
    else:
        return False

    #输入密码
    try:
        while True:
            tmp = tn.read_very_eager()
            if len(tmp.decode('utf-8')) > 0:
                if (tmp.decode('utf-8')).find('Password:') >= 0:
                    tn.write(('zte2013').encode('UTF-8') + b'\n')
                    #退出循环
                    break
            else:
                time.sleep(1)
    except:
        return False

    return True

#初始化日志
def initlog(orderCode, CommType):
    #命令分类  1:新增 3:扩容 6:退网 9:ONU命令二
    arrNode = {'COMMAND': [], 'COMMTYPE': CommType, 'LOGIN': [], 'RESULT': '0'}
    try:
        data = database.IOMDatabase()
        result = data.ExecSelect('select * from tasklog where ordercode=%s', [orderCode])
        if len(result) > 0: #日志存在
            if CommType == '6' or CommType == '1' or CommType == '3':
                if result[0]['runlog'] is None:
                    return arrNode
                else:
                    if CommType == '6' or CommType == '1' or CommType == '3':
                        return json.loads(result[0]['runlog'])
            else:
                if result[0]['onulog'] is None:
                    arrNode = {'COMMAND': [], 'COMMTYPE': CommType, 'LOGIN': [], 'RESULT': '0', 'VLANLogin': [], 'VLAN': [], 'VLANRESULT': '0'}
                    return arrNode
                else:
                    return json.loads(result[0]['onulog'])
        else:
            return arrNode
    except:
        return arrNode

#过滤telnet中的字符
def bytes_to_string(b):
    tmp = []
    iCount = 1
    bStart = False
    for i in range(0, len(b)):
        if bStart:
            if iCount < 4:
                iCount += 1
            else:
                bStart = False
                iCount = 1
            continue
        else:
            if b[i] == 27:
                bStart = True
                continue
        if b[i] >= 0 and b[i] <= 127:
            tmp.append(b[i])
    return (bytes(tmp))

#增加日志 订单编码 订单主题 服务 运行日志
def addlog(orderCode, orderTitle, serviceName, runLog, devicetype, commtype):
    #commtype 1:新增 OLT命令 2:新增 ONU命令  3:扩容 OLT命令 4:ONU命令  6:退网
    try:
        data = database.IOMDatabase()
        result = data.ExecSelect('select * from tasklog where ordercode=%s', [orderCode])

        if len(result) > 0:
            sql = ''
            if commtype == '1' or commtype == '3' or commtype == '6':#新增OLT命令,#退网命令,#扩容OLT命令
                sql = 'update tasklog set runlog=%s,orderTitle=%s,serviceName=%s where ordercode=%s'
            elif commtype == '2' or commtype == '4':#新增ONU命令,#扩容ONU命令
                sql = 'update tasklog set onulog=%s,orderTitle=%s,serviceName=%s where ordercode=%s'
            param = [json.dumps(runLog), orderTitle, serviceName, orderCode]
            data.ExecUpdate(sql, param)
        else:
            sql = ''
            if commtype == '1':#工单入网OLT命令
                sql = 'insert into tasklog(orderCode,orderTitle,serviceName,runlog,createtime,devicetype, commtype) values(%s,%s,%s,%s,%s,%s,%s)'
                param = [orderCode, orderTitle, serviceName, json.dumps(runLog), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), devicetype, '1']
                data.ExecInsert(sql, param)
            elif commtype == '2':#工单入网ONU命令
                sql = 'insert into tasklog(orderCode,orderTitle,serviceName,onulog,createtime,devicetype, commtype) values(%s,%s,%s,%s,%s,%s,%s)'
                param = [orderCode, orderTitle, serviceName, json.dumps(runLog), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), devicetype, '1']
                data.ExecInsert(sql, param)
            elif commtype == '3':#工单扩容
                sql = 'insert into tasklog(orderCode,orderTitle,serviceName,runlog,createtime,devicetype, commtype) values(%s,%s,%s,%s,%s,%s,%s)'
                param = [orderCode, orderTitle, serviceName, json.dumps(runLog), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), devicetype, '3']
                data.ExecInsert(sql, param)
            elif commtype == '4':#工单扩容
                sql = 'insert into tasklog(orderCode,orderTitle,serviceName,onulog,createtime,devicetype, commtype) values(%s,%s,%s,%s,%s,%s,%s)'
                param = [orderCode, orderTitle, serviceName, json.dumps(runLog), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), devicetype, '3']
                data.ExecInsert(sql, param)
            elif commtype == '6':#退网
                sql = 'insert into tasklog(orderCode,orderTitle,serviceName,runlog,createtime,devicetype, commtype) values(%s,%s,%s,%s,%s,%s,%s)'
                param = [orderCode, orderTitle, serviceName, json.dumps(runLog), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), devicetype, '6']
                data.ExecInsert(sql, param)
            else:
                sql = 'insert into tasklog(orderCode,orderTitle,serviceName,runlog,createtime,devicetype, commtype) values(%s,%s,%s,%s,%s,%s,%s)'
                param = [orderCode, orderTitle, serviceName, json.dumps(runLog), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), devicetype, '0']
                data.ExecInsert(sql, param)
    except:
        return


#判断有中文
def ContainCh(b):
    bFind = False
    for i in range(0, len(b)):
        if b[i] > 127:
            bFind = True
            break
    return bFind

#判断loid已经存在
def get_loid_info(loid):
    try:
        data = database.IOMDatabase()
        result = data.ExecSelect('select * from dutyterm where loid=%s', [loid])
        if len(result) > 0:
            return True
        else:
            return False
    except:
        return False

#获取任务执行时间
def set_task_run_time(start_time, duty_id):
    try:
        data = database.IOMDatabase()
        result = data.ExecSelect('select * from duty where duty_id=%s', [duty_id])
        if len(result) > 0:
            if result[0]['run_time'] is None or result[0]['run_time'] == '':
                stop_run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data.ExecUpdate('update duty set run_time=%s where duty_id=%s', [stop_run_time - start_time, duty_id])
            else:
                stop_run_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data.ExecUpdate('update duty set run_time=%s where duty_id=%s', [result[0]['run_time'] + '|' + str(stop_run_time - start_time), duty_id])
    except:
        return

#保存e8-c重启的日志
def pon_info_save(ponParam, duty_id, olt_ip):
    try:
        data = database.IOMDatabase()
        result = data.ExecSelect('select * from dutylog where duty_id=%s and olt_ip=%s', [duty_id, olt_ip])
        if len(result) > 0:
            data.ExecUpdate('update dutylog set pon=%s where duty_id=%s and olt_ip=%s', [ponParam, duty_id, olt_ip])
        else:
            data.ExecInsert('insert into dutylog(duty_id, olt_ip, pon) values(%s,%s,%s)', [duty_id, olt_ip, ponParam])
    except:
        return

#所有的重启参数的保存
def all_info_save(duty_id, olt_ip, ponParam):
    try:
        data = database.IOMDatabase()
        result = data.ExecSelect('select * from dutylog where duty_id=%s and olt_ip=%s', [duty_id, olt_ip])
        if len(result) > 0:
            data.ExecUpdate('update dutylog set param_detail=%s where duty_id=%s and olt_ip=%s', [json.dumps(ponParam), duty_id, olt_ip])
        else:
            data.ExecInsert('insert into dutylog(duty_id, olt_ip, param_detail) values(%s,%s,%s)', [duty_id, olt_ip, json.dumps(ponParam)])
    except:
        return

#初始化e8-c的日志
def initec8log(duty_id, olt_ip):
    #命令分类  1:新增 3:扩容 6:退网 9:ONU命令二
    arrNode = {'COMMAND': []}
    try:
        data = database.IOMDatabase()
        result = data.ExecSelect('select * from dutylog where duty_id=%s and olt_ip=%s', [duty_id, olt_ip])
        if len(result) > 0: #日志存在
            return json.loads(result[0]['param_detail'])
        return arrNode
    except:
        return arrNode

def getPortCount(Info):
    print(Info)
    return True
