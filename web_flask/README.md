# AirBnB clone - Web framework

## pip3 install Flask

start mysql service: 
sudo service mysql start  

usage with scripts: 
```
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list 
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states 
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states 
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.10-hbnb_filters 
```
in borwser: 
```
http://localhost:5000/states_list 
http://localhost:5000/cities_by_states 
http://localhost:5000/states  
http://localhost:5000/states/421a55f4-7d82-47d9-b54c-a76916479552  
http://localhost:5000/holberton 
http://localhost:5000/hbnb_filters 
```
in other tab: 
```
curl 0.0.0.0:5000/states_list ; echo "" 
curl 0.0.0.0:5000/cities_by_states ; echo "" 
curl 0.0.0.0:5000/states ; echo "" 
curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo "" 
curl 0.0.0.0:5000/states/holberton ; echo "" 
```

*use hbnb_dev_db database*  
```
DROP DATABASE IF EXISTS hbnb_dev_db;  
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p  
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./main_place_amenities.py 
HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list 
```