# Playing with Kafka
Start Kafka with:

```
docker-compose up -d
```

Create a topic using:

```
./create_kafka_topic.sh event1, event2
```

To see the list of topics:
```
docker compose exec broker kafka-topics --list --bootstrap-server broker:9092
```

To see the describtion of the topics
```
docker compose exec broker kafka-topics --describe --bootstrap-server broker:9092
```

Listen to events via:

```
docker exec -ti broker kafka-console-consumer \
	--topic events \
	--bootstrap-server broker:9092
```

And, in a separate terminal, send some events via:

```
docker exec -ti broker kafka-console-producer \
	--topic events \
	--bootstrap-server broker:9092
```

Write the events in the terminal, separating with a newline.

