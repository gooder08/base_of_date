INSERT INTO genre (name) VALUES ('Шансон'), ('Блюз'), ('Джаз'), ('Поп'), ('Рок');
INSERT INTO executor (name) VALUES ('Ваенга Елена'), ('Роберт Джонсон'), ('Луи Армстронг'), ('Хабиб'), ('Глюкоза'), ('Монеточка'), ('Линкин Парк'), ('Элвис Пресли');
INSERT INTO album (name, release_date) VALUES ('Белый', '05.05.2005'), ('Черный', '01.01.2009'), ('Красный', '10.6.2000'), ('Синий', '15.07.1995'), ('Оранжевый', '02.02.1995'), ('Коричневый', '01.01.2002'), ('Зеленый', '30.11.2010'), ('Голубой', '14.12.2009');
INSERT INTO track (name, length, album_id) VALUES ('Нежность', '00:03:45', 1), ('Вечная весна', '00:02:45', 1), ('Итоги', '00:03:51', 2), ('Белые розы', '00:03:50', 2), ('Осень', '00:02:50', 2), ('Лето', '00:04:45', 2), ('Темная ночь', '00:04:20', 3), ('Выхода нет', '00:03:30', 3), ('Перемен', '00:03:20', 4), ('Голоса', '00:03:10', 4), ('На заре', '00:03:05', 5), ('Солдат', '00:04:24', 5), ('Осколки', '00:02:57', 5), ('Варвара', '00:02:48', 6), ('Зима', '00:03:45', 6), ('Кресты', '00:02:09', 7), ('Юла', '00:05:01', 8);
INSERT INTO collection (name, release_date) VALUES ('Все подряд', '05.05.2005'), ('Лучшие', '07.05.2005'), ('Лучшие музыканты', '10.06.2010'), ('Лучшие песняры', '15.07.2003'), ('Любимые', '02.02.2004'), ('Пей и пой', '01.01.2006'), ('Любимые музыканты', '30.11.2011'), ('Играй гармонь', '14.12.2012');
INSERT INTO genre_executor (genre_id, executor_id) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (4, 5), (5, 6), (5, 7), (5, 8);
INSERT INTO executor_album  (executor_id, album_id) VALUES (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8);
INSERT INTO collection_track  (track_id, collection_id) VALUES (1, 1), (2, 1), (3, 1), (4, 2), (5, 2), (6, 3), (7, 3), (8, 4), (9, 4), (10, 5), (11, 5), (12, 6), (13, 6), (14, 6), (15, 7), (16, 7), (17, 8);



SELECT * FROM track

