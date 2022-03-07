import re

def make_dict(soup) -> dict:
    info_dict = {}
    info_dict["title"] = clear_text(soup.title.text)
    info_dict["description"] = clear_text(soup.description.text)
    info_dict["category"] = clear_text(soup.category.text)
    info_dict["pubDate"] = clear_text(soup.pubDate.text)
    return info_dict

def clear_text(text) -> str:
    text = text.replace("\n", "")
    text = text.rstrip()
    text = text.lstrip()
    return text