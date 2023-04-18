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

INSERT INTO usuarios(usuario, email, plano, tipo, idade)
values
	('Lindomar', 'lindomar@gmail.com', 'premium', 'admin', 37),
	('Joao',  'joao@gmail.com', 'basic', 'user', 22),
	('Bruna',  'bruna@gmail.com', 'medium', 'admin', 18),
    
INSERT INTO filmes(filme, plano, descricao)
values
	('Duro de Matar', 'medium', 'xxxxxxxxxxxxx'),
	('Homem Aranha', 'premium', 'xxxxxxxxxxxxx'),
	('Avatar', 'premium', 'xxxxxxxxxxxxx'),