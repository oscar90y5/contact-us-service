build-django:
	docker build -t contact-us-django ./django
	docker tag contact-us-django:latest osferna/contact-us-django:latest
	docker push osferna/contact-us-django:latest

image-size:
	docker manifest inspect osferna/contact-us-django:latest | jq '.layers[].size' | awk '{s+=$$1} END {printf "Comprimido: %.2f GB\n", s/1024/1024/1024}'

ssh:
	ssh -i servidor-gratis.pem ec2-user@ec2-34-241-229-197.eu-west-1.compute.amazonaws.com

up:
	docker compose -f contact-us-docker-compose.yml -f contact-us-docker-compose-dev.yml --env-file .env.local up -d --pull always

down:
	docker compose -f contact-us-docker-compose.yml -f contact-us-docker-compose-dev.yml --env-file .env.local down
