import requests
from pyquery import PyQuery as pq
import os

threadURL = 'https://boards.4chan.org/wg/thread/7763875'
# r = requests.get(threadURL)
d = pq(url=threadURL)
links = d('.fileText > a')
dir_name = "nobra"
try:
    os.mkdir(dir_name)
except Exception:
    print("Oje")

for link in links:
    full_path = link.attrib["href"] # //i.4cdn.org/wg/1619558467950.jpg
    picture_file_req = requests.request('GET',url="https:"+full_path)

    file_name = full_path.split("/")[-1]
    # os.getcwd()
    picture_path = os.path.join(dir_name,file_name)
    with open(picture_path,"w+b") as curr_file:
        curr_file.write(picture_file_req.content)


