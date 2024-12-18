
## Предупреждение
Если у вас Python 3.9 или ниже, замените `<тип1> | <тип2>` на `Union[<тип1>, <тип2>]`

## Создание репозитория
```
git init
git remote add origin git@github.com:<никнейм>/<названиеРепозитория>.git
.... add gitignore
git add .
git commit -m "..."
git branch -M main
git push -u origin main
```

## Подготовка сервера
### git
```
sudo apt-get update
sudo apt-get install git
```

### docker
Можно воспользоваться инструкцией: https://docs.docker.com/engine/install/ubuntu/
или скопировать код ниже
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Запуск приложения
Создание образа (коробки) с приложением
```
docker build . --tag fastapi_app
```
Запуск образа в контейнере с пробросом портов для доступа к контейнеру из интернета
```
docker run -p 80:80 fastapi_app
```



---

## Warning
If you are using Python 3.9 or earlier, replace `<type1> | <type2>` with `Union[<type1>, <type2>]`.

## Creating a Repository
```
git init
git remote add origin git@github.com:<username>/<repositoryName>.git
.... add .gitignore
git add .
git commit -m "..."
git branch -M main
git push -u origin main
```

## Preparing the Server
### git
```
sudo apt-get update
sudo apt-get install git
```

### docker
You can use the instructions: https://docs.docker.com/engine/install/ubuntu/
or copy the code below:
```
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

### Running the Application
Create an image (box) with the application:
```
docker build . --tag fastapi_app
```
Run the image in a container with port forwarding to allow internet access to the container:
```
docker run -p 80:80 fastapi_app
```
