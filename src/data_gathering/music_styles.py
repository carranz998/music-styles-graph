import pandas as pd


class MusicStyles:
    @classmethod
    def gather(cls) -> pd.DataFrame:
        df_music_styles = pd.read_csv('resources\\styles.csv')

        return df_music_styles
