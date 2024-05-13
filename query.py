from datetime import datetime
from elasticsearch import Elasticsearch

class LogIngestorQueryInterface:
    def __init__(self, host='localhost', port=9200):
        self.es = Elasticsearch([{'host': host, 'port': port}])

    def search_logs(self, query=None, level=None, log_string=None, timestamp=None, source=None):
        query_body = {"query": {"bool": {"must": []}}}
        
        if query:
            query_body["query"]["bool"]["must"].append({"query_string": {"query": query}})
        
        if level:
            query_body["query"]["bool"]["must"].append({"match": {"level": level}})
        
        if log_string:
            query_body["query"]["bool"]["must"].append({"match": {"log_string": log_string}})
        
        if timestamp:
            query_body["query"]["bool"]["must"].append({"range": {"timestamp": {"gte": timestamp}}})
        
        if source:
            query_body["query"]["bool"]["must"].append({"match": {"metadata.source": source}})
        
        response = self.es.search(index="logs_index", body=query_body)
        return response['hits']['hits']

# Example usage:
# Initialize the query interface
query_interface = LogIngestorQueryInterface()

# Search for logs with a specific level and log_string
logs = query_interface.search_logs(level="INFO", log_string="User logged in")

# Search for logs within a specific time range
start_time = datetime(2024, 5, 10)
end_time = datetime(2024, 5, 13)
logs = query_interface.search_logs(timestamp={"gte": start_time, "lte": end_time})

# Search for logs from a specific source
logs = query_interface.search_logs(source="app_server")
