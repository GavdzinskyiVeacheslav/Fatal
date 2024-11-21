import requests

# Замените 'YOUR_GITHUB_TOKEN' на ваш персональный токен доступа
TOKEN = 'g h p _ g Q P K S N e Y 2 g D a t Y E Q T a v r 3 b 0 l K p f M k N 3 5 9 H e 9'
GIST_ID = 'e3bcb1c11d58fb764e83ac1a366f855c'  # ID вашего Gist
GIST_URL = f'https://api.github.com/gists/{GIST_ID}'

# Путь к локальному файлу, который вы хотите добавить
local_file_path = 'C:\\Users\\HONOR\\OneDrive\\Рабочий стол\\D.py'  # Замените на путь к вашему файлу

# Чтение содержимого локального файла
with open(local_file_path, 'r') as file:
    file_content = file.read()

# Данные для обновления Gist
new_file_data = {
    "files": {
        "README.py": {  # Имя файла в Gist
            "content": file_content  # Содержимое файла
        }
    }
}

# Заголовки для запроса
headers = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Отправляем PATCH-запрос для обновления Gist
response = requests.patch(GIST_URL, json=new_file_data, headers=headers)

if response.status_code == 200:
    print("Файл успешно добавлен в Gist!")
    print("URL Gist:", response.json()['html_url'])
else:
    print("Произошла ошибка:", response.status_code, response.json())