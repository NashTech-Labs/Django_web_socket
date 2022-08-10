## What is web-Socket in Django?
Web Socket is a bi-directional, a full duplex protocol that is used to in the client-server communication.it start from ws:// or wss://, ws stand for webSocket. It is stateful protocol.

WebSockets (via Django) managing the communication between the client and the server, whenever a user is authenticated, an event will be broadcasted to every other connected user.Each user's screen will change automatically, without them having to reload their browsers.

## What is a Consumer?
Django Channels facilitates support of WebSockets in Django in a manner similar to traditional HTTP views. It wraps Django's native asynchronous view support, allowing Django projects to handle not only HTTP, but also protocols that require long-running connections, such as WebSockets, MQTT, chatbots, etc.

## asgi
The Asynchronous Server Gateway Interface, is the designed to Channels apps from a specific application server and provide a common way to write application and middleware code.


# How to use web-socket in Django?
You have create the Django project and inside the django project create the application using the command.
'django-admin startproject projectname'
'python3 manage.py startapp applicationname'

After the above process you can put the application name in the installed_app in setting.py file and install the cahnnels and redis using the pip command.
'pip install channels'
'pip install channels-redis'

Inside the installed_app put the channels in setting.py file after the installation of channel.

Use the asgi application inside the settinf.py file and comment the wsgi application
'ASGI_APPLICATION = 'chatproject.asgi.application'

and add the channel layer in setting.py under the asgi application

'CHANNELS_LAYERS = {
    "deafult":{
        "BACKENDS": "channels_redis.core.RedisChannelLayer",
        "CONFIG":{
            "hosts":[("localhost", 6379)],
        },
    },
}'

Running the Django server use the command
'python3 manage.py runserver'

In the web-Socket use the 'ws' in the URL
ex- 'ws://localhost:8000/'

you can use the websocketking to the websocket connection test(communication).
'https://websocketking.com/'
