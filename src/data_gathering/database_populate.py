from string import Template

import pandas as pd
from database_management.database_session import DatabaseSession


class DatabasePopulate:
    @classmethod
    def load_music_styles(cls, df_music_styles: pd.DataFrame) -> None:
        database_session = DatabaseSession('', '', '')

        with database_session.driver.session() as session:
            session.write_transaction(cls.__create_all, df_music_styles)

    @classmethod
    def __create_all(cls, tx, df_music_styles: pd.DataFrame) -> None:
        string_template = Template('CREATE (style_$music_style_id: music_style {name: "$music_style_name"})')

        for _, row in df_music_styles.iterrows():
            script = string_template.substitute(music_style_id=row['id'], music_style_name=row['name'])
            tx.run(script)
