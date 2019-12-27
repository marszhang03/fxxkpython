import requests

# Referer是看了网上的攻略，如果不加，获取不到图片
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Referer':'https://www.mzitu.com/192647'          
}

def request_mzitu(url):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.content
    except requests.RequestException:
        return None

def main(page):
    url = "https://i5.meizitu.net/2019/07/01b0"+ str(page) +".jpg"
    # pic_name = "20190701b"+ str(page) +".jpg"
    # 先按/区分，然后再切片
    pic_name = url.split('/')[-1]
    # 将获取到的图片源码存入html
    html = request_mzitu(url)
    # 写入文件需要用二进制的形式
    with open (pic_name,'wb') as f:
        f.write(html)
    
if __name__ == '__main__':
    for i in range(1,5):
        main(i)