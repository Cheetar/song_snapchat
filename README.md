Snapchat for songs
===========
Share music in a magical way

### Technology
- Django 2.0.7
- Bootstrap 4.0.0

### Installation
- Download this repo `git clone https://github.com/Cheetar/song_snapchat.git`
- Enter project's directory `cd song_snapchat`
- Setup virtual environment `virtualenv venv`
- Activate the virtual environment `source venv/bin/activate`
- Go into web/app/ directory `cd web/app/`
- Install dependencies `pip install -r requirements.txt`
- Create an .env file with custom settings suiting your needs (you can update .env.example accordingly and save it as .env)
- Migrate data to database `python manage.py migrate`
- Create admin account `python manage.py createsuperuser`
- Start the app `python manage.py runserver`

### Tests
- To run tests: `python web/app/manage.py test`

### Live
The app runs live here: https://snapchatforsongs.com
