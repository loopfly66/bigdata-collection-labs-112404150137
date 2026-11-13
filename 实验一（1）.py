import requests

def get_image(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/79.0.3945.88 Safari/537.36"
        }
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status() 
        return r.content
    except Exception as err:
        print(f"获取图片异常：{err}")
        return None

def save_image(path, content):
    if content is None:
        return
    with open(path, "wb") as f:
        f.write(content)


if __name__ == "__main__":
    url_list = [
        "http://www.bspider.top/static/yh31/images/202103302056530751.gif",
        "http://www.bspider.top/static/yh31/images/202103182029425871.jpg"
    ]
    save_dir = "d:/"   
    for url in url_list:
        img_content = get_image(url)
        file_name = url.split("/")[-1]
        full_path = save_dir + file_name
        save_image(full_path, img_content)
        print(f"已保存：{full_path}")
