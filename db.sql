create database bibliotecapythonc4;

use bibliotecapythonc4;

CREATE TABLE `bibliotecas`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `nombre` VARCHAR(255) NULL,
    `direccion` VARCHAR(255) NULL,
    date_create datetime default current_timestamp,
	date_update datetime default current_timestamp on update current_timestamp
);
CREATE TABLE `secciones`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_biblioteca` INT NOT NULL,
    `nombre` VARCHAR(255) NOT NULL,
    `piso` INT NOT NULL,
    date_create datetime default current_timestamp,
	date_update datetime default current_timestamp on update current_timestamp
);
CREATE TABLE `libros`(
    `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `id_seccion` INT NOT NULL,
    `nombre` VARCHAR(255) NOT NULL,
    `generos`  VARCHAR(255)  NOT NULL,
    `prologo`  VARCHAR(255)  NOT NULL,
    `isbn`  VARCHAR(255)  NOT NULL,
    `autores`  VARCHAR(255)  NOT NULL,
    `id_biblioteca` INT NOT NULL,
    date_create datetime default current_timestamp,
	date_update datetime default current_timestamp on update current_timestamp
);
ALTER TABLE
    `secciones` ADD CONSTRAINT `secciones_id_biblioteca_foreign` FOREIGN KEY(`id_biblioteca`) REFERENCES `bibliotecas`(`id`);
ALTER TABLE
    `libros` ADD CONSTRAINT `libros_id_seccion_foreign` FOREIGN KEY(`id_seccion`) REFERENCES `secciones`(`id`);
ALTER TABLE
    `libros` ADD CONSTRAINT `libros_id_biblioteca_foreign` FOREIGN KEY(`id_biblioteca`) REFERENCES `bibliotecas`(`id`);
    
    
    -- Insertar bibliotecas
INSERT INTO bibliotecas (nombre, direccion) VALUES
('Biblioteca Central de Madrid', 'Calle Alcalá 96, 28009 Madrid'),
('Biblioteca Nacional de España', 'Paseo de Recoletos 20, 28001 Madrid'),
('Biblioteca de Cataluña', 'Carrer de l''Hospital 56, 08001 Barcelona'),
('Biblioteca Regional de Andalucía', 'Calle San Fernando 4, 41004 Sevilla'),
('Biblioteca Pública de Valencia', 'Plaza Maguncia 6, 46023 Valencia');

-- Insertar secciones
INSERT INTO secciones (id_biblioteca, nombre, piso) VALUES
(1, 'Literatura Española', 1),
(1, 'Ciencia y Tecnología', 2),
(1, 'Historia y Geografía', 1),
(2, 'Fondo Antiguo', 3),
(2, 'Referencia General', 1),
(3, 'Literatura Catalana', 2),
(3, 'Arte y Diseño', 1),
(4, 'Literatura Andaluza', 1),
(4, 'Ciencias Sociales', 2),
(5, 'Literatura Valenciana', 1);

-- Insertar libros
INSERT INTO libros (id_seccion, nombre, generos, prologo, isbn, autores, id_biblioteca) VALUES
(1, 'Don Quijote de la Mancha', 'Novela Clásica', 'En un lugar de la Mancha...', 9788491053456, 'Miguel de Cervantes', 1),
(1, 'La Colmena', 'Novela Social', 'Madrid, año 1942...', 9788437603790, 'Camilo José Cela', 1),
(2, 'Breve Historia del Tiempo', 'Ciencia', 'Desde el Big Bang hasta los agujeros negros...', 9788408103859, 'Stephen Hawking', 1),
(3, 'Historia de España', 'Historia', 'La península ibérica desde la prehistoria...', 9788430609377, 'Various Authors', 1),
(4, 'Códices Medievales', 'Historia del Arte', 'Manuscritos iluminados del siglo XV...', 9788412345678, 'Anónimo', 2),
(5, 'Enciclopedia Universal', 'Referencia', 'Conocimiento general organizado...', 9788412345679, 'Various Authors', 2),
(6, 'Tirant lo Blanc', 'Novela Caballeresca', 'En las tierras de Inglaterra...', 9788447307654, 'Joanot Martorell', 3),
(7, 'Historia del Arte Catalán', 'Arte', 'Arte desde el románico hasta el modernismo...', 9788412345680, 'Josep Pijoan', 3),
(8, 'Platero y Yo', 'Poesía', 'Platero es pequeño, peludo, suave...', 9788420402683, 'Juan Ramón Jiménez', 4),
(9, 'Sociología Contemporánea', 'Ciencias Sociales', 'Análisis de la sociedad moderna...', 9788412345681, 'Various Sociologists', 4),
(10, 'Canción de Navidad', 'Teatro', 'Una adaptación valenciana del clásico...', 9788412345682, 'Charles Dickens', 5),
(2, 'El Gen Egoísta', 'Biología', 'Los genes como unidad de evolución...', 9788498924148, 'Richard Dawkins', 1),
(3, 'Arte de la Guerra', 'Estrategia', 'La guerra es de vital importancia...', 9788497648259, 'Sun Tzu', 1),
(6, 'La Plaza del Diamante', 'Novela', 'Barcelona durante la guerra civil...', 9788423347654, 'Mercè Rodoreda', 3),
(8, 'Romancero Gitano', 'Poesía', 'Verde que te quiero verde...', 9788437608962, 'Federico García Lorca', 4);

-- Datos adicionales para más variedad
INSERT INTO libros (id_seccion, nombre, generos, prologo, isbn, autores, id_biblioteca) VALUES
(1, 'Cien Años de Soledad', 'Realismo Mágico', 'Muchos años después...', 9788437604940, 'Gabriel García Márquez', 1),
(2, 'El Universo en una Cáscara de Nuez', 'Física', 'Explorando los misterios del cosmos...', 9788408069742, 'Stephen Hawking', 1),
(5, 'Archivos Históricos', 'Documentación', 'Documentos oficiales del siglo XIX...', 9788412345683, 'Gobierno de España', 2),
(7, 'Gaudí: Arquitectura y Diseño', 'Arquitectura', 'La obra del genio modernista...', 9788412345684, 'Various Architects', 3),
(9, 'Psicología de las Masas', 'Psicología', 'Comportamiento colectivo analizado...', 9788412345685, 'Gustave Le Bon', 4),
(10, 'Leyendas Valencianas', 'Folklore', 'Tradiciones y leyendas populares...', 9788412345686, 'Various Authors', 5);

SELECT * FROM bibliotecas;

SELECT DISTINCT 
		l.nombre AS titulo_libro,
		l.autores,
        b.nombre AS biblioteca,
        s.nombre AS seccion,
        s.piso
FROM libros AS l 
INNER JOIN bibliotecas AS b ON l.id_biblioteca = b.id
INNER JOIN secciones AS s ON l.id_seccion = s.id
WHERE l.nombre = 'Don Quijote de la Mancha';

SELECT * FROM secciones;