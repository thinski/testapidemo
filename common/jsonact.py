#coding=utf-8
import json
import os.path

class OperationJson(object):
    def __init__(self):
        self.data = self.read_data()

    # 读取Json文件
    def read_data(self):
        test_filepath = os.path.dirname(os.path.abspath('.')) + '/testapidemo/testdata/'
        testfilename= test_filepath+'test.json'
        #data = [json.loads(line.replace("'",'"'))for line in open(testfilename,'r')]
        with open(testfilename,'rb') as fp:
            data = json.load(fp)
        return data

    # 根据关键字获取数据
    def get_data(self, id):
        return self.data[id]