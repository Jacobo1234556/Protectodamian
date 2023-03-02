from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=aFqTjk3kcEw&ab_channel=Garajedeideas")

#Title of video
print("Titulo: ",yt.title)
#Number of views of video
print("Numero de visitas: ",yt.views)
#Length of the video
print("Duración del video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Puntación: ",yt.rating)
