from urllib.parse import urlparse

import requests
from lxml import html


def _is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False


def get_second_degree_urls(url, max_n_urls=20):
    page = requests.get(url, timeout=120).content

    tree =  html.fromstring(page)

    valid_urls = [href
                  for href in tree.xpath('//a/@href')
                  if _is_url(href)][:max_n_urls]

    return set(valid_urls)
