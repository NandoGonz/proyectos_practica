CREATE DATABASE biblioteca;

USE biblioteca2;

CREATE TABLE bibliotecas(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    direccion VARCHAR(255) NOT NULL,
    date_create DATETIME DEFAULT CURRENT_TIMESTAMP,
    date_update DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE secciones(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_biblioteca INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    piso INT NOT NULL,
    date_create DATETIME DEFAULT CURRENT_TIMESTAMP,
    date_update DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY(id_biblioteca) REFERENCES bibliotecas(id)
);

CREATE TABLE libros(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_seccion INT NOT NULL,
    id_biblioteca INT NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    generos VARCHAR(255) NOT NULL,
    prologo VARCHAR(255) NOT NULL,
    isbn BIGINT NOT NULL,
    autores VARCHAR(255) NOT NULL,
    FOREIGN KEY(id_seccion) REFERENCES secciones(id),
    FOREIGN KEY(id_biblioteca) REFERENCES bibliotecas(id)
);

INSERT INTO bibliotecas (nombre, direccion) VALUES
('Biblioteca Central', 'Calle 45 #12-30'),
('Biblioteca Norte', 'Av. Las Palmas 90'),
('Biblioteca Sur', 'Cra 80 #25-10'),
('Biblioteca Infantil', 'Calle 10 #4-55'),
('Biblioteca Moderna', 'Diagonal 60 #22-15');

INSERT INTO secciones (id_biblioteca, nombre, piso) VALUES
(1, 'Literatura Universal', 1),
(1, 'Historia', 2),
(2, 'Ciencia Ficción', 1),
(2, 'Filosofía', 2),
(3, 'Latinoamericana', 1),
(3, 'Arte', 2),
(4, 'Infantil', 1),
(4, 'Cuentos Ilustrados', 2),
(5, 'Tecnología', 1),
(5, 'Divulgación Científica', 2);

INSERT INTO libros (id_seccion, id_biblioteca, nombre, generos, prologo, isbn, autores) VALUES
(1, 1, 'Cien Años de Soledad', 'Realismo mágico', 'Una saga familiar llena de misticismo.', 9780307474728, 'Gabriel García Márquez'),
(1, 1, 'El Amor en los Tiempos del Cólera', 'Romance, Realismo mágico', 'Una historia de amor que desafía el tiempo.', 9780307389732, 'Gabriel García Márquez'),
(2, 1, 'Sapiens: De Animales a Dioses', 'Historia, Ensayo', 'Un recorrido por la historia humana.', 9780062316097, 'Yuval Noah Harari'),
(2, 1, 'Guns, Germs and Steel', 'Historia, Sociología', 'Por qué unas sociedades prosperan y otras no.', 9780393317558, 'Jared Diamond'),
(3, 2, 'Dune', 'Ciencia ficción', 'El ascenso de un líder en un planeta desértico.', 9780441172719, 'Frank Herbert'),
(3, 2, 'Fundación', 'Ciencia ficción', 'La caída y renacimiento galáctico.', 9780553293357, 'Isaac Asimov'),
(4, 2, 'Meditaciones', 'Filosofía', 'Reflexiones del emperador Marco Aurelio.', 9780140449334, 'Marco Aurelio'),
(4, 2, 'La República', 'Filosofía política', 'El ideal de una sociedad justa.', 9780140455113, 'Platón'),
(5, 3, 'Rayuela', 'Literatura latinoamericana', 'Una novela que rompe estructuras.', 9788437604947, 'Julio Cortázar'),
(5, 3, 'Pedro Páramo', 'Literatura latinoamericana', 'Una historia de un pueblo fantasmal.', 9786070728792, 'Juan Rulfo'),
(6, 3, 'Historia del Arte', 'Arte, Humanidades', 'Un vistazo global al arte.', 9780199219650, 'E.H. Gombrich'),
(6, 3, 'El Arte de la Guerra', 'Estrategia, Filosofía', 'Lecciones antiguas sobre conflicto.', 9781590302255, 'Sun Tzu'),
(7, 4, 'El Principito', 'Infantil, Filosófico', 'Un viaje lleno de enseñanzas.', 9780156012195, 'Antoine de Saint-Exupéry'),
(7, 4, 'Matilda', 'Infantil, Fantasía', 'La historia de una niña extraordinaria.', 9780142410377, 'Roald Dahl'),
(8, 4, 'Donde Viven los Monstruos', 'Cuento ilustrado', 'Un viaje al mundo de los monstruos.', 9780064431781, 'Maurice Sendak'),
(8, 4, 'El Grúfalo', 'Cuento ilustrado', 'Una historia divertida y astuta.', 9781509804757, 'Julia Donaldson'),
(9, 5, 'Clean Code', 'Tecnología, Programación', 'Cómo escribir buen código.', 9780132350884, 'Robert C. Martin'),
(9, 5, 'Eloquent JavaScript', 'Programación', 'Una introducción profunda a JavaScript.', 9781593279509, 'Marijn Haverbeke'),
(10, 5, 'Breves Respuestas a las Grandes Preguntas', 'Ciencia, Divulgación', 'Reflexiones sobre el futuro de la humanidad.', 9781984819192, 'Stephen Hawking'),
(10, 5, 'Cosmos', 'Astronomía, Divulgación', 'Un viaje por el universo.', 9780345539434, 'Carl Sagan');

