# Combinar script de Python con Docker


---

* **Utiliza docker hub para encontrar la imagen de python**

```yml
FROM python:3

RUN pip install pytube

```

    
* **Personaliza la imagen (usa el fichero Dockerfile) añadiendole:**

```yml
FROM python:3

RUN pip install pytube


```

```yml
services:
  py:
    image: youtubeimagen:latest
    build: .
    volumes:
      - .:/usr/src/app
    stdin_open: true
    tty: true
    working_dir: /usr/src/app
    command: python3 Damian_1.py
```
* **Construye la nueva imagen con 'docker build'**

Para construir la imagen primero me logueo en docker con el comando ```docker login ```
![Imagen](https://github.com/Jacobo1234556/Protectodamian/blob/master/Imagenes/Captura%20de%20pantalla%20de%202023-03-02%2017-35-01.png?raw=true)

A continuación creo la imagen con el comando ```docker build -t nombre_de_mi_imagen:latest .```

![Imagen](https://github.com/Jacobo1234556/Protectodamian/blob/master/Imagenes/Captura%20de%20pantalla%20de%202023-03-08%2017-54-06.png?raw=true)

* **Pruebala con "docker run"**

![Imagen](https://github.com/Jacobo1234556/Protectodamian/blob/master/Imagenes/Captura%20de%20pantalla%20de%202023-03-08%2018-27-11.png?raw=true)

* **Crea un docker-compose.yml para lanzar el contenedor**
    ``` yml
    services:
  py:
    image: youtubeimagen:latest
    build: .
    volumes:
      - .:/usr/src/app
    stdin_open: true
    tty: true
    working_dir: /usr/src/app
    command: python3 Damian_1.py
 
    ```
* Date de alta en docker-hub, para poder subirla y hacerla pública
    Crea un repositorio en docker-hub y sube tu imágen

