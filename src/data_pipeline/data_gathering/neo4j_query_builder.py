from string import Template
from typing import Iterator

import pandas as pd

class Neo4jQueryBuilder:
    def __init__(self):
        self.query = ''

    def create_nodes(self, df_nodes: pd.DataFrame):
        nodes_creation_query = ' '.join(self.__generate_node_queries(df_nodes))
        self.query = self.query + ' ' + nodes_creation_query

        return self

    def create_edges(self, df_edges: pd.DataFrame):
        edges_creation_query = ' '.join(self.__generate_edge_queries(df_edges))
        self.query = self.query + ' ' + edges_creation_query

        return self

    def __generate_node_queries(self, df_nodes: pd.DataFrame) -> Iterator[str]:
        template_query = Template('CREATE (style$id: style {name: "$name"})')
        
        for _, row in df_nodes.iterrows():
            yield template_query.substitute(id=row['id'], name=row['name'])

    def __generate_edge_queries(self, df_edges: pd.DataFrame) -> Iterator[str]:
        template_query = Template('MERGE (style$style1_id) - [:SIMILAR] -> (style$style2_id)')

        for _, row in df_edges.iterrows():
            yield template_query.substitute(style1_id=row['style1_id'], style2_id=row['style2_id'])
            yield template_query.substitute(style1_id=row['style2_id'], style2_id=row['style1_id'])
