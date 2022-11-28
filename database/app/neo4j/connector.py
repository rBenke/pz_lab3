from py2neo import Graph

class Neo4jConnection:

    def __init__(self):
        self.graph = Graph("bolt://localhost:7687", auth=("neo4j", "test"))

    def run_query(self, query, params = None):
        message = self.graph.run(query, params)
        return message


if __name__=="__main__":
	conn = Neo4jConnection()
	

