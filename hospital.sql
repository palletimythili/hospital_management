
CREATE DATABASE hospital;

USE hospital;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(20),
    disease VARCHAR(100)
);

INSERT INTO patients (name, age, gender, disease)
VALUES
('Rahul', 25, 'Male', 'Fever'),
('Priya', 22, 'Female', 'Cold');

SELECT * FROM patients;
