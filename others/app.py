# -*- coding: utf8 -*- #
# '''
# author:谢晓晓
# '''

import time
import getHtml

if __name__ == '__main__':
    while True:
        print('开始')
        task = getHtml.GetHtml()
        login = task.login()
        if not login:
            continue
        task.getList()
        # 销毁对象
        del task
        print('结束')
        time.sleep(60)