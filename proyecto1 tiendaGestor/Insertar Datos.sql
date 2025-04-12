-- Datos de ejemplo para la tabla MANGA
INSERT INTO MANGA (Manga_name, Author_name, Genre, Publish_date, Modified_date, Estado) VALUES
('Naruto',              'Masashi Kishimoto', 'Shonen',        '1999-09-21', '2025-04-11', 1),
('One Piece',           'Eiichiro Oda',      'Adventure',     '1997-07-22', '2025-04-11', 1),
('Attack on Titan',     'Hajime Isayama',    'Dark Fantasy',  '2009-09-09', '2025-04-11', 1),
('Fullmetal Alchemist', 'Hiromu Arakawa',    'Action',        '2001-07-12', '2025-04-11', 1),
('Death Note',          'Tsugumi Ohba',      'Thriller',      '2003-12-01', '2025-04-11', 1),
('Dragon Ball',         'Akira Toriyama',    'Shonen',        '1984-12-03', '2025-04-11', 1),
('Bleach',              'Tite Kubo',         'Shonen',        '2001-08-07', '2025-04-11', 1),
('My Hero Academia',    'Kohei Horikoshi',   'Superhero',     '2014-07-07', '2025-04-11', 1),
('Jujutsu Kaisen',      'Gege Akutami',      'Dark Fantasy',  '2018-03-05', '2025-04-11', 1),
('One Punch-Man',       'ONE',               'Action',        '2009-06-14', '2025-04-11', 1);

-- Datos de ejemplo para la tabla VOLUME
INSERT INTO VOLUME (Volume_nro, Release_date, Price, Stock, Id_Manga, Modified_date, Estado) VALUES
(1, '1999-03-03', 5000, 100, 1,  '2025-04-11', 1),
(2, '1999-10-07', 5500,  80, 1,  '2025-04-11', 1),
(1, '1997-12-24', 6000, 120, 2,  '2025-04-11', 1),
(2, '1998-08-04', 6200, 110, 2,  '2025-04-11', 1),
(1, '2009-10-23', 7000,  90, 3,  '2025-04-11', 1),
(1, '2001-10-10', 6500, 100, 4,  '2025-04-11', 1),
(1, '2003-12-02', 6800,  95, 5,  '2025-04-11', 1),
(1, '1985-03-13', 4500, 150, 6,  '2025-04-11', 1),
(1, '2001-12-18', 5000, 130, 7,  '2025-04-11', 1),
(1, '2014-09-04', 7200,  75, 8,  '2025-04-11', 1);

-- Datos de ejemplo para la tabla CUSTOMER
INSERT INTO CUSTOMER (Customer_name, Customer_first_surname, Customer_second_surname, NIT,    Email,                       Customer_Birthday, Modified_date) VALUES
('Juan',   'Pérez',    'Gómez',      1234567, 'juan.perez@example.com',    '1985-05-12', '2025-04-11'),
('María',  'López',    'Rodríguez',  2345678, 'maria.lopez@example.com',   '1990-11-23', '2025-04-11'),
('Carlos', 'Martínez', 'Hernández',  3456789, 'carlos.martinez@example.com','1978-02-10', '2025-04-11'),
('Ana',    'García',   'Fernández',  4567890, 'ana.garcia@example.com',    '1995-07-30', '2025-04-11'),
('Luis',   'Sánchez',  'Jiménez',    5678901, 'luis.sanchez@example.com',  '1982-09-14', '2025-04-11'),
('Laura',  'Ramírez',  'Torres',     6789012, 'laura.ramirez@example.com', '1993-03-08', '2025-04-11'),
('Pedro',  'Flores',   'Vargas',     7890123, 'pedro.flores@example.com',  '1975-12-19', '2025-04-11'),
('Lucía',  'Mendoza',  'Castillo',   8901234, 'lucia.mendoza@example.com', '1988-06-27', '2025-04-11'),
('Miguel', 'Ortega',   'Soto',       9012345, 'miguel.ortega@example.com', '1992-01-05', '2025-04-11'),
('Sofía',  'Navarro',  'Ruiz',      1012345, 'sofia.navarro@example.com', '1987-10-15', '2025-04-11');

-- Datos de ejemplo para la tabla EMPLOYEE
INSERT INTO EMPLOYEE (Employee_name, Employee_first_surname, Employee_second_surname, Wage,  Hired_date, Email,                          Phone_number, Modified_date, Estado) VALUES
('Andrés',    'Torres',  'Molina',    30000, '2020-01-15','andres.torres@example.com',    555123456, '2025-04-11', 1),
('Patricia',  'Vega',    'Ramos',     32000, '2019-03-22','patricia.vega@example.com',    555234567, '2025-04-11', 1),
('Javier',    'Suárez',  'Cruz',      28000, '2021-06-01','javier.suarez@example.com',    555345678, '2025-04-11', 1),
('Elena',     'Morales', 'Paz',       31000, '2018-11-30','elena.morales@example.com',    555456789, '2025-04-11', 1),
('Diego',     'Ramírez', 'Díaz',      29000, '2022-02-17','diego.ramirez@example.com',    555567890, '2025-04-11', 1),
('Isabel',    'Gómez',   'Nieto',     33000, '2017-05-10','isabel.gomez@example.com',     555678901, '2025-04-11', 1),
('Raúl',      'Castro',  'Mendoza',   30000, '2020-09-05','raul.castro@example.com',      555789012, '2025-04-11', 1),
('Silvia',    'Rubio',   'León',      34000, '2016-07-25','silvia.rubio@example.com',     555890123, '2025-04-11', 1),
('Fernando',  'Hernández','Vega',     28000, '2021-12-12','fernando.hernandez@example.com',555901234,'2025-04-11', 1),
('Gabriela',  'Ortiz',   'Sánchez',   35000, '2015-04-18','gabriela.ortiz@example.com',   555012345, '2025-04-11', 1);

-- Datos de ejemplo para la tabla SALES_DETAILS
INSERT INTO SALES_DETAILS (Id_Customer, Id_Employee, Sales_date, Total_price, Modified_date) VALUES
(1,  1, '2025-01-10',  5000, '2025-04-11'),
(2,  2, '2025-01-11', 11200, '2025-04-11'),
(3,  3, '2025-01-12',  6500, '2025-04-11'),
(4,  4, '2025-01-13',  6800, '2025-04-11'),
(5,  5, '2025-01-14',  4500, '2025-04-11'),
(6,  6, '2025-01-15', 15000, '2025-04-11'),
(7,  7, '2025-01-16',  5000, '2025-04-11'),
(8,  8, '2025-01-17',  7200, '2025-04-11'),
(9,  9, '2025-01-18',  3000, '2025-04-11'),
(10,10, '2025-01-19',  8600, '2025-04-11');

-- Datos de ejemplo para la tabla SALES
INSERT INTO SALES (Id_Sales, Id_Volume, Quantity, Modified_date) VALUES
(1,  1, 1, '2025-04-11'),
(2,  2, 2, '2025-04-11'),
(3,  3, 1, '2025-04-11'),
(4,  4, 3, '2025-04-11'),
(5,  5, 1, '2025-04-11'),
(6,  6, 2, '2025-04-11'),
(7,  7, 1, '2025-04-11'),
(8,  8, 4, '2025-04-11'),
(9,  9, 1, '2025-04-11'),
(10,10, 2, '2025-04-11');
