#!/bin/bash

docker compose exec broker kafka-topics --create --topic event1 --bootstrap-server broker:9092

docker compose exec broker kafka-topics --list --bootstrap-server broker:9092

docker compose exec broker kafka-topics --topic event1 --describe --bootstrap-server broker:9092
