-- Script de inicialización de Base de Datos - Grupo 06 USIL Cloud Computing
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(150) NOT NULL,
    codigo_alumno VARCHAR(20) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Inserción de los 5 integrantes del Grupo 06 con contraseñas cifradas mediante bcrypt (cost=12)
INSERT INTO usuarios (username, password_hash, nombre_completo, codigo_alumno) VALUES
    ('stif.cerna@cloudg06.usil.pe', '$2b$12$1GGdNeuBEXv6ijbxYk/9BuP8bDIo2WzZnSOT9K1/XQ8qEGghWA0kS', 'Stif Yoau Cerna Benites', '2311570'),
    ('miguel.cueva@cloudg06.usil.pe', '$2b$12$TzcJn/c5XIGMVGJ6fNYfNORcuSI/2B79gSv/XmlejEhzqDwUWuXXG', 'Miguel Angel Cueva Añanca', '2320408'),
    ('aaron.salyrosas@cloudg06.usil.pe', '$2b$12$mI7QY8tpJ7t5iWxu/qodn.PXSV1yHHoRKgbzRQVKg55Ot2q1ajGry', 'Aarón Alejandro Sal Y Rosas Vidal', '2312859'),
    ('luis.lopez@cloudg06.usil.pe', '$2b$12$/IAigomgnHtooY08xN6tEugWWko9gUuSct54vrej4ZIrmnj4EAdG2', 'Luis Jesus Lopez Reyes', '2313029'),
    ('cesar.valdivia@cloudg06.usil.pe', '$2b$12$Jv1d2AwOd6mVegWGXpWcJubxXjZqVyDc.4REnIagA.ffRsusn7TW.', 'Cesar Raul Valdivia Huayllas', '2313537')
ON CONFLICT (username) DO NOTHING;
