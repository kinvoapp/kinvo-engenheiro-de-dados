from scrapy.utils.serialize import ScrapyJSONEncoder
import json
import csv
import os

def return_spider_output(output):
    """
    Encode the output into json
    """
    _encoder = ScrapyJSONEncoder(ensure_ascii=False)
    return _encoder.encode(output)


def save_finance_json(output):
    """
    Save a list of spyder's outputs into jsonlines
    """
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'files/finance.jsonl'))
    with open(path, 'w', encoding='utf-8') as outfile:
        for item in output:
            json.dump(dict(item), outfile, ensure_ascii=False)
            outfile.write('\n')
    return output


def save_b3_csv(output):
    """
    Save the B3 spyder's outputs into csv
    """
    path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'files/b3.csv'))
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        for item in output:
            writer.writerow((item['name'], item['symbol']))

    return output


def load_b3():
    """
    Read a b3 csv file and return a set with it's items.
    """
    file_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'files/b3.csv'))
    if not os.path.exists(file_path):
        raise "B3 file not found"
    b3_set = {"B3", "Bovespa"}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            b3_set |= set(line.rstrip('\n|\r').split(','))
    return b3_set


def get_finance(number):
    data = []
    json_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'files/finance.jsonl'))
    if not os.path.exists(json_path):
        raise "Finance file not found"
    with open(json_path) as f:
        for index, line in enumerate(f):
            if index == number:
                break
            data.append(json.loads(line))

    return data