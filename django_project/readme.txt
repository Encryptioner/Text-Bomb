

# Necessary Commands:


#virtual environment

$ workon web (env_name)

#to access global site-packages if not accessed

$ toggleglobalsitepackages

#install python3, django, django-class, crispy_forms, PIL, Pillow, pip, docker, redis 2.8 etc.

$ cd (path to django_project)

$ python manage.py makemigrations

$ python manage.py migrate

$ python3 manage.py createsuperuser

$ sudo docker run -p 6379:6379 -d redis:2.8

#Needed to be run after any change in tasks.py or celery.py
$ celery -A django_project worker -l info OR celery -A proj beat -l INFO


$ python3 manage.py runserver



# Necessary email, superuser, password

admin1
web1.chat0


admin2
web1.chat0


new1
web.1221


sefatullah.test18@gmail.com
#123vfrt



# Instructions

1. After running necessary commands a viewer should go to http://127.0.0.1:8000 

2. User can login or register from that page

3. Using standard precaution for registration user need to verify his mail by clicking verification link sent to his mail. It uses google smtp server.

4. User having previous account can login. He will sent to home page. Home and about section is not decorated yet.

5. User can see his profile and make updates.

6. Clicking chat user can go to chat home. Necessary linking has not been made yet. so typing any text and entering user will sent to a a chat portal.

7. if another user log in from another browser to test and go to same link of chat portal, then they can both chat in real time.

8. All contact list is not shown yet and there is no one to one relationship for chatting is not made yet, so any logged in user entering that link can participant in chat.

9. The number of newly registered user will be sent to every user in every hour. Functionality of this chat app is in progress and will be updated soon.

10. Thanks for reading. A folder of screenshots has been uploaded for detailed view.



  












