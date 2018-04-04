#coding=utf-8
import os
from common.jsonact import OperationJson
import json
import requests
from common.excelact import Operationexcel
from common.logger import Logger
import sys
import time

logger = Logger(logger="test").getlog()
test_reports = []

ojson = OperationJson()
testcases = ojson.read_data()
for key in testcases:
    logger.info("now test %s" %key)
    start_time = time.time()
    case = testcases[key]
    url = case["url"]
    hope_result = case['assert']
    methord = case["methord"]
    data = case["parama"]
    test_report = {
        "case_id":case["id"],
        "t_name":case["name"],
        "methord":methord,
        "url":url,
        "parama":data,
        "hope_result":hope_result,
        "actual_result":[],
        "test_result":""
    }
    try:
        if methord == "post":

            r = requests.post(url,data=data)
            logger.info("now test post url is %s" %url)
            logger.info("now test post %s" %data)
            rsp = r.json()
            logger.info(rsp)
            s = True
            for k in hope_result:
                ar = str(k)+":"+str(rsp[k])
                test_report["actual_result"].append(ar)
                if type(hope_result[k]) == type(''):
                    if hope_result[k] in rsp[k]:
                        s = s&True
                    else:
                        s=s&False
                else:
                    if hope_result[k] == rsp[k]:
                        s =s&True
                    else:
                        s= s&False
            if s:
                test_report["test_result"]="PASS"
            else:
                test_report["test_result"] = "Fail"

        elif methord == 'get':
            r = requests.get(url,data=json.dumps(data))
            rsp = r.json()
            s = True
            for k in hope_result:
                ar = str(k) + ":" + str(rsp[k])
                test_report["actual_result"].append(ar)
                if type(hope_result[k]) == type(''):
                    if hope_result[k] in rsp[k]:
                        s = s & True
                    else:
                        s = s & False
                else:
                    if hope_result[k] == rsp[k]:
                        s = s & True
                    else:
                        s = s & False
            if s:
                test_report["test_result"] = "PASS"
            else:
                test_report["test_result"] = "Fail"

        else:
            print(u'暂不支持该请求方式')
        logger.info("testreport is:%s"%test_report)
        test_reports.append(test_report)
        end_time = time.time()
        str_time = u'当前执行用例：'+key+"_"*4+'用例执行时间：'+str(end_time-start_time)+'s'
        logger.info(str_time)
    except:
        error_msg = sys.exc_info()
        logger.info(error_msg)
        continue

excel = Operationexcel()
excel.create_report(test_reports)






