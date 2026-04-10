import xml.etree.ElementTree as ET
import re

def normalize_tag(tag: str) -> str:
    tag = tag.strip().lower()
    tag = re.sub(r'[^a-z0-9_]', '_', tag)

    if tag and tag[0].isdigit():
        tag = f"field_{tag}"

    return tag


def row_to_xml(row: dict) -> str:
    root = ET.Element("root")

    for key, value in row.items():
        tag = normalize_tag(key)
        elem = ET.SubElement(root, tag)
        elem.text = str(value) if value is not None else ""

    return ET.tostring(root, encoding="utf-8").decode()