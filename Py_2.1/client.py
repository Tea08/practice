import socket

def login():
   login = input("Введите логин: ")
   password = input("Введите пароль: ")
   return login, password

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Создание сокета
server_address = ('localhost', 9090)      # Установка хоста и порта
client_socket.connect(server_address)     # Подключение к серверу

login, password = login()     # Отправка логина и пароля на сервер для аутентификации
client_socket.send(login.encode())
client_socket.send(password.encode())

auth_result = client_socket.recv(1024).decode()    # Получение результата аутентификации 
print(auth_result)

if auth_result == "Аутентификация прошла успешно":
   while True:    #Отправка запросов на сервер      
      message = input("Введите сообщение: ")    # Ввод сообщения      
      client_socket.send(message.encode())      # Отправка данных серверу       
      response = client_socket.recv(1024)    # Получение ответа от сервера
      print(f"От сервера: {response.decode()}")

      if message.lower() == 'exit':    # Проверка на выход
         break

client_socket.close()      # Закрытие соединения
