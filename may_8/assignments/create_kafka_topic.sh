#!/bin/bash

docker compose exec broker kafka-topics --create --topic event1 --bootstrap-server broker:9092 --partitions 3

docker compose exec broker kafka-topics --create --topic event2 --bootstrap-server broker:9092 --partitions 5

docker compose exec broker kafka-topics --list --bootstrap-server broker:9092

docker compose exec broker kafka-topics --describe --bootstrap-server broker:9092
