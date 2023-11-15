import requests

url = input("주소 입력 (input url) : ") 

response = requests.get(url)

if response.status_code == 200:
    html = response.text  # 웹페이지의 HTML 내용
    with open("webpage.html", "w", encoding="utf-8") as f:
        f.write(html)
else:
    print("error")
