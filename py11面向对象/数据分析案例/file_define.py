# 和文件相关的类定义
# 定义一个抽象类，确定要实现哪些功能，做顶层设计
import json

from data_define import Record
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件数据，将读到的每一条数据都转换为Record数据，将它们都封装到list中返回"""
        pass

class csvFileReader(FileReader):
    def __init__(self,path):
        self.path = path        # 定义成员变量记录文件路径

    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            line.strip()        # 消除每一行中的/n
            line_list = line.split(",")
            record = Record(line_list[0],line_list[1],int(line_list[2]),line_list[3])
            record_list.append(record)
        f.close()
        return record_list

class jsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path        # 定义成员变量记录文件路径

    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list = []
        for line in f.readlines():
            ld:dict = json.loads(line)
            record = Record(ld["date"],ld["order_id"],int(ld["money"]),ld["province"])
            record_list.append(record)
        f.close()
        return record_list
