CREATE TABLE IF NOT EXISTS genre (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS executor (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS album (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS track (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	length TIME NOT NULL,
	album_id INTEGER REFERENCES album(id)
);

CREATE TABLE IF NOT EXISTS collection (
	id SERIAL PRIMARY KEY,
	name VARCHAR(60) NOT NULL,
	release_date DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS executor_album (
	executor_id INTEGER REFERENCES executor(id),
	album_id INTEGER REFERENCES album(id),
	CONSTRAINT pk1 PRIMARY KEY(executor_id, album_id)
);

CREATE TABLE IF NOT EXISTS genre_executor (
	genre_id INTEGER NOT NULL REFERENCES genre(id),
	executor_id INTEGER NOT NULL REFERENCES executor(id),
	CONSTRAINT pk PRIMARY KEY(genre_id, executor_id)
);

CREATE TABLE IF NOT EXISTS collection_track (
	track_id INTEGER REFERENCES track(id),
	collection_id INTEGER REFERENCES collection(id),
	CONSTRAINT pk2 PRIMARY KEY(track_id, collection_id)
);
