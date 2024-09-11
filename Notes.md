
### Detail URL
```
"https://tv.apple.com/api/uts/v2/view/product/{}/?utscf=OjAAAAAAAAA~&utsk=000000000000000000&caller=web&sf=143443&v=40&pfm=web&locale=de-DE".format(entryId)
```




### INFO - file
```
{
	"id": "com.ceviixx",
	"description": "Load the metadata from the AppleTV Api",
	"version": "1.1",
	"entry_file": "run.sh",
	"type": ["movie", "tvshow"],
	"language": ["de-DE"],
	"test_example": {
		"movie": {
			"title": "--setup",
			"original_available": "1970-01-01"
		},
		"tvshow": {
			"title": "--setup",
			"original_available": "1970-01-01"
		},
		"tvshow_episode": {
			"title": "--setup",
			"original_available": "1970-01-01",
			"season": 1,
			"episode": 1
		}
	}
}

```