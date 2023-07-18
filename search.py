#!/usr/bin/env python

import webbrowser
from iterfzf import iterfzf
import re


from googlesearch import Search


def search(inp, maxRes, lang):

    res = Search(inp, number_of_results=maxRes, language=lang).as_dict()

    res_list = res['results']

    sorted_list = []
    key = ['title', 'url', 'description']
    for i in res_list:
        results = f"{i.get(key[0])} || {i.get(key[2])} || {i.get(key[1])}"

        sorted_list.append(results)

    fzf_result = iterfzf(sorted_list)

    # получаем ссылку
    get_link = re.search(
        "(?P<url>https?://[^\s]+)", fzf_result).group("url")

    webbrowser.open(get_link, new=2)  # Открывает в вашем браузере


def main():
    inp = str(input('Search\n>>>'))
    maxRes = int(input('Max results\n>>>'))
    lang = str(input('Language(ru, en)\n>>>'))

    search(inp, maxRes, lang)


if __name__ == '__main__':
    main()
