from app import app, db

from app.models import User, Post
# export FLASK_APP=microblog.py

#importerar databasen db till flask-shell (skalet för testing)
@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User, 'Post':Post}

#https://www.fullstackpython.com/flask.html för alla tutorials
#export MAIL_SERVER=smtp.googlemail.com export MAIL_PORT=587 export MAIL_USE_TLS=1 export MAIL_USERNAME=<your-gmail-username> export MAIL_PASSWORD=<your-gmail-password>
# export MAIL_SERVER=smtp.googlemail.com
# export MAIL_PORT=587
# export MAIL_USE_TLS=1

#OM LOCALHOST: python -m smtpd -n -c DebuggingServer localhost:8025 
# export MAIL_SERVER=localhost
# export MAIL_PORT=8025
