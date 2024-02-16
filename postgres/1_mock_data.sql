INSERT INTO users (id, name, email, password, created, updated, role, email_token, verified, token, token_expiration) 
VALUES 
(1, 'Joan Pérez', 'joan@example.com', 'pbkdf2:sha256:600000$6z4jAvFXNwcxn9Q5$abc08131fa0b2030fbf75e26e608de0a4f15f8d4d679368ad9f8089bf53151a6', '2023-10-21 17:34:08', '2023-10-21 17:34:08', 'wanner', null, 0, null, null),
(2, 'Anna García', 'anna@example.com', 'pbkdf2:sha256:600000$BDJqMsf8jNsmQB18$fc91cabe5f91b9d052b4bdd965c4d317672465c5ee8c6c64ddff668b493bf083', '2023-10-21 17:34:08', '2023-10-21 17:34:08', 'wanner', null, 0, null, null),
(3, 'Elia Rodríguez', 'elia@example.com', 'pbkdf2:sha256:600000$kvVELaReafDkeTAp$d0f62563dfc57b8323a5cb8ffe1e41206b08ef005a0e8297da18f1b32c4c685c', '2023-10-21 17:34:08', '2023-10-21 17:34:08', 'wanner', null, 0, null, null),
(4, 'Mike Raft', 'test@test.com', 'pbkdf2:sha256:600000$VylDVPix4kMiTM6h$d3fd33bfe10c2892170a1af6382bd3a3757441ee5cc047de7cad4beb42f4b04a', '2023-11-19 17:00:08', '2023-11-19 17:00:08', 'admin', null, 0, null, null),
(5, 'Olivette Garlett', 'ogarlett4@storify.com', 'pbkdf2:sha256:600000$cKf75v82ZkXNllaE$9928eccb90a247d3d7a6203afd5f9050032939cd3b50ca2b0793f96dd81521a9', '2022-01-24 22:34:48', '2023-02-28 12:11:50', 'wanner', null, 0, null, null),
(6, 'Cristy Varnham', 'cvarnham5@usatoday.com', 'pbkdf2:sha256:600000$Ojqq0FcmtCQ5jt3j$c13d761b938a1826df7e896fc4ddfaaa1de8d32b49ac87c1e6151fb2e051d6e3', '2022-10-09 06:24:43', '2022-04-17 17:22:52', 'wanner', null, 0, null, null),
(7, 'Jordan Sesons', 'jsesons6@phoca.cz', 'pbkdf2:sha256:600000$EgTRimnHDi3WEcdQ$d26b32f744bc68731a7ee360c23377fc6d2c242f48a9f40816b81a121ecdf113', '2023-07-12 17:30:49', '2022-07-06 19:17:17', 'wanner', null, 0, null, null),
(8, 'Louie Normanville', 'lnormanville7@reddit.com', 'pbkdf2:sha256:600000$vDaRgIhUVQlkaNeN$524435d1495183115ed4c0c0cab6b7937df3e0f8e6705e4d2211492c28e0930e', '2022-12-15 14:07:01', '2022-01-30 19:11:06', 'wanner', null, 0, null, null),
(9, 'Dagny Heritege', 'dheritege8@google.pl', 'pbkdf2:sha256:600000$FhGT9zznurM7KyjA$f9d22b40706908f1293d7e77409a2291e420f33f455534a551d32df6981ff7da', '2022-01-29 00:08:18', '2023-02-24 06:05:46', 'wanner', null, 0, null, null),
(10, 'Neille Humphery', 'nhumphery9@bbc.co.uk', 'pbkdf2:sha256:600000$ptPkiqFFpwylu6iv$dcae7d089d9fbacbd7d13fc0edcabc5a95032159047dd33f8c225c5a2678eac5', '2023-03-10 21:17:51', '2022-06-10 08:31:59', 'wanner', null, 0, null, null),
(11, 'marti', 'msolert@fp.insjoaquimmir.cat', 'scrypt:32768:8:1$QHs8OMy9kmSLOI5N$303e51cdc5ac1aad5e98b8fa808d64698685c0493560220a5b716593ec5983ab06d62eeb160264f1d7fb61bd2ba4bb60036b07b6aa80279ef19f6584724d1989', '2023-11-20 17:00:29', '2023-11-20 17:00:29', 'moderator', null, 0, null, null);

INSERT INTO categories (id, name, slug) 
VALUES 
(1, 'Electrònica', 'electronica'),
(2, 'Roba', 'roba'),
(3, 'Joguines', 'joguines'),
(4, 'Electrodomèstics', 'electrodomestics'),
(5, 'Esports', 'esports'),
(6, 'Decoració', 'decoracio'),
(7, 'Cuina', 'cuina'),
(8, 'Productes de la llar', 'prod_llar'),
(9, 'Eines', 'eines'),
(10, 'Literatura', 'literatura');

INSERT INTO blocked_users (user_id, message, created) 
VALUES 
(1, ' You suck', '2023-12-15 14:35:06');

INSERT INTO products (id, title, description, photo, price, category_id, seller_id, created, updated, status_id) 
VALUES 
(1, 'Telèfon mòbil', 'Telèfon mòbil de la marca Nokia, indestructible', 'no_image.png', 599.99, 1, 1, '2023-10-21 17:34:08', '2024-02-09 16:06:11', null),
(2, 'Samarreta', 'Una samarreta de cotó de color blau.', 'no_image.png', 19.99, 2, 2, '2023-10-21 17:34:08', '2023-10-21 17:34:08', null),
(3, 'Ninot de peluix', 'Un ninot de peluix suau.', 'no_image.png', 9.99, 3, 3, '2023-10-21 17:34:08', '2023-10-21 17:34:08', null),
(4, 'Telèfon mòbil', 'Model antic de telèfon mòbil de la marca Nokia, indestructible', 'no_image.png', 499.99, 1, 4, '2022-05-13 00:01:47', '2024-02-15 16:18:01', null),
(5, 'Raqueta de pàdel', 'Raqueta de pàdel de segona ma, en perfecte estat.', 'no_image.png', 12.84, 5, 5, '2022-07-27 04:43:26', '2022-06-22 10:24:19', null),
(6, 'Portaespelmes', 'Portaespelmes de petites dimensions per decoració.', 'no_image.png', 4.88, 6, 6, '2023-03-05 08:58:43', '2023-09-06 17:49:01', null),
(7, 'Sandwitxera elèctrica', 'Grill elèctric per tostar sandwitxos, encara funciona.', 'no_image.png', 45.13, 7, 7, '2023-06-29 22:12:36', '2022-01-31 07:30:32', null),
(8, 'Escombra', 'Escombra per neteja de la llar en bon estat.', 'no_image.png', 31.97, 8, 8, '2023-07-22 03:56:12', '2022-10-04 09:52:57', null),
(9, 'Set de tornavisos', 'Maletí amb tornavisos de diferents diàmetres.', 'no_image.png', 12.6, 9, 9, '2023-08-23 12:59:55', '2023-02-15 21:11:03', null),
(10, 'ultrices posuere cubilia', 'Diccionari de la llengua catalana.', 'no_image.png', 55.52, 10, 10, '2023-08-18 12:32:35', '2022-08-27 00:45:21', null);

INSERT INTO banned_products (product_id, reason, created) 
VALUES 
(1, 'Lame product', '2023-12-12 17:46:53');

INSERT INTO orders (id, product_id, buyer_id, offer, created) 
VALUES 
(1, 1, 1, 10.9, '2023-10-21 17:34:08'),
(2, 2, 1, 6.99, '2023-10-21 17:34:08'),
(3, 3, 3, 12.99, '2023-10-21 17:34:08');

