import pandas as pd
from data_pipeline.data_gathering.neo4j_query_builder import Neo4jQueryBuilder
from database_management.database_connection import DatabaseConnection


class Application:
    def __del__(self) -> None:
        self.database_connection.close()

    def __init__(self) -> None:
        self.database_connection = DatabaseConnection('bolt://localhost:7687', 'neo4j', 'music-styles')

    def populate_database(self) -> None:
        df_nodes, df_edges = map(pd.read_csv, ('resources\\styles.csv', 'resources\\relations.csv'))
        graph_creation_query = Neo4jQueryBuilder().create_nodes(df_nodes).create_edges(df_edges).query

        if self.database_connection.driver:
            with self.database_connection.driver.session():
                self.database_connection.execute_transaction(graph_creation_query)
