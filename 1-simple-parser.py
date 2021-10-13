import csv
from zipfile import ZipFile
from io import BytesIO
import re
import os

'''
Each .idx (index) file contains 5 fields to identify a filing

1. cik - central index key (unique and primary key)
2. name - company name
3. Form - 
4. Filing date in YYYY-MM-DD format
5. path is the url extension after the main url - https://www.sec.gov/Archives/
~ For example, url extension = edgar/data/1000184/0000947871-21-000046.txt
~ full link is at https://www.sec.gov/Archives/edgar/data/1000184/0000947871-21-000046.txt
'''
class MasterIndexRecord:
    def __init__(self, line):
        self.err = False
        parts = line.split('|')
        if len(parts) == 5:
            self.cik = int(parts[0])
            self.name = parts[1]
            self.form = parts[2]
            self.filingdate = int(parts[3].replace('-', ''))
            self.path = parts[4]
        else:
            self.err = True
        return



'''
We then provide the list of ciks that we want to check on.
We must first compile this in a list. 
'''
regexlist=""
# separate each entry of CIK with a |
with open('cik.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader) #skip the first header
    for row in csv_reader:
        regexlist = regexlist + row[0] + "|"

regexlist = regexlist[:-1] #removes the last |
'''
To first start, we need to get the .idx file of each quarter. This is a directory of
all the filings. Access this at - https://www.sec.gov/Archives/edgar/full-index/
'''
#takes in an idx, regexlist as above 
def compile_into_text_file(master_idx,regexlist,link):
    masterindex = []
    with open(master_idx) as myfile:
        abc = myfile.read().splitlines()[10:]
        for line in abc:
            mir = MasterIndexRecord(line)
            if not mir.err:
                masterindex.append(mir)
    PARM_ROOT_PATH = 'https://www.sec.gov/Archives/'
    #PARM_ROOT_PATH = 'https://www.sec.gov/Archives/edgar/full-index/'

    f_8K = ['8-K']
    f_10K = ['10-K', '10-K405', '10KSB', '10-KSB', '10KSB40']
    f_10KA = ['10-K/A', '10-K405/A', '10KSB/A', '10-KSB/A', '10KSB40/A']
    f_10KT = ['10-KT', '10KT405', '10-KT/A', '10KT405/A']
    f_10Q = ['10-Q', '10QSB', '10-QSB']
    f_10QA = ['10-Q/A', '10QSB/A', '10-QSB/A']
    f_10QT = ['10-QT', '10-QT/A']
    # List of all 10-X related forms
    f_10X = f_10K + f_10KA + f_10KT + f_10Q + f_10QA + f_10QT + f_8K
    # Regulation A+ related forms
    f_1X = ['1-A', '1-A/A', '1-K', '1-SA', '1-U', '1-Z']

    PARM_FORMS = ['10-K','10-Q','8-K']

    #converts the regexlist to regular expression object to use re.search
    regexlist_re = re.compile(regexlist)

    file_txt = open(link,'w') #opens new .txt file to write in the entries

    for i in masterindex:
        if regexlist_re.search(str(i.cik)):
            # write a row to the csv file
            if i.form in PARM_FORMS:
                file_txt.write(i.name)
                file_txt.write("|")
                file_txt.write(str(i.form))
                file_txt.write("|")
                file_txt.write(str(i.filingdate))
                file_txt.write("|")
                file_txt.write(str(i.cik))
                file_txt.write("|")
                file_txt.write(PARM_ROOT_PATH+i.path)
                file_txt.write("\n")
    return

link_1 = 'links\\links-2020-q1.txt'
idx_1 = 'idx\\master-2021-q1.idx'

link_2 = 'links\\links-2020-q2.txt'
idx_2 = 'idx\\master-2020-q2.idx'

link_3 = 'links\\links-2020-q3.txt'
idx_3 = 'idx\\master-2020-q3.idx'

link_4 = 'links\\links-2021-q1.txt'
idx_4 = 'idx\\master-2021-q1.idx'

link_5 = 'links\\links-2021-q2.txt'
idx_5 = 'idx\\master-2021-q2.idx'

link_6 = 'links\\links-2021-q3.txt'
idx_6 = 'idx\\master-2021-q3.idx'

compile_into_text_file(idx_1,regexlist,link_1)
compile_into_text_file(idx_2,regexlist,link_2)
compile_into_text_file(idx_3,regexlist,link_3)
compile_into_text_file(idx_4,regexlist,link_4)
compile_into_text_file(idx_5,regexlist,link_5)
compile_into_text_file(idx_6,regexlist,link_6)