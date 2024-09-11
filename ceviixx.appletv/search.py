import argparse
import json

from media import movie
from media import tvshow
from media import tvshow_episode

import helper




def main(type, language: str, input, limit: int, allowguess: bool):
    locale = helper.getLocale(language)
    langCode = helper.getLangCode(language)

    r = json.dumps(input)
    loaded_r = json.loads(r)

    data = json.loads(loaded_r)
    searchString = data['title']
    searchString = searchString.replace(' ', '+')

    if type == "movie":
        return movie.metaData(searchString, langCode, locale)
    elif type == "tvshow":
        return tvshow.metaData(searchString, "1", "1", langCode, locale)
    else:
        return helper.errorData()












if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Search',
        description='Forward search query from DSVideo to AppleTV API')

    parser.add_argument('--type')
    parser.add_argument('--lang')
    parser.add_argument('--input')
    parser.add_argument('--limit')
    parser.add_argument('--allowguess')

    args = parser.parse_args()

    

    result = []

    if "--setup" in args.input:
        if args.type == "movie":
            result = movie.setupData()
        elif args.type == "tvshow":
            result = tvshow.setupData()
        elif args.type == "tvshow_episode":
            result = tvshow_episode.setupData()
        else:
            result = helper.errorDataDisplay(args.type)
    else:
        data = main(args.type, args.lang, args.input, args.limit, args.allowguess)
        result = data

    result = {
        "success": True,
        "result": result
    }

    loaded_r = json.dumps(result, ensure_ascii=False, separators=(',', ':'), indent=2)
    print(loaded_r)