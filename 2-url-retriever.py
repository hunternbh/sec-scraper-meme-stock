
import os.path
import requests
import glob
import os

LINK = 'links-2020-q3.txt'

#using requests library to get the information
def get_data(link):
    hdr = {'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36'}
    req = requests.get(link,headers=hdr)
    content = req.content
    return content

# main function - takes links from links folder and outputs into data folder
def url_retrieve(file_link,name_file):
    links = open(file_link, 'r')
    cwd = os.getcwd()
    newpath = cwd+"\\1-data\\"+name_file
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    os.chdir(newpath)
    for link in links:
        link_split = link.split("|")
        filename = link_split[0] + " " + link_split[1] + " " + link_split[2]
        cik = link_split[3]
        filename = filename + "_" + cik
        filename=filename.replace("/","-")
        if not os.path.isfile(filename):
            print('Downloading: ' + filename)
            try:
                bb = get_data(link_split[4])
                f = open(filename, 'wb')
                f.write(bb)
            except Exception as inst:
                print(inst)
                print('  Encountered unknown error. Continuing.')

# calls the function url_retrieve iteratively for the items in the links folder
cwd = os.getcwd()
file_list = glob.glob(cwd+"\\links\\*.*")
for file in file_list:
    name_file = (file.split('\\'))[-1]
    url_retrieve(file,name_file)

# downloads in data folder are in raw format, we need to add extensions and parse them.

data_list = glob.glob(cwd+"\\1-data\\*")
for path in data_list:
    files = os.listdir(path)
    for index, file in enumerate(files):
        os.rename(os.path.join(path, file), os.path.join(path, file+'.html'))