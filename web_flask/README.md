# AirBnB clone - Web framework

## pip3 install Flask

Environment variables:
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db

usage with scripts:
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states

int other tab:
curl 0.0.0.0:5000/states_list ; echo ""

int other tab:
curl 0.0.0.0:5000/cities_by_states ; echo ""

int other tab:
curl 0.0.0.0:5000/states ; echo ""
curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
curl 0.0.0.0:5000/states/holberton ; echo ""



issue
needed to comment in models/place.py :
"city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)"
run:
cat 7-dump.sql | mysql -uroot -p