#Faust agent communication

For check connection of separated faust applications:
1) Start faust apps and kafka<br>
`sudo docker-compose up -d`
2) Wait while app starting (use `sudo docker-compose logs producer_service` for check)
3) Send message producer, for testing .ask() method:<br>
`sudo docker exec -it producer_service faust -A app send @producer_agent "Hello Faust"`
4) Check logs in producer and consumer:
- `sudo docker-compose logs producer_service`
- `sudo docker-compose logs consumer_service`

Get topics:
- `sudo docker exec -it kafka ./opt/bitnami/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181`