import requests
import os

current_folder = os.getcwd()

folder_name = 'html'

folder_path = os.path.join(current_folder, folder_name)

os.makedirs(folder_path, exist_ok=True)

url = input("주소 입력 (input url): ")
response = requests.get(url)
if response.status_code == 200:
    # HTML 파일 저장 경로
    file_path = os.path.join(folder_path, "index.html")

    # HTML 내용 저장
    html = response.text
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)
else:
    print("error")
