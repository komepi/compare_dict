from pathlib import Path
import ast

def read_dict_from_file(filename):
    path = Path(filename)
    if path.exists() and path.is_file():
        data = ""
        with open(path, "r") as f:
            lines = f.readlines()
            for l in lines:
                data += l.strip()
    else:
        raise Exception("ファイルが存在しません")
    return data

def to_dict(data):
    if "'" in data:
        m = "'"
    elif '"' in data:
        m = '"'
    else:
        return
    def _(str,num=1):
        return (m*num)+str+(m*num)
    
    def exchange(data,target):
        small = target
        big = target.capitalize()
        data = data.replace(small,_(small)).replace(big,_(big))
        data = data.replace(_(small,2),_(small)).replace(_(big,2),_(big))
        return data
    data = exchange(data,"true")
    data = exchange(data,"false")
    data = exchange(data,"none")
    data = exchange(data,"null")
    data = ast.literal_eval(data)
    return data

class CompareDict():
    def __init__(self):
        self.result = []
    def compare(data1, data2):
        if isinstance(data1,list):
            pass
        elif isinstance(data1,dict):
            pass
            
    def compare_dict(data1,data2):
        for k, v in data1.items():
            if k in data2:
                if type(v) == type(data2.get(k)):
                    if isinstance(v,list):
                        compare_list(v,data2.get(k))
                    elif isinstance(v,dict):
                        compare_dict(v,data2.get(k))
                    else:
                        if v == data2.get(v):
                            pass
                        else:
                            return "not equal value"
                else:
                    return ""
            else:
                return "not exist key k"
    def compare_list(data1,data2):
        for i, d in enumerate(data1):
            if type(d) == type(data2[i]):
                pass
            else:
                return ""
if __name__ == "__main__":
    pass