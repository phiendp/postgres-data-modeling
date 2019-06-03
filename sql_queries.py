# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplay (\
                            songplay_id SERIAL PRIMARY KEY, \
                            start_time TIMESTAMP NOT NULL, \
                            user_id INT NOT NULL, \
                            level VARCHAR, \
                            song_id VARCHAR(50), \
                            artist_id  VARCHAR(50), \
                            session_id INT, \
                            location VARCHAR, \
                            user_agent TEXT);")

user_table_create = ("CREATE TABLE IF NOT EXISTS users (\
                        user_id INT PRIMARY KEY, \
                        first_name VARCHAR, \
                        last_name VARCHAR, \
                        gender VARCHAR(3), \
                        level VARCHAR);")

song_table_create = ("CREATE TABLE IF NOT EXISTS songs( \
                        song_id VARCHAR(50) PRIMARY KEY, \
                        title VARCHAR(255), \
                        artist_id VARCHAR(50), \
                        year INT, \
                        duration DOUBLE PRECISION);")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artist( \
                            artist_id VARCHAR PRIMARY KEY, \
                            name VARCHAR(127), \
                            location VARCHAR(255), \
                            lattitude FLOAT, \
                            longitude FLOAT);")

time_table_create = ("CREATE TABLE IF NOT EXISTS time(\
                        start_time TIMESTAMP, \
                        hour INT, \
                        day INT, \
                        week INT, \
                        month INT, \
                        year INT, \
                        weekday INT);")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
