```
synoExtraItem = {
    "com.ceviixx": {
        "rating": {
            "com.cevixx": 1.0
        },
        "poster": [posterUrl],
        "backdrop": [backdropUrl]
    }
}
```
```
# original_available > releaseDate
synoEntryItem = {
    "title": item["title"],
    "tagline": "",
    "original_available": "2024-01-01",
    "original_title": "",
    "summary": item["description"],
    "certificate": item["rating"]["displayName"],
    "genre": [],
    "actor": [],
    "director": [],
    "writer": [],
    "extra": synoExtraItem
}
```

Detail URL\
infoURL = 'https://tv.apple.com/api/uts/v2/view/product/{}/?utscf=OjAAAAAAAAA~&utsk=000000000000000000&caller=web&sf=143443&v=40&pfm=web&locale=de-DE'.format(entryId)