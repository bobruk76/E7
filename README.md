# E7
docker run --name redis -d --restart unless-stopped -p "6379:6379" redis
docker run --name mongo -d --restart unless-stopped -p "27017:27017" -v /opt/mongo/db:/data/db mongo