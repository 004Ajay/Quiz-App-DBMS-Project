-- DB COMMANDS

-- SQL SYNTAX VALIDATOR(ONLINE): https://www.eversql.com/sql-syntax-check-validator/

-- ---------------------------------------------------------------------------------------- --

-- FOR REMOVING TABLES FROM PROGRAMIZ SQL EDITOR
DROP TABLE CUSTOMERS;
DROP TABLE ORDERS;
DROP TABLE SHIPPINGS;

-- ---------------------------------------------------------------------------------------- --

-- USERNAME: ROOT
-- PASSWORD: 1234
-- DATABASE NAME: PROJECT

-- CHANGE DATABASE TO OUR DB
USE PROJECT;

-- SHOW TABLES IN DATABASE
SHOW TABLES;

-- ---------------------------------------------------------------------------------------- --

-- FOR CREATING 'SIGN-IN' TABLE
CREATE TABLE PLAYERS(USRNM VARCHAR(20), EMAIL VARCHAR(20) NOT NULL, PSWD VARCHAR(20), PRIMARY KEY(EMAIL));

-- INSERTING VALUES TO 'SIGN-IN' TABLE
INSERT INTO PLAYERS VALUES ('AJAY', 'AJAY@GMAIL.COM', 'SJC'), ('JUDIN', 'JUDIN@GMAIL.COM', 'SJC'), ('JUSTIN', 'JUSTIN@GMAIL.COM', 'SJC'), ('NOYAL', 'NOYAL@GMAIL.COM', 'SJC'), ('VISHNU', 'VISHNU@GMAIL.COM', 'SJC');

-- CHECKING TABLE CREATION IS SUCCESS OR NOT
SELECT * FROM PLAYERS;

-- DELETE DATA FROM TABLE
DELETE FROM PLAYERS WHERE EMAIL = 'AJAY@GMAIL.COM';

-- ---------------------------------------------------------------------------------------- --

-- SAMPLE LOGIN QUERY
SELECT * FROM USERS WHERE usrnm = 'AJAY' AND pswd = 'SJC'