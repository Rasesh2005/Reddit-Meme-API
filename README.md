# Reddit Meme API
JSON API for a random meme scraped from reddit.

API Link : [https://reddit-meme-api.herokuapp.com/meme_api](https://reddit-meme-api.herokuapp.com/meme_api)

**Example Response:**

```jsonc
{

    "code": 200,
    "post_link": "https://redd.it/kadq22",
    "subreddit": "AdviceAnimals",
    "title": "The struggle is real during these trying times.",
    "url": "https://i.redd.it/di9suwomhc461.jpg",
    "ups": 22471,
    "author": "bobbydigital_ftw",
    "spoilers_enabled": true,
    "nsfw": false,
    "image_previews": [
        "https://preview.redd.it/di9suwomhc461.jpg?width=108&crop=smart&auto=webp&s=8c033387866f4a2ff608abf3f8cce8507518866c",
        "https://preview.redd.it/di9suwomhc461.jpg?width=216&crop=smart&auto=webp&s=85ea6bc35101b9fd76bbbd1c17a1df3889e21e62",
        "https://preview.redd.it/di9suwomhc461.jpg?width=320&crop=smart&auto=webp&s=263b77afd27714f155a94f15578b042f968cc688"
    ]

}
```
> Note: While using thw API always confirm that the response for `"code"` is 200, else there is some error!!!

## Custom Endpoints

### Specify count (MAX 200)

In order to get multiple memes in a single request specify the count with the following endpoint.

Endpoint: [/{count}](https://reddit-meme-api.herokuapp.com/2)

Example: [https://reddit-meme-api.herokuapp.com/2](https://reddit-meme-api.herokuapp.com/2)

Response:

```jsonc
{

    "code": 200,
    "count": 2,
    "memes": [
        {
            "post_link": "https://redd.it/kgvsku",
            "subreddit": "MemeEconomy",
            "title": "Easy Investment",
            "url": "https://i.redd.it/9xsdu34x0d661.jpg",
            "ups": 7439,
            "author": "KingEmperio",
            "spoilers_enabled": true,
            "nsfw": false,
            "image_previews": [
                "https://preview.redd.it/9xsdu34x0d661.jpg?width=108&crop=smart&auto=webp&s=f24bfe89b3946b4c9fe8d37d475582067953cafd",
                "https://preview.redd.it/9xsdu34x0d661.jpg?width=216&crop=smart&auto=webp&s=ce659a23b9983ac821b0a0a2bfe4fb2243750e08",
                "https://preview.redd.it/9xsdu34x0d661.jpg?width=320&crop=smart&auto=webp&s=c3bfb292653ab689cc0b9ce6b20371e320fc7020",
                "https://preview.redd.it/9xsdu34x0d661.jpg?width=640&crop=smart&auto=webp&s=96d04ad834466addf1a9482a17a6a1d92e5f86dd",
                "https://preview.redd.it/9xsdu34x0d661.jpg?width=960&crop=smart&auto=webp&s=e0d74c2cf387326927838cd777b54eee7eb83462",
                "https://preview.redd.it/9xsdu34x0d661.jpg?width=1080&crop=smart&auto=webp&s=b3dea7a7fc38dbfd2764a8d08af0fdf449e6e3d8"
            ]
        },
        {
            "post_link": "https://redd.it/kgfk5v",
            "subreddit": "MemeEconomy",
            "title": "How much is this meme template worth?",
            "url": "https://i.redd.it/2j5r9myud7661.jpg",
            "ups": 127,
            "author": "ABC0012300",
            "spoilers_enabled": true,
            "nsfw": false,
            "image_previews": [
                "https://preview.redd.it/2j5r9myud7661.jpg?width=108&crop=smart&auto=webp&s=879677b7b53b9612b35d04b7182edae85e778599",
                "https://preview.redd.it/2j5r9myud7661.jpg?width=216&crop=smart&auto=webp&s=f933ed1d55d0effbd196afd52cb2e755e683a9c1",
                "https://preview.redd.it/2j5r9myud7661.jpg?width=320&crop=smart&auto=webp&s=e921fb4b46920bc72efba8a477ced020a8c16c49"
            ]
        }
    ]

}
```
> Not all memes have image preview so it is suggested to use the `"url"` endpoint's result

### Specify Subreddit

By default the API grabs a random meme from '_memes_', '_dankmemes_', '_AdviceAnimals_','_MemeEconomy_' subreddits. To provide your own custom subreddit use the following endpoint.

Endpoint: [/{subreddit}](https://reddit-meme-api.herokuapp.com/wholesomememes)

Example: [https://reddit-meme-api.herokuapp.com/wholesomememes](https://reddit-meme-api.herokuapp.com/wholesomememes)

Response:

```json
{
    "code": 200,
    "post_link": "https://redd.it/kgx7gq",
    "subreddit": "wholesomememes",
    "title": "Good looking cookiea",
    "url": "https://i.redd.it/hn2axo0zed661.jpg",
    "ups": 36563,
    "author": "the_mean_guy_is_here",
    "spoilers_enabled": true,
    "nsfw": false,
    "image_previews": [
                "https://preview.redd.it/hn2axo0zed661.jpg?width=108&crop=smart&auto=webp&s=e3cf46f9200d4d9ad71ea4e8a12741b1c83aa7a9",
                "https://preview.redd.it/hn2axo0zed661.jpg?width=216&crop=smart&auto=webp&s=acee023286903da15e977b2cc62346529dec359b",
                "https://preview.redd.it/hn2axo0zed661.jpg?width=320&crop=smart&auto=webp&s=b7e9973afcb785a821b8dfd9f2e20763465653a1",
                "https://preview.redd.it/hn2axo0zed661.jpg?width=640&crop=smart&auto=webp&s=695d53f60ae2e7bb353a85a26997175904c8fbe6"
            ]
},
```

### Specify Subreddit Count (MAX 200)

In order to get a custom number of memes from a specific subreddit provide the name of the subreddit and the count in the following endpoint.

Endpoint: [/{subreddit}/{count}](https://reddit-meme-api.herokuapp.com/wholesomememes/2/)

Example: [https://reddit-meme-api.herokuapp.com/wholesomememes/2](https://reddit-meme-api.herokuapp.com/wholesomememes/2/)

Response:

```json
{

    "code": 200,
    "count": 2,
    "memes": [
        {
            "post_link": "https://redd.it/kgx7gq",
            "subreddit": "wholesomememes",
            "title": "Good looking cookiea",
            "url": "https://i.redd.it/hn2axo0zed661.jpg",
            "ups": 36563,
            "author": "the_mean_guy_is_here",
            "spoilers_enabled": true,
            "nsfw": false,
            "image_previews": [
                "https://preview.redd.it/hn2axo0zed661.jpg?width=108&crop=smart&auto=webp&s=e3cf46f9200d4d9ad71ea4e8a12741b1c83aa7a9",
                "https://preview.redd.it/hn2axo0zed661.jpg?width=216&crop=smart&auto=webp&s=acee023286903da15e977b2cc62346529dec359b",
                "https://preview.redd.it/hn2axo0zed661.jpg?width=320&crop=smart&auto=webp&s=b7e9973afcb785a821b8dfd9f2e20763465653a1",
                "https://preview.redd.it/hn2axo0zed661.jpg?width=640&crop=smart&auto=webp&s=695d53f60ae2e7bb353a85a26997175904c8fbe6"
            ]
        },
        {
            "post_link": "https://redd.it/kh1svx",
            "subreddit": "wholesomememes",
            "title": "yes yes yes",
            "url": "https://i.redd.it/upypw6gtke661.jpg",
            "ups": 1945,
            "author": "patrickpotato07",
            "spoilers_enabled": true,
            "nsfw": false,
            "image_previews": [
                "https://preview.redd.it/upypw6gtke661.jpg?width=108&crop=smart&auto=webp&s=fea3a1b77bf574dd42d9c890c56e4b99f27f3002",
                "https://preview.redd.it/upypw6gtke661.jpg?width=216&crop=smart&auto=webp&s=6d79463760e9a53be595dd95fe249390c574a03f",
                "https://preview.redd.it/upypw6gtke661.jpg?width=320&crop=smart&auto=webp&s=8738d682e8059ec5ef0cb1cecf980888cfdb33f2",
                "https://preview.redd.it/upypw6gtke661.jpg?width=640&crop=smart&auto=webp&s=70a37d8e5d9f9020942f2f85f30cb393f4e59f4f"
            ]
        }
    ]

}
```
