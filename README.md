# E7

Необходимо установить docker и docker-compose.
##I вариант 
1. В docker-compose.yaml задать mongo_db_path
2. Собрать образы командой
    docker-compose build
3. Их запустить с помощью команды 
    docker-compose up
4. Открыть ссылку и должно заработать))))  
##II вариант
1. запустить образы следующими комантами
docker run --name redis -d --restart unless-stopped -p "6379:6379" redis
docker run --name mongo -d --restart unless-stopped -p "27017:27017" -v /opt/mongo/db:/data/db mongo
2.запустить вебсервер командой:
gunicorn -w 4 -b 127.0.0.1:5000 api:app
3. Открыть ссылку и должно заработать))))  
