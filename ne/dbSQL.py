CREATE DATABASE netflix;

use netflix;

CREATE TABLE usuarios(
	idUsuario int auto_increment primary key,
    usuario varchar(45) not null,
	email varchar(100) not null,
    plano varchar(50),
    tipo varchar(50),
	idade int
    );

CREATE TABLE filmes(
	idFilme int auto_increment primary key,
    filme varchar(80),
    plano varchar(50),
    descricao varchar(200)
);

INSERT INTO usuarios(usuario, email, plano, tipo)
values
	('Lindomar', 'lindomar@gmail.com', 'premium', 'admin'),
	('Joao',  'joao@gmail.com', 'basic', 'user'),
	('Bruna',  'bruna@gmail.com', 'medium', 'admin'),
	('Danilo',  'danilo@gmail.com', 'basic', 'admin'),
	('Nataly',  'nataly@gmail.com', 'premium', 'user'),
	('Karen',  'karen@gmail.com', 'medium', 'admin'),
	('Susy',  'susy@gmail.com', 'premium', 'admin'),
	('Paola',  'paola@gmail.com', 'premium', 'user'),
	('Junior',  'junior@gmail.com', 'basic', 'admin');
    
INSERT INTO filmes(filme, plano, descricao)
values
	('Duro de Matar', 'medium', 'xxxxxxxxxxxxx'),
	('Homem Aranha', 'premium', 'xxxxxxxxxxxxx'),
	('Avatar', 'premium', 'xxxxxxxxxxxxx'),
	('Homens de Honra', 'basic', 'xxxxxxxxxxxxx'),
	('Interestelar', 'medium', 'xxxxxxxxxxxxx'),
	('O Conde de Monte Cristo', 'basic', 'xxxxxxxxxxxxx'),
	('Coração Valente', 'premium', 'xxxxxxxxxxxxx');