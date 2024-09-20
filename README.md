# Cadastro de Categorias de cursos.

- Estamos utilizando o docker e poetry. Sugiro que instale para conseguir subir o servidor.

1 - Precisamos instalar o gRPC e os plugins para compilar e gerar os arquivos do pb

```bash
poetry install
```

2 - Buildar a imagem do Servidor

```bash
docker buildx build -t grpc_server_course .
```

3 - Criar e executar o container com a iamgem do Servidor

```bash
docker run -it -p 50051:50051 --name grpc_server grpc_server_course
```

### Testes

  - Existe um client(course/client.py) que implementei para testar a aplicação. Acesse este arquivo e altere o **nome** e a **descrição**.

1 - Comando para rodar o client 

```bash
python -m course.client
```