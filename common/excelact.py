#coding=utf-8
import xlwt
import os.path
import time
from common.logger import Logger

logger = Logger(logger="excel").getlog()

class Operationexcel(object):
    def create_report(self,testreports):
        workbook = xlwt.Workbook(encoding='ascii')
        worksheet = workbook.add_sheet('APItestreport')
        i = 0
        for key in testreports[0]:
            worksheet.write(0,i,key)
            i=i+1
        for j in range(1,len(testreports)):
            col=0
            for key1 in testreports[j]:
                logger.info("testreport[j][key1]%s"%testreports[j][key1])
                worksheet.write(j,col,str(testreports[j][key1]))
                col=col+1



        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        reportpath = os.path.dirname(os.path.abspath('.')) + '/testapidemo/report/'
        reportname = reportpath+rq+'.xls'
        workbook.save(reportname)