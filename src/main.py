from data_gathering.database_populate import DatabasePopulate
from data_gathering.music_styles import MusicStyles
from database_management.database_session import DatabaseSession

if __name__ == '__main__':
    df_music_styles = MusicStyles.gather()
    print(df_music_styles)

    database_session = DatabaseSession('bolt://localhost:7687', 'neo4j', 'music-styles')
    database_populate = DatabasePopulate.load_music_styles(df_music_styles)
    database_session.close()
