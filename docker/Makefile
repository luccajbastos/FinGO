# Nome dos containers e serviços
CONTAINER_NAME_DB=fingo_postgredb_dev
CONTAINER_NAME_APP=fingo_dev
DOCKER_COMPOSE_FILE=docker-compose-dev.yml

# Comando padrão do Docker Compose
DOCKER_COMPOSE=docker-compose -f $(DOCKER_COMPOSE_FILE)

# Iniciar o container
start:
	$(DOCKER_COMPOSE) up -d

# Parar o container
stop:
	$(DOCKER_COMPOSE) down

# Buildar do zero e iniciar, removendo containers e imagens antigos
rebuild:
	# Parar e remover containers antigos
	$(DOCKER_COMPOSE) down
	# Remover containers antigos se ainda existirem
	docker rm -f $(CONTAINER_NAME_DB) || true
	docker rm -f $(CONTAINER_NAME_APP) || true
	# Remover imagens antigas associadas
	docker rmi $(shell docker images -q postgres:15-alpine) || true
	docker rmi $(shell docker images -q myapp:latest) || true
	# Fazer o build novamente e subir
	$(DOCKER_COMPOSE) up --build -d

# Limpar containers, volumes e imagens antigas
clean:
	# Parar os serviços
	$(DOCKER_COMPOSE) down
	# Remover containers antigos
	docker rm -f $(CONTAINER_NAME_DB) $(CONTAINER_NAME_APP) || true
	# Remover volumes não utilizados
	docker volume prune -f
	# Remover imagens antigas
	docker rmi $(shell docker images -q) || true

# Verificar o status dos containers
status:
	docker ps -a

logs:
	$(DOCKER_COMPOSE) logs -f