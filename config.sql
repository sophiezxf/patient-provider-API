CREATE database doctorinfo;
USE doctorinfo;
CREATE TABLE docinfo(id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), address VARCHAR(100), address2 VARCHAR(100), docid INT(11));
CREATE TABLE avapp(id INT(11) AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), docid INT(11), date VARCHAR(100), dateid INT(11), address VARCHAR(100), address2 VARCHAR(100));
CREATE TABLE boapp LIKE avapp;
CREATE TABLE unavapp LIKE avapp;
