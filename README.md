# DjangoSocialNetwork
Social network on Pyhon/Django 

1. git clone https://github.com/DolphinHMPY/DjangoSocialNetwork.git
2. you should change the paths for yourself:
    ./DjangoSocialNetwork/social_network/social_network/settings.py - MEDIA_ROOT = ...
    ./DjangoSocialNetwork/social_network/user/models.py - Photo.correct_dir() -> ...
    ./DjangoSocialNetwork/social_network/user/views.py Photo.get .replace(...)
3. python ./DjangoSocialNetwork/social_network/manage.py migrate
