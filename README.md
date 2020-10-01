# MyAwesomeCart - Django Website with payment gateway and admin panel 

$ git clone https://github.com/gocardless/sample-django-app.git
$ cd sample-django-app
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/shop/
