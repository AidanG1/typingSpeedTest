from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
import json, requests
from bs4 import BeautifulSoup
from random import choice

read_data = ''
with open('main/api-key.txt') as f:
    read_data = f.read()  # api key must be read from text file so it isn't in the code


def get_text_to_type(request):
    article_type = request.GET.get('type', '')

    def get_url_top_story():
        '''
            List of options for top story type:
            arts, automobiles, books, business, fashion, food, health, home, insider, magazine, movies, nyregion,
            obituaries, opinion, politics, realestate, science, sports, sundayreview, technology, theater, t-magazine,
            travel, upshot, us, world
        '''
        url = f"https://api.nytimes.com/svc/topstories/v2/{request.GET.get('top_story_category', '')}.json?api-key={read_data}"
        r = requests.get(url)
        article_choice = choice(r.json()['results'])
        article_url = article_choice['url']
        byline = article_choice['byline']
        title = article_choice['title']
        return {'article_url': article_url, 'byline': byline, 'title': title}

    if article_type == 'top_stories':  # written like this because currently top story is the only type supported but this will be easy to change later
        article = get_url_top_story()
    else:
        article = get_url_top_story()
    soup = BeautifulSoup(requests.get(article['article_url']).content, 'html.parser')
    paragraphs = []
    while len(paragraphs) == 0:
        paragraphs = soup.find_all(class_='css-axufdj')
    paragraph_choice = choice([paragraph.contents for paragraph in paragraphs])[0]
    while '<' in paragraph_choice:
        paragraph_choice = choice([paragraph.contents for paragraph in paragraphs])[0]
    return HttpResponse(json.dumps(
        {'paragraph': paragraph_choice, 'byline': article['byline'], 'title': article['title'],
         'url': article['article_url']}), content_type='application/json')


class Test(TemplateView):
    template_name = 'test.html'
