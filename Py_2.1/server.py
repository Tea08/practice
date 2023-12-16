import socket

user_credentials = {"user1": "pass1", "user2": "pass2"}     # Словарь для хранения пар логин-пароль

def authenticate(client_socket):     
   login = client_socket.recv(1024).decode()    # Получение логина и пароля от клиента 
   password = client_socket.recv(1024).decode()  
   if login in user_credentials and user_credentials[login] == password:       # Проверка логина и пароля
      client_socket.send("Аутентификация прошла успешно".encode())
      return True
   else:
      client_socket.send("Не удалось выполнить аутентификацию".encode())
      return False

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # Создание сокета
server_address = ('localhost', 9090)      #Установка хоста и порта('хост', порт)
server_socket.bind(server_address)     # Привязка сокета к хосту и порту
server_socket.listen(1)    # Начало прослушивания
print(f"Сервер запущен на {server_address[0]}:{server_address[1]}")
client_socket, client_address = server_socket.accept()     # Принятие соединения клиента 
print(f"Соединение установлено с {client_address}")

if authenticate(client_socket):     # Аутентификация клиента
   print("Клиент успешно прошел аутентификацию.")     
# Продолжение работы с аутентифицированным клиентом

while True:    #Обработка запросов от клиента   
   data = client_socket.recv(1024)     #Получение данных от клиента
   if not data:
      break
   print(f"Получено от клиента: {data.decode()}")   
   response = "Сообщение получено!"    # Отправка ответа клиенту
   client_socket.send(response.encode())   

client_socket.close()      # Закрытие соединения
#server_socket.close()