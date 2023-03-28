--1. Название и год выхода альбомов, вышедших в 2018 году.
SELECT name, release_date FROM album
WHERE release_date >= '01.01.2018' AND release_date <= '31.12.2018';

--2. Название и продолжительность самого длительного трека.
SELECT name, length FROM track
ORDER BY length DESC
LIMIT 1;

--3. Название треков, продолжительность которых не менее 3,5 минут.
SELECT name FROM track
WHERE length > '00:03:30'

--4. Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT name FROM collection
WHERE release_date >= '01.01.2018' AND release_date <= '31.12.2020'

--5. Исполнители, чьё имя состоит из одного слова.
SELECT name FROM executor
WHERE name NOT LIKE '% %'

--6. Название треков, которые содержат слово «Весна» или «Лето».
SELECT name FROM track
WHERE name LIKE '%Лето%' or name LIKE '%Зима%'



