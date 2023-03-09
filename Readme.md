# Combinar script de Python con Docker


---

* **Utiliza docker hub para encontrar la imagen de python**

```yml
FROM python:3

RUN pip install pytube

```

    
* **Personaliza la imagen (usa el fichero Dockerfile) añadiendole:**

Fichero dockerfile y docker-compose-yml
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

Comprobación de Docker run

![Imagen](https://github.com/Jacobo1234556/Protectodamian/blob/master/Imagenes/Captura%20de%20pantalla%20de%202023-03-08%2018-27-11.png?raw=true)



* **Crea un docker-compose.yml para lanzar el contenedor**

Fichero docker-compose

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
* **Date de alta en docker-hub, para poder subirla y hacerla pública**

Me doy de alta en la página a traves del siguiente enlace https://hub.docker.com

![img.png](https://github.com/Jacobo1234556/Protectodamian/blob/master/Imagenes/img.png?raw=true)

* **Crea un repositorio en docker-hub y sube tu imágen**

Primero me logeo en docker con el comando ```docker login```

Despues creo un tag con el comando ```docker tag appyoutube:latest jacobocatelao/appyoutube:latest ```

Por ultimo subo la imagen con el comando ``` sudo docker push jacobocatelao/youtube:latest ```

![img.png](https://github.com/Jacobo1234556/Protectodamian/blob/master/Imagenes/captura.png?raw=true)

Una vez hecho estó ya tenemos la imagén subida y lista para usar

![img.png](https://github.com/Jacobo1234556/Protectodamian/blob/master/Imagenes/captura.png?raw=true)
