import json

def read_json():
    fo = open("D:\\report.json","r",encoding="utf-8")
    data = json.load(fo)
    #print(data)
    fo.close()
    list_tests=[]
    list_status =[]
    list_combine =[]
    for i in range(1,12,2):
        test_case=data["tables"][0]["rows"][i]["cols"][0]["nodeValue"]
        test_result=data["tables"][0]["rows"][i]["cols"][1]["nodeValue"]
        list_tests.append(test_case)
        list_status.append(test_result)
    list_combine.append(list_tests)
    list_combine.append(list_status)
    return list_combine
res = read_json()
print(res)