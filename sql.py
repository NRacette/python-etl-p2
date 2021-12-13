insert_movie = ('''
    TODO
''')

create_schema = ('''
    create schema IF NOT EXISTS petl2;
''')

create_table = ('''
    CREATE TABLE petl2.movie_list(
    title TEXT NOT NULL,
    rated TEXT NOT NULL,
    released DATE NOT NULL,
    runtime INT NOT NULL,
    genre TEXT[] NOT NULL,
    director TEXT NOT NULL,
    writer TEXT[] NOT NULL,
    actors TEXT[] NOT NULL,
    plot TEXT NOT NULL,
    awards TEXT NOT NULL,
    poster TEXT NOT NULL
    );
''')

insert_movie = ('''
    INSERT INTO petl2.movie_list (Title,Rated,Released,Runtime,Genre,Director,Writer,Actors,Plot,Awards,Poster)
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
''')
