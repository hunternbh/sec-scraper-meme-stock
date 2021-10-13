#import pandas as pd
import glob
import re
import os
from bs4 import BeautifulSoup

cwd = os.getcwd()

data = glob.glob(cwd+"\\1-data\\*\\*.txt")
newpath = cwd + "\\2-cleaned-html\\"

# PART 1 - clean the html markup
for path in data:
    with open(path, encoding="utf-8") as myfile:
        path = path.split("\\")
        dir_path = path[-2]
        file_path = path[-2] + "\\" + path[-1]
        dir_path = newpath + dir_path
        file_path = newpath + file_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        item = myfile.read()
        try:
            item = BeautifulSoup(item)
            file_txt = open(file_path,'w', encoding="utf-8")
            file_txt.write(item.get_text())
            file_txt.close()
        except:
            continue

# PART 2 - clean the rubbish text - using signature as a stopword
data = glob.glob(cwd+"\\2-cleaned-html\\*\\*.txt")
newpath = cwd + "\\3-cleaned-signature\\"

for path in data:
    with open(path, encoding="utf-8") as myfile:
        path = path.split("\\")
        dir_path = path[-2]
        file_path = path[-2] + "\\" + path[-1]
        dir_path = newpath + dir_path
        file_path = newpath + file_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        
        item = myfile.read()
        try:
            item = re.split("signature",item,flags=re.IGNORECASE)
            file_txt = open(file_path,'w', encoding="utf-8")
            for index,i in enumerate(item):
                if index == len(item)-1:
                    continue
                else:
                    file_txt.write(i)
            file_txt.close()
        except:
            continue

#Part 3 - data_clean using stop words

#import pandas as pd
import glob
import re
import os
from bs4 import BeautifulSoup

# the goal of 8K analysis is to get the disclosure items - by eliminating signatures preveiously, we only
# the items.
cwd = os.getcwd()

data = glob.glob(cwd+"\\3-cleaned-signature\\*\\*.txt")
newpath = cwd + "\\4-cleaned-final\\"

for path in data:
    with open(path, encoding="utf-8") as myfile:
        path = path.split("\\")
        dir_path = path[-2]
        file_path = path[-2] + "\\" + path[-1]
        dir_path = newpath + dir_path
        file_path = newpath + file_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        item = myfile.read()
        print(file_path)
        if "8-K" in file_path:
            # split_at_htm = re.split("htm",item)
            # split_at_htm = " ".join(split_at_htm[1:])

            # split_item = (re.split(START_8K, item, flags=re.IGNORECASE))[1]
            # split_item = re.split("item+\s+\d",split_item, flags=re.IGNORECASE)
            file_txt = open(file_path,'w',encoding="utf-8")
            file_txt.write(item)
            file_txt.close()
        if "10-K" in file_path:
            MDA = "MD&A"
            RF = "RISK FACTORS"
            try:
                split_item = re.split(r"item\s*\n*\r*\t*1a\.*\s*\n*\r*\t*\-*\–*\s*risk", item, flags=re.IGNORECASE)[2]
                split_item = (re.split(r"item\s*\n*\r*\t*1b\.*\s*\n*\r*\t*\-*\–*\s*unresolved", split_item, flags=re.IGNORECASE))[0]
            except:
                MDA = "ERROR"
            try:
                split_item2 = (re.split(r"item\s*\n*\r*\t*7\.*\s*\n*\r*\t*\-*\–*\s*management", item, flags=re.IGNORECASE))[2]
                split_item2 = (re.split(r"item\s*\n*\r*\t*7a\.*\s*\n*\r*\t*\-*\–*\s*quantitative", split_item2, flags=re.IGNORECASE))[0]
            except:
                RF = "ERROR"
            file_txt = open(file_path.split(".txt")[0]+" "+MDA+" "+RF+".txt",'w',encoding="utf-8")
            file_txt.write(MDA)
            file_txt.write(split_item)
            file_txt.write(RF)
            file_txt.write(split_item2)
            file_txt.close()
        if "10-Q" in file_path:
            MDA = "MD&A"
            RF = "RISK FACTORS"
            try:
                split_item = re.split(r"item\s*\n*\r*\t*2\.*\s*\n*\r*\t*\-*\–*\s*management", item, flags=re.IGNORECASE)[2]
                split_item = (re.split(r"item\s*\n*\r*\t*3\.*\s*\n*\r*\t*\-*\–*\s*quantitative", split_item, flags=re.IGNORECASE))[0]
            except:
                MDA = "ERROR"
            try:
                split_item2 = (re.split(r"item\s*\n*\r*\t*1a\.*\s*\n*\r*\t*\-*\–*\s*risk", item, flags=re.IGNORECASE))[2]
                split_item2 = (re.split(r"item\s*\n*\r*\t*2\.*\s*\n*\r*\t*\-*\–*\s*unregistered", split_item2, flags=re.IGNORECASE))[0]
            except:
                RF = "ERROR"
            file_txt = open(file_path.split(".txt")[0]+" "+MDA+" "+RF+".txt",'w',encoding="utf-8")
            file_txt.write(MDA)
            file_txt.write(split_item)
            file_txt.write(RF)
            file_txt.write(split_item2)
            file_txt.close()
#Deprecated

# START_8K = "If an emerging growth company"

# START_10Q = "2.Management"
# STOP_10Q = "item3.Quantitative and Qualitative Disclosures about Market Risk"

# START_10Q_2 = "1A.Risk Factors"
# STOP_10Q_2 ="2.Unregistered Sales of Equity Securities and Use of Proceeds"

# START_10K_1 = r"item 1a\.\s*Risk Factors"
# STOP_10K_1 = r"item 1b\.\s*Unresolved Staff Comments"

#START_10K_1 = "1A.Risk Factors."
#STOP_10K_1 = ["1B.Unresolved Staff Comments","1B. Unresolved Staff Comments","1B.  Unresolved Staff Comments"]

# START_10K_2 = r"7\.\s*Management"
# STOP_10K_2 = r"7A\.\s*Quantitative and Qualitative Disclosures About Market Risk"

#START_10K_2 = "7.Management"
#STOP_10K_2 = "7A.Quantitative and Qualitative Disclosures About Market Risk."