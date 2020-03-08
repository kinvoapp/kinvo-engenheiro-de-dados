import unittest
import os
from scrapy.http import Request, TextResponse
from financescrape.spiders import financenews
from financescrape.pipelines import FinancescrapePipeline
from financescrape.utils import load_b3
import re

def fake_response(file_name=None, url=None):
    """
    Create a Scrapy fake HTTP response from a HTML file.
    The file must be inside the folder 'files'.
    """
    file_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'files/', file_name))
    request = Request(url=url)
    file_reader = open(file_path, 'r')
    file_content = file_reader.read()
    file_reader.close()
    response = TextResponse(url=url, request=request, body=file_content, encoding='utf-8')
    
    return response

class TestSpider(unittest.TestCase):
    def setUp(self):
        self.spider = financenews.FinanceNews()
        self.pipeline = FinancescrapePipeline()
        
    def test_items(self):
        """
        Testing the parse function
        """
        response = fake_response(url='https://financenews.com.br/feed/', file_name='scrapy-financenews.html')

        # set here the number of items in the page
        number_of_items = 10
        items = self.spider.parse(response)
        count = 0
        for item in items:
            print(item)
            self.assertIsNotNone(item['origin'])
            self.assertIsNotNone(item['title'])
            self.assertIsNotNone(item['content'])
            count += 1

        self.assertEqual(count, number_of_items)


    def test_valid_items(self):
        """
        Verify if the downloaded news should be saved or dropped
        """
        ########## TODO: train the Spacy to recognize the entities
        # self.assertTrue(self.pipeline.title_b3_match('Veja por que as ações do IRB desabam nesta quarta-feira'))
        self.assertTrue(self.pipeline.title_b3_match('Notícia da Totvs, Telebras, Locaweb, Carrefour e da Anima'))
        # self.assertFalse(self.pipeline.title_b3_match('PIB do Brasil é destaque nesta quarta-feira'))
        



    ############# HELPER TEST FUNCTIONS
    # def test_title_analizer(self):
    #     """
    #     For a given phrase print the entities, labels, matches and scores
    #     """
    #     title_list = [
    #         'Notícia Totvs, Telebras, Locaweb, Carrefour e da Anima',
    #         'PIB do Brasil é destaque nesta quarta-feira',
    #         'Veja por que as ações do IRB desabam nesta quarta-feira'
    #     ]
    #     for title in title_list:
    #         print('-----------------------------------------------------')
    #         for ent in self.pipeline.extract_entities(title):
    #             score = 0
    #             item = ent.text
    #             label = ent.label_
    #             match = self.pipeline.match_entity(item)
    #             if match:
    #                 score = self.pipeline.calculate_score(match, item)
    #             print(f"entity:{item}, label:{label}, match:{match}, score:{score}")



