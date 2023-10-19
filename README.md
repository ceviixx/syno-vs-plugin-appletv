# Synology Video Station Plugin
An Synology Video Station Plugin to fetch movie metdata from the `Apple TV`-API.

Synology Video Station Plugin Docu can be find [here](https://download.synology.com/download/Document/Software/DeveloperGuide/Package/VideoStation/All/enu/Synology_Video_Station_API_enu.pdf).


**If you have found an bug or need help, feel free and create an issue**


### Server Side (/server)
The index.php file fetch response from the "Apple TV"-Api and clean up the data for Synology Video Station


### Plugin (/plugin)
The Plugin receives the data from the Server Side (`index.php`) and shows result in Video Staion.
You can choose from the search results.


## Setup
1. Upload the index.php file to your server.
2. Change the IP / Hostname in the `INFO`-file in the Plugin.
3. Create an ZIP file from "`com.appletv`" and add this file to the Plugins from Video staion. *(name of zip must be the same as in the `INFO`-file)*
4. Fetch metadata using the search. :blush:



## Supported media types
- [x] Movies
- [ ] TV-Shows
- [ ] TV-Episodes


## Supported languages
- [x] German
- [ ] English
- [ ] ...


## Open tasks
- [ ] Loading speed
- [ ] Cleanup the code




## Workaround for adding plugin
- Maybe you couldn't upload the plugin with some error. Return from the server side an static serach result eg.
```json
{
    "success": true,
    "result": [
        {
            "title": "Title",
            "tagline": "Tagline",
            "original_available": "2023-10-19",
            "original_title": "Orginal title",
            "summary": "Summary",
            "certificate": "G",
            "genre": [
                "Animation",
                "Adventure",
                "Family",
                "Comedy"
            ],
            "actor": [
                "Actor"
            ],
            "director": [
                "Director"
            ],
            "writer": [
                "Writer"
            ],
            "extra": {
                "com.ceviixx": {
                    "rating": {"com.ceviixx": 7.9},
                    "poster": ["http://imageUrl.png"],
                    "backdrop": ["http://imageUrl.png"]
                }
            }
        }
    ]
}
```
After adding to Video Station was successfull you can change the server side (`index.php`) to dynamic responses.
