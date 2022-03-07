import json

def save_jsons(infos) -> None:
    with open('json_data.json', 'w', encoding='utf-8') as json_output:
            json.dump(infos, json_output, ensure_ascii=False)

def read_jsons() -> dict:
    with open('json_data.json', 'r', encoding='utf-8') as json_input:
        data = json.loads(json_input.read())
    return data