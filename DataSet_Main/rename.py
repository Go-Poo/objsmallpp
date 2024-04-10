import os
import re
import json

# specify the directory you want to change the files in
directory = 'C:/Users/17048/objsmallpp/DataSet_Main/train/annotations/'

for filename in os.listdir(directory):
    # print(filename)
    data =""
    if filename.endswith(".json"):
        with open(directory+filename, 'r') as f:
            print(directory+filename)
            data = json.load(f)
            print(data["id"])
            print(data["label"][0]["x"]/100)
            print(data["label"][0]["y"]/100)
            print(data["label"][0]["width"]/100)
            print(data["label"][0]["height"]/100)
        filename = filename[0:-4]+"txt"
        with open(directory+filename, "w") as f:
            f.write("0 " + str(data["label"][0]["x"]/100.0) + " " + str(data["label"][0]["y"]/100.0) + " " + str(data["label"][0]["width"]/100.0) + " " + str(data["label"][0]["height"]/100.0))