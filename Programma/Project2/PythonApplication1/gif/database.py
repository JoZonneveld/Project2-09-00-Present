"""Postgres database interaction
Copyright 2017, Sjors van Gelderen
"""

import psycopg2


# Use the database
def interact_with_database(command):
    # Connect and set up cursor
    connection = psycopg2.connect("dbname=Battleport user=postgres")
    cursor = connection.cursor()

    # Execute the command
    cursor.execute(command)
    connection.commit()

    # Save results
    results = None
    try:
        results = cursor.fetchall()
    except psycopg2.ProgrammingError:
        # Nothing to fetch
        pass

    # Close connection
    cursor.close()
    connection.close()

    return results


# Uploads a score into the hiscore table
def upload_score(name, score):
    interact_with_database("UPDATE Highscore SET beurten = {} WHERE name = '{}'"
                           .format(score, name))


# Downloads score data from database
def download_scores():
    return interact_with_database("SELECT * FROM Highscore")


# Downloads the top score from database
def download_top_score():
    result = interact_with_database("SELECT * FROM Highscore ORDER BY beurten")[0][1]
    return result