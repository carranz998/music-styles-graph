import pandas as pd


class MusicStyles:
    @classmethod
    def gather(cls) -> pd.Series:
        s_styles = pd.read_csv('resources\\styles.csv', header=None).squeeze()

        return s_styles if isinstance(s_styles, pd.Series) else pd.Series()
