CREATE DATABASE ria_iniciales;

USE ria_iniciales;

CREATE TABLE clientes(
    nombre varchar(50) NOT NULL PRIMARY KEY,
    ape_pat_cli varchar(50) NOT NULL,
    ape_mat_cli varchar(50) NOT NULL,
    telefono_cli varchar(10) NOT NULL,
    email varchar(50) NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO clientes (nombre, ape_pat_cli, ape_mat_cli, telefono_cli, email) 
VALUES ('Dejah', 'Juarez', 'Lopez', '7162534987', 'dejah@barson'),
('John', 'Carter', 'Juarico', '1928763527', 'jhon@earth'),
('Carthoris', 'Mendoza', 'Francis', '8921764567', 'carthoris@barson');

CREATE TABLE productos(
    codigo varchar(10) NOT NULL PRIMARY KEY,
    nombre_produ varchar(50) NOT NULL,
    existencia int NOT NULL,
    fecha_caducidad DATE NOT NULL,
    no_lote varchar(30) NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO productos(codigo, nombre_produ, existencia, fecha_caducidad, no_lote) VALUES
('6278172634', 'Jabon', 35, now(), '35'),
('8982716234', 'Pozole', 20, now(), '69'),
('9817983213', 'Agua', 10, now(), '98');

SHOW TABLES;

SELECT * FROM clientes;

DESCRIBE clientes;

CREATE USER 'ria'@'localhost' IDENTIFIED BY 'ria.2019';
GRANT ALL PRIVILEGES ON ria_iniciales.* TO 'ria'@'localhost';
FLUSH PRIVILEGES;