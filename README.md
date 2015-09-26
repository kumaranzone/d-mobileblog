# d-mobileblog
This is sample mobile blog made in django
# Move to the project directory
cd d-mobileblog/
# Create a virtualenv to isolate our package dependencies locally
virtualenv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
sleep 10
# Install Django into the virtualenv
pip install -r requirements.txt
sleep 10
./manage.py makemigrations blog
./manage.py migrate blog
./manage.py runserver 0.0.0.0:8000/
