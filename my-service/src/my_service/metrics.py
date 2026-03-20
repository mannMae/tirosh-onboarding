from prometheus_client import Counter, generate_latest

request_counter = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["path"]
)