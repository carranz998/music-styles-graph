from string import Template
from typing import Iterator

import pandas as pd


class MusicStylesGathering:
    @classmethod
    def create_gathering_query(cls, df_node_attributes: pd.DataFrame, df_node_relations: pd.DataFrame) -> str:
        create_nodes_query = ' '.join(cls.__generate_node_creation_queries(df_node_attributes))
        connect_nodes_query = ' '.join(cls.__generate_node_connection_queries(df_node_relations))
        gathering_query = ' '.join([create_nodes_query, connect_nodes_query])

        return gathering_query

    @classmethod
    def __generate_node_connection_queries(cls, df_node_relations: pd.DataFrame) -> Iterator[str]:
        query_template = Template('MERGE (style$style1_id) - [:SIMILAR] -> (style$style2_id)')

        for _, row in df_node_relations.iterrows():
            yield query_template.substitute(style1_id=row['style1_id'], style2_id=row['style2_id'])
            yield query_template.substitute(style1_id=row['style2_id'], style2_id=row['style1_id'])

    @classmethod
    def __generate_node_creation_queries(cls, df_node_attributes: pd.DataFrame) -> Iterator[str]:
        query_template = Template("CREATE (style$id: style {name: '$name'})")
        
        for _, row in df_node_attributes.iterrows():
            yield query_template.substitute(id=row['id'], name=row['name'])
