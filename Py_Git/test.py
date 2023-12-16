import os
import time
from git import Repo, Remote

# Путь к директории, которую нужно отслеживать
dir_path = 'C:/Users/TEA/code/practice'

# Подключение к локальному репозиторию Git
repo = Repo(dir_path)

# URL удаленного репозитория Git
remote_url = 'https://github.com/Tea08/practice.git'

# Функция для проверки изменений и создания коммита
def check_changes_and_commit():
    # Получаем список измененных файлов
    changed_files = [item.a_path for item in repo.index.diff(None)]
    
    if changed_files:
        # Добавляем все изменения в локальный репозиторий
        repo.index.add(changed_files)
        
        # Создаем коммит с автоматическим сообщением
        commit_message = f'Auto commit: {time.strftime("%Y-%m-%d %H:%M:%S")}'
        repo.index.commit(commit_message)

        # Отправляем изменения на удаленный репозиторий
        #remote = repo.create_remote('origin', remote_url)
        #remote.push(refspec='main:main')
        repo.git.push("--all", 'origin', remote_url)
        print('Изменения успешно отправлены на удаленный репозиторий.')
    else:
        print('Изменений не обнаружено.')

# Периодически проверяем изменения раз в час
while True:
    check_changes_and_commit()
    time.sleep(60)  # 3600 секунд = 1 час

if __name__ == "__main__":
    main()
