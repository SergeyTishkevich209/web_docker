##### Я взял готоввый образ для работы с python основанный на Ubuntu, подготовленый моим знакомым AlexeyGulyaev 
> pndf/my-py:latest

##### images "svtishkevich777/server" и "svtishkevich777/client" это собранные из "pndf/my-py" образы на основе Dockerfile которые лежат в соответсвующих дерикториях.
##### Собирались они командами, приведенными ниже из соответствующих директорий
```
docker build -t pndf/client:latest
docker build -t pndf/server:latest
```
##### В данном проекте используется утилита docker-compose, из корневой директории 
##### запуск
```
docker-compose up -d
```
##### остановка
```
docker-compose down
```
Pапускаем клинет по адресу localhost:82, который запрашивает случайное
число с сервера localhost:81,
и еcли второй недоступен, то вместо случайного числа мы увидим "null"