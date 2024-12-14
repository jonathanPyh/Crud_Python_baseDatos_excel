CREATE DATABASE MiDatos;

USE MiDatos;

CREATE TABLE Datos_Person(
ID INT IDENTITY(1,1) PRIMARY KEY,
Nombre NVARCHAR(50) NOT NULL,
Edad INT NULL,
Correo NVARCHAR(100) NOT NULL,
Telefono NVARCHAR(11) NOT NULL,
);

INSERT INTO Datos_Person(Nombre,Edad,Correo,Telefono) VALUES('Juan',28,'jhon@.com','0123456789');

SELECT * FROM Datos_Person;
