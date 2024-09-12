
### getLocale(value)
def getLocale(value):
    if value == "dan":
        return "da-DK"
    elif value == "ger":
        return "de-DE"
    elif value == "enu":
        return "en-US"
    elif value == "spn":
        return "es-ES"
    elif value == "fre":
        return "fr-FR"
    elif value == "ita":
        return "it-IT"
    elif value == "hun":
        return "hu-HU"
    elif value == "nld":
        return "nl-NL"
    elif value == "nor":
        return "nn-NO"
    elif value == "plk":
        return "pl-PL"
    elif value == "ptg":
        return "pt-PT"
    elif value == "ptb":
        return "pt-PT"
    elif value == "sve":
        return "se-SE"
    elif value == "trk":
        return "tr-TR"
    elif value == "csy":
        return "cs-CZ"
    elif value == "rus":
        return "ru-RU"
    elif value == "tha":
        return "th-TH"
    elif value == "jpn":
        return "ja-JP"
    elif value == "chs":
        return "zh-CN"
    elif value == "krn":
        return "zh-TW"
    elif value == "krn":
        return "ko-KR"
    else:
        return "-"

### getLangCode(value)
def getLangCode(value):
    if value == "dan":
        return "143458"
    elif value == "ger":
        return "143443"
    elif value == "enu":
        return "143441"
    elif value == "spn":
        return "143454"
    elif value == "fre":
        return "143442"
    elif value == "ita":
        return "143450"
    elif value == "hun":
        return "143482"
    elif value == "nld":
        return "143452"
    elif value == "nor":
        return "143457"
    elif value == "plk":
        return "143478"
    elif value == "ptg":
        return "143453"
    elif value == "ptb":
        return "143453"
    elif value == "sve":
        return "143456"
    elif value == "trk":
        return "143480"
    elif value == "csy":
        return "143443" # <<<< TO DO
    elif value == "rus":
        return "143469" 
    elif value == "tha":
        return "143443" # <<<< TO DO
    elif value == "jpn":
        return "143462"
    elif value == "chs":
        return "143465"
    elif value == "krn":
        return "143466"
    elif value == "krn":
        return "143466"
    else:
        return "-"

### errorData()
def errorData():
    synoRes = []
    synoExtraItem = {
        "ceviixx.appletv": {
            "rating": {
                "com.rottentomatoes": 10.0
            },
            "poster": ["https://localhost/test.jpg"],
            "backdrop": ["https://localhost/test.jpg"]
        }
    }
    synoEntryItem = {
        "title": "ERROR",
        "tagline": "",
        "original_available": "1970-01-01",
        "original_title": "ERROR",
        "summary": "ERROR",
        "certificate": "",
        "genre": ["GENRE"],
        "actor": ["ACTOR"],
        "director": ["DIRECTOR"],
        "writer": ["WRITER"],
        "extra": synoExtraItem
    }
    
    synoRes.append(synoEntryItem)
    return synoRes

### errorDataDisplay(requestType)
def errorDataDisplay(requestType):
    synoExtraItem = {
        "ceviixx.appletv": {
            "rating": {
                "com.rottentomatoes": 2.0
            },
            "poster": ["http://localhost.com/test.jpg"],
            "backdrop": ["http://localhost.com/test.jpg"]
        }
    }
    synoEntryItem = {
        "title": requestType,
        "tagline": "",
        "original_available": "2024-01-01",
        "original_title": "TITLE",
        "summary": "DESCRIPTION",
        "certificate": "FSK12",
        "genre": ["GENRE"],
        "actor": ["ACTOR"],
        "director": ["DIRECTOR"],
        "writer": ["WRITER"],
        "extra": synoExtraItem
    }
    return [synoEntryItem]
