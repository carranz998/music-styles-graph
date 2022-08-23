import pandas as pd

from data_gathering.music_styles_gathering import MusicStylesGathering
from database_management.database_connection import DatabaseConnection

if __name__ == '__main__':
    df_music_styles = pd.read_csv('resources\\styles.csv')
    df_relations = pd.read_csv('resources\\relations.csv')

    database_connection = DatabaseConnection(uri='bolt://localhost:7687', user='neo4j', password='music-styles')

    with database_connection.driver.session():
        gathering_query = MusicStylesGathering.create_gathering_query(df_music_styles, df_relations)
        database_connection.execute_transaction(gathering_query)

    database_connection.close()
