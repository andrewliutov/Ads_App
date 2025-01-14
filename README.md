## REST API (backend) для сайта объявлений с использованием Flask

Реализованы методы создания/удаления/редактирования объявления.    

Реализована система прав:
* Создавать объявление может только авторизованный пользователь.
* Удалять/редактировать может только владелец объявления.
  
У объявления есть: 
- идентификатор
- заголовок
- описание
- дата создания
- владелец

У пользователей есть: 
- идентификатор
- имя
- почта
- хэш пароля

---
  
Для сборки образа из файла Dockerfile необходимо выполнить команду:

`docker build --tag flask_rest_api_image .`

Команда для запуска контейнера на основе собранного образа:

`docker run -P -d --name rest_api_container flask_rest_api_image`
