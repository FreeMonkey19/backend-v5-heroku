to activate venv - source venv/bin/activate
to open local database - sqlite3 api/database.database
there is two tables in the local db - user_data and job_listings

link to api - https://jobs.github.com/api
endpoint used in search form - https://jobs.github.com/positions?description=python&location=new+york
endpoint used to get all job listings - https://jobs.github.com/positions.json?

to run locally you must be in venv and then add this to the commandline
1. export FLASK_APP=api
2. export FLASK_DEBUG=1
3. then flask run 

this app is set up for automatic deployment
depoloyed version is here: https://application-station.herokuapp.com
https://dashboard.heroku.com/apps/application-station

get list of all users: https://application-station.herokuapp.com/api/users


flask migration commands
flask db Migrate
flask db upgrade
flask db --help

flask docs - https://flask.palletsprojects.com/en/1.1.x/quickstart/

postgres db for deployed version

local frontend Desktop/v5 on Ada loaner laptop
frontend deployed on gh-pages here: https://freemonkey19.github.io/application-station/

install: 
virtualenv
flask
python
pip3
psycopg2

I used `pip3` or `python -m` to install technologies depending on the docs being read


