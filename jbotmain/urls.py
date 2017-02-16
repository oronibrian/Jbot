
from django.conf.urls import patterns, include, url
from .views import Jbotview

urlpatterns = [
     url(r'^EAABh4lUwvGIBAPtOCYyeNTHM9R2x8iCeuv3VQhek57IX6nPOG3Wm4pw5aiIImQJJJRhVrxH3AiGViHD7IFCBnj4NTdqhI4ZC4dWXHQgoIbuIqDNooyZCMLV426CCKvOCgnJHxp0qBryDLF6XomRh2gZAm5GKwnZAuSYXHS5QMAZDZD/', Jbotview.as_view()),
]
