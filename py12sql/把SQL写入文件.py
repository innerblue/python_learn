import json


class WriterJson:
    def __init__(self,datas:tuple,path):
        self.datas = datas
        self.path = path
    def Writer(self):
        data_list = []
        for data in self.datas:
            data_dict = {"date": data[0], "order_id": data[1], "money": data[2], "province": data[3]}
            data_list.append(data_dict)

        jsondata = json.dumps(data_list,ensure_ascii=False)
        f = open(self.path,"w",encoding="UTF-8")
        f.write(jsondata)
        f.close()
