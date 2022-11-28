from connector import Neo4jConnection
from tqdm import tqdm
import numpy as np

def main():
    N_NODES = 1_000_000
    N_EDGES = 10_000_000
    conn = Neo4jConnection()
    #CREATE CONSTRAINT unique_id FOR ( n:Node ) REQUIRE (n.id) IS UNIQUE;
    def partition(lst, n):
        division = len(lst) / n
        return [lst[round(division * i):round(division * (i + 1))] for i in range(n)]

    conn.run_query(f"UNWIND $props as map CREATE (n:Node) SET n.id=map", {"props": list(range(N_NODES))})

    edges = list(zip(np.random.randint(0,N_NODES-1, N_EDGES).tolist(),np.random.randint(0,N_NODES-1, N_EDGES).tolist()))
 
    for edge_lst in tqdm(partition(edges, 1000)):
        print(edge_lst)
        conn.run_query(f"UNWIND $props as map MATCH (n1:Node),(n2:Node) WHERE n1.id=map[0] and n2.id=map[1] CREATE (n1)-[r:REL]->(n2)", {"props": edge_lst})
        break        


if __name__=="__main__":
    main()
