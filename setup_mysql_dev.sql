-- create the hbnb_dev_db database if not exist
-- create the hbnb_dev user if not exist and set the password to hbnb_dev_pwd
-- grant all privileges to the hbnb_dev user on the hbnb_dev_db database
-- grant select privilege to the hbnb_dev user on the performance_schema database

CREATE DATABASE if NOT EXISTS hbnb_dev_db;

CREATE USER if NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;