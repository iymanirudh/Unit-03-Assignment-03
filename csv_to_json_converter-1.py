"""
CSV to JSON Converter
Anirudh Kakde | Roll No. 05

Reads student record data from a CSV-formatted string and converts it
into a formatted JSON string, without relying on csv.DictReader.
"""

import json


def parse_csv_text(csv_text):
    """
    Manually splits raw CSV text into a list of dictionaries.
    First line is treated as the header row; each following line
    is zipped against the header to build one record.
    """
    lines = [line for line in csv_text.strip().split("\n") if line.strip()]

    headers = lines[0].split(",")
    records = []

    for line in lines[1:]:
        values = line.split(",")
        record = dict(zip(headers, values))
        records.append(record)

    return records


def to_json_string(records):
    """Serializes a list of dictionaries into a pretty-printed JSON string."""
    return json.dumps(records, indent=4)


def display_csv(csv_text):
    print("Original CSV data:")
    print(csv_text)


def display_json(json_text):
    print("Converted JSON output:")
    print(json_text)


if __name__ == "__main__":

    student_csv = (
        "roll_no,name,branch,cgpa\n"
        "05,Anirudh Kakde,Computer Science,8.7\n"
        "12,Rhea Kulkarni,Information Technology,9.1\n"
        "19,Yash Deshmukh,Electronics,8.3\n"
    )

    display_csv(student_csv)

    records = parse_csv_text(student_csv)
    json_output = to_json_string(records)

    display_json(json_output)
