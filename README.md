Quick Registration Api using Django-Django Rest Framework 

Host and send url to the front end developer and integrate into the front end (form)

**INSTALLATION PROCESS**
Install Python 3.1 or any version that is still supported mostly python3 

install Django
Install Django Rest Framework 

Create a folder on your local device

cd into that directory through your terminal or command prompt 

cd Folder path(copy  the path)

create a virtual environment

python -m venv venv 


Then activate your env

source venv/bin/activate - for Macos 
venv\Script\activate - for windows 

Install django again to  be sure
might see equirements already satisfied, but to be sure, try resinstalling

Create a django project

django-admin startproject myproject 

cd into the myproject folder 

Then create an app

remain on your terminal or command prompt 

python3 manage.py startapp myapp

Start your server 
python3 manage.py runserver 


**ADD INSTALLED LIBRARIES 
**

Go to your settings.py file and look for the Installed apps
and include the app the also the drf

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'django rest framework',
    ''
]

then start your server again.


**Pull a repository**

Create a directory locally where you want the repository to be cloned to

mkdir your directory name (create a directory ) // or you can use the normal createing of folder step 

cd your directory name (navigate into the directory) // or you use cd the directory path

Click on the green code button you see 

copy the HTTPS url 

open your command prompt or terminal 
Nacigate to the directory where you want to clone the repository 

use the [

      git clone https://github.com/username/repository-name.git  ##for HTTPS
      git clone git@github.com:username/repository-name.git      ##for SSH
]

**Navigate to the Repository Directory**

cd repositoy name.
