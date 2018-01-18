import os
import json
import requests

def download_json():
    resp = requests.get('http://pvp.qq.com/web201605/js/herolist.json', stream=True)
    data = resp.content.decode()
    list = json.loads(data)
    num = []
    if os.path.exists('picture'):
        os.chdir('picture')        #改变目录
    else:
        os.mkdir('picture')    #创建目录
        os.chdir('picture')
        #print(os.getcwd())
    for i in range(len(list)):
        dict = list[i]
        #print('字典:', dict)
        num.append(dict.get('ename'))
    print(num)
    #pictures = os.mkdir('picture')

    #遍历列表
    for i in range(len(num)):
        #print(num[i])
        URL = 'http://game.gtimg.cn/images/yxzj/img201606/heroimg/' + str(num[i]) + '/' + str(num[i]) + '.jpg'
        resp = requests.get(URL, stream=True)
        with open(str(num[i]) + '.jpg', 'wb') as fd:
            for pictures in resp.iter_content(128):
                fd.write(pictures)
            fd.close()

if __name__ == '__main__':
    download_json()
















