-- Script that creates the database hbtn_0d_usa and the table cities
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS cities (
    id iNT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id int NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);