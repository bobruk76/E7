# E7
docker run --name redis-server -d --restart unless-stopped -p "6379:6379" redis
docker run --name mongo-server -d --restart unless-stopped -p "27017:27017" -v /opt/mongo/db:/data/db mongo