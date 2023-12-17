import time
from git import Repo

dir_path = 'C:/Users/TEA/code/practice'   # Путь к директории, которую нужно отслеживать  
repo = Repo(dir_path)   # Подключение к локальному репозиторию Git
remote_url = 'https://github.com/Tea08/practice.git'  # URL удаленного репозитория Git

def check_changes_and_commit():  # Функция для проверки изменений и создания коммита    
    changed_files = [item.a_path for item in repo.index.diff(None)]     # Получаем список измененных файлов    
    if changed_files:       
        repo.index.add(changed_files)   #Добавляем все изменения в локальный репозиторий 
        commit_message = f'Auto commit: {time.strftime("%Y-%m-%d %H:%M:%S")}'    # Создаем коммит с автоматическим сообщением
        repo.index.commit(commit_message)        
        repo.git.push("--all", 'origin')     # Отправляем изменения на удаленный репозиторий
        print('Изменения успешно отправлены на удаленный репозиторий.')
    else:
        print('Изменений не обнаружено.')

while True:    # Периодически проверяем изменения раз в час
    check_changes_and_commit()
    time.sleep(3600)  # 3600 секунд = 1 час

if __name__ == "__main__":
    main()
