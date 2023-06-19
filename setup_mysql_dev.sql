-- a script that prepares a MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creates a new user hbnb_dev
CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';
-- grants all privileges to database called hbnb_dev_db
GRANT ALL PRIVILEGES
   ON `hbnb_dev_db`*.*
   TO 'hbnb_dev'@'localhost'
   IDENTIFIED BY 'hbnb_dev_pwd';
-- grants SELLECT privilege to
GRANT SELECT
   ON `performance_schema`*.*
   TO 'hbnb_dev'@'localhost'
   IDENTIFIED BY 'hbnb_dev_pwd';
FLUSH PRIVILEGES;
