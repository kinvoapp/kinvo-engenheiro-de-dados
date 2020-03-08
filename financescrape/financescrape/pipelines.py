# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import spacy
from fuzzywuzzy import fuzz, process
from scrapy.exceptions import DropItem
from .utils import load_b3
nlp = spacy.load("pt_core_news_sm")

b3_set = load_b3()


class FinancescrapePipeline(object):

    def process_item(self, item, spider):
        """
        Process items and discard the items that do not belong to the B3 set.
        """
        title = item['title']
        match = self.title_b3_match(title)
        if match:
            return item
        else:
            raise DropItem("Not found")

        
    def title_b3_match(self, title):
        """
        Verify if an entity of the title match with one contained in the B3 set;
        """
        entities = self.extract_entities(title)
        exist=False
        for ent in entities.ents:
            exist = self.match_entity(ent.text)
            if exist:
                break
        if exist:
            return True
        else:
            return False

    def extract_entities(self, string):
        """
        Extract the entities from a given string using Spacy
        """
        return nlp(string)


    def match_entity(self, entity):
        """
        Verify if the B3 set contains an entity using fuzzy ratio match.
        If exist return the match, else return None
        """
        for item in b3_set:
            score = self.calculate_score(entity, item)
            if score > 75:
                return item

        return None

    def calculate_score(self, entity, b3_item):
        """
        Use fuzzy to calculate a score for a string match
        """
        score = fuzz.token_sort_ratio(entity, b3_item)
        return score