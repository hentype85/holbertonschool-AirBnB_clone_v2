-- create the database hbnb_test_db if not exists
-- create the user hbnb_test if not exists and set the password to hbnb_test_pwd
-- grant all privileges to hbnb_test on hbnb_test_db
-- grant select privilege to hbnb_test on performance_schema

CREATE DATABASE if NOT EXISTS hbnb_test_db;

CREATE USER if NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';