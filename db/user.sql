CREATE DATABASE first;
use first;
GRANT ALL on first to root@localhost;

CREATE TABLE students (
    reg_no INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    vaccination_status VARCHAR(3) NOT NULL,
    PRIMARY KEY (reg_no)
);

INSERT INTO students (reg_no, name, vaccination_status)
VALUES
    (1001, 'John Doe', 'Yes'),
    (1002, 'Jane Doe', 'No'),
    (1003, 'Bob Smith', 'Yes');