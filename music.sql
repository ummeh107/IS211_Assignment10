
CREATE TABLE artists(id INTEGER PRIMARY KEY, 
                     artist TEXT)

CREATE TABLE albums(id INTEGER PRIMARY KEY, 
                    title TEXT, 
                    artist_id INTEGER NOT NULL, 
                    FOREIGN KEY(artist_id) REFERENCES artists(artist_id))

CREATE TABLE songs( id INTEGER PRIMARY KEY, 
                    title TEXT, 
                    track_number INTEGER, 
                    track_length INTEGER, 
                    artist_id INTEGER NOT NULL, 
                    album_id INTEGER NOT NULL,
                    FOREIGN KEY(artist_id) REFERENCES artists(artist_id),
                    FOREIGN KEY(album_id) REFERENCES albums(album_id))