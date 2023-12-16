import os
import time
import git
from git import Repo

# Пути к выбранным директориям и файлам
watched_paths = "C:\Users\TEA\code\future\sand"

# Функция для добавления всех изменений в локальный репозиторий и создания коммита
def commit_changes(repo, message):
    repo.git.add(update=True)
    repo.index.commit(message)
    print("Изменения добавлены в локальный репозиторий")

# Функция для отправки изменений на удаленный репозиторий (GitHub)
def push_to_remote(repo, remote_name="origin"):
    repo.git.push("--all", remote_name)
    print("Изменения отправлены на удаленный репозиторий")

# Функция для проверки изменений в выбранных директориях и файлах
def check_for_changes(repo, paths):
    for path in paths:
        if os.path.exists(path):
            repo.index.add([path])
            diff = repo.git.diff(repo.head.commit, path)
            if diff:
                print(f"Обнаружены изменения в {path}.")
                commit_message = f"Изменения в {path}"
                commit_changes(repo, commit_message)
                push_to_remote(repo)
        else:
            print(f"Путь {path} не существует.")

# Основная функция, которая выполняет проверку изменений с заданным интервалом времени
def main():
    repo_path = "путь/к/локальному/репозиторию"
    repo = Repo(repo_path)
    while True:
        check_for_changes(repo, watched_paths)
        time.sleep(60)  # Интервал проверки изменений (в секундах)

if __name__ == "__main__":
    main()
