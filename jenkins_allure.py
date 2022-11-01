#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
# -*- coding: utf-8 -*-

import nose
class TestClass1():

    def setUp(self):
        print u"setUp1"

    def tearDown(self):
        print u"tearDown2"

    @nose.allure.severity("hard")
    def test11(self):
        print u"test11"
        #pass

    @nose.allure.severity("hard")
    def test12(self):
        print u"test12"
        #pass

class TestClass2():

    def setUp(self):
        print u"setUp2"
    def tearDown(self):
        print u"tearDown2"
    def test21(self):
        print "test21"
    def test22(self):
        print "tt22"


# create xml_report:
# D:\software\Python2714\py2script\test_demo01\nose_test>python2 -m nose -v -s nose_t1.py --with-allure --logdir=result_xml
# xml change to html
#allure generate xml文件的目录 -o html需要保存的路径
#问题：生成的html报告数据为空，
#原因：要开启服务才可以查看，命令如下：allure report open
#https://blog.csdn.net/chenfei_5201213/article/details/80982929
#解决方法1：使用pycharm→浏览器打开（firefox存在问题，都是loading，无法加载数据）
#解决方法2：https://www.cnblogs.com/ivywoon/p/11990946.html
#使用Microsoft Edge浏览器打开即可