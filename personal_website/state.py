"""
State Variables

TODO: Save in database and retrieve and load.
"""

state = {
    "author": "Keegan Skeate",
    "email": "keeganskeate@gmail.com",
    "phone": "828 406-0839",
    "phone_number": "18284060839",
    "social": [
        { 
          "title": "GitHub",
          "url": "https://github.com/keeganskeate",
        },
        { 
          "title": "Twitter",
          "url": "https://twitter.com/KeeganSkeate",
        },
        { 
          "title": "LinkedIn",
          "url": "https://twitter.com/KeeganSkeate",
        },
    ]
}

homepage = {
    "blurb": "Economist, software developer, and data scientist currently available for employment. You can feel free to contact me anytime.",
    "hero": {
        "action": "Hire me!",
        "title": "Economist, software developer, and data scientist looking for work.",
        "message": "With almost 9 years of economics, data science, and software development experience, I could begin building valuable assets for you immediately.",
        "url": "/contact",
    },
    "featured_posts": [
        {
            "category": "Python",
            "title": "Creating a Django Website and Hosting it with Firebase",
            "description": "Ever since I learned Python, I've wanted to create a website with Python. This site is built with Python Django and is open source, so, you can clone this website and tinker with it to your heart's content.",
            "written_at": "Oct. 18, 2020",
            "url": "posts/2020/10/18/creating-a-django-website-and-hosting-it-with-firebase",
        }
    ],
    "post_index": [
        {
            "title": "October 2020",
            "url": "posts/2020/10",
        },
    ],
    "posts": [
        {
            "title": "Creating a Django Website and Hosting it with Firebase",
            "url": "posts/2020/10/18/creating-a-django-website-and-hosting-it-with-firebase",
            "written_at": "October 18th, 2020",
        },
    ]
}

header = {
    "action": {
        "title": "Free Software",
        "url": "software",
    },
    "nav_items": [
        {
            "slug": "about",
            "title": "About",
        },
        {
            "slug": "contact",
            "title": "Contact",
        },
        {
            "slug": "posts",
            "title": "Blog",
        },
    ]
}

footer = {
    "index": [
        {
            "slug": "posts",
            "group": "Recent Posts",
            "links": [
                {
                    "title": "Creating a Django Website and Hosting it with Firebase",
                    "url": "contact",
                    "path": ""
                },
            ],
        },
        {
            "slug": "software",
            "group": "Software",
            "links": [
                {"title": "CoverLetter AI", "url": "coverletter-ai"},
            ],
        },
        {
            "slug": "about",
            "group": "About",
            "links": [
                {
                    "title": "Art",
                    "url": "about",
                    "path": "",
                    "hashtag": "art",
                },
            ],
        },
    ]
}
