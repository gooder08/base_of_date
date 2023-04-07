--Количество исполнителей в каждом жанре.
SELECT name, count(executor_id) FROM genre g  
LEFT JOIN genre_executor ge ON g.id = ge.genre_id
GROUP BY name;

--Количество треков, вошедших в альбомы 2009–2010 годах. "Тут изменил года на 2009-2010, т к 2019-2020 у меня нет"
SELECT count(name_track) FROM track t 
JOIN album a  ON a.id = t.album_id 
WHERE release_date BETWEEN '01.01.2009' AND '31.12.2010';


--Средняя продолжительность треков по каждому альбому
SELECT (name_album), date_trunc('second', avg(length)) FROM album a 
FULL JOIN track t  ON t.album_id = a.id  
GROUP BY name_album;

--Все исполнители, которые не выпустили альбомы в 1995 году. "Тут изменил год на 1995, т к 2020 у меня нет"
SELECT fio FROM executor e 
WHERE fio NOT IN (
	SELECT fio FROM executor e1 
	JOIN executor_album ea ON e1.id = ea.executor_id 
	JOIN album a ON ea.album_id = a.id
	WHERE release_date BETWEEN '01.01.1995' AND '31.12.1995'
);


--Названия сборников, в которых присутствует конкретный исполнитель (Глюкоза)
SELECT name_collection, fio FROM collection c 
FULL JOIN collection_track ct  ON ct.collection_id  = c.id
FULL JOIN track t ON t.id = ct.track_id 
FULL JOIN album a ON t.album_id = a.id 
FULL JOIN executor_album ea ON a.id = ea.album_id 
FULL JOIN executor e ON ea.executor_id = e.id 
WHERE fio LIKE 'Глюкоза';

--Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT name_album, count(name) FROM album a 
FULL JOIN executor_album ea ON a.id = ea.album_id
FULL JOIN executor e ON ea.executor_id = e.id 
FULL JOIN genre_executor ge ON e.id = ge.executor_id 
FULL JOIN genre g ON ge.genre_id = g.id 
GROUP BY name_album 
HAVING count(name)>1;

--Наименования треков, которые не входят в сборники (у меня все треки входят в сборники, поэтому пустой список)
SELECT name_track, name_collection FROM track t 
FULL JOIN collection_track ct ON t.id  = ct.track_id 
FULL JOIN collection c ON ct.collection_id = c.id 
WHERE name_collection IS NULL; 

--Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.
SELECT length, fio FROM track t 
JOIN album a ON t.album_id  = a.id 
JOIN executor_album ea ON a.id = ea.album_id 
JOIN executor e ON ea.executor_id = e.id 
WHERE length = (SELECT min(length) FROM track);

--Названия альбомов, содержащих наименьшее количество треков.
SELECT name_album, count(*) FROM album a 
JOIN track t ON a.id = t.album_id 
GROUP BY name_album
HAVING  count(*) = (SELECT count(*) FROM album a1 
	JOIN track t1 ON a1.id = t1.album_id 
	GROUP BY a1.id 
	ORDER BY 1
	LIMIT 1);
--(SELECT min(count) FROM (SELECT name_album, count(*) FROM album a1 JOIN track t1 ON a1.id = t1.album_id GROUP BY name_album) AS foo);




 



  

 











