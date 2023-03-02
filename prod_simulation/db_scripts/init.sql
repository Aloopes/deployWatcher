CREATE DATABASE deploywatcher;
USE deploywatcher;

CREATE TABLE Transitions (
    id MEDIUMINT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    component VARCHAR(140),
    version DECIMAL(2,1),
    author VARCHAR(80),
    status VARCHAR(80),
    sentTimestamp DATETIME,
    receivedTimestamp DATETIME
);
