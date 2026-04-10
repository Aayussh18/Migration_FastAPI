import csv
import io

def parse_csv(content:str) -> list[dict]:
    reader = csv.DictReader(io.StringIO(content))
    return list(reader)
