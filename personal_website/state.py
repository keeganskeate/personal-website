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
          "url": "https://www.linkedin.com/in/keegan-skeate-2181b1bb",
        },
        {
            "title": "StackOverflow",
            "url": "http://stackoverflow.com/users/5021266/keegan-skeate",
        }
    ]
}

homepage = {
    "blurb": "Economist, software developer, and data scientist currently available for employment. You can feel free to contact me anytime.",
    "hero": {
        "action": "Request a project",
        "title": "Data scientist, software developer, and economist.",
        "message": "With 9 years of economics, data science, and software development under my belt, I can create brilliant websites, software, and applications for you in a short amount of time.",
        "url": "/contact",
    },
    "featured_posts": [
        {
            "category": "Logo",
            "title": "Logo for Myong Sae",
            "description": "A logo designed for Myong Sae, Salon and Beauty Spa.",
            "written_at": "Oct. 25, 2020",
            "url": "posts/2020/10/25/myong-sae-logo",
        },
        {
            "category": "Website",
            "title": "ETCH Mobility Website",
            "description": "A Django website for a business to government business implementing action items of the Thurston County Climate Mitigation Plan.",
            "written_at": "Oct. 25, 2020",
            "url": "posts/2020/10/25/etch-mobility",
        },
        # {
        #     "category": "Python",
        #     "title": "Creating a Django Website and Hosting it with Firebase",
        #     "description": "Ever since I learned Python, I've wanted to create a website with Python. This site is built with Python Django and is open source, so, you can clone this website and tinker with it to your heart's content.",
        #     "written_at": "Oct. 18, 2020",
        #     "url": "posts/2020/10/18/creating-a-django-website-and-hosting-it-with-firebase",
        # },
    ],
}
posts = {
    "post_index": [
        {
            "title": "October 2020",
            "url": "posts/2020/10",
        },
    ],
    "posts": [
        {
            "title": "Creating a Website with Python's Django and Hosting it with Firebase",
            "url": "posts/2020/10/18/creating-a-django-website-and-hosting-it-with-firebase",
            "written_at": "October 18th, 2020",
        },
    ]
}

header = {
    "action": {
        "title": "Portfolio",
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
            "title": "Writing",
        },
    ]
}

footer = {
    "index": [
        {
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
            "group": "Portfolio",
            "links": [
                {
                    "title": "Business Website",
                    "url": "business-website",
                },
                {
                    "title": "Cannlytics",
                    "url": "cannlytics",
                },
                {
                    "title": "CoverLetter AI",
                    "url": "coverletter-ai",
                },
                {
                    "title": "SkateClipper",
                    "url": "skateclipper",
                },
            ],
        },
        {
            "group": "About",
            "links": [
                {
                    "title": "Story",
                    "url": "about",
                    "hashtag": "story",
                },
                {
                    "title": "Education",
                    "url": "about",
                    "hashtag": "education",
                },
                {
                    "title": "Experience",
                    "url": "about",
                    "hashtag": "experience",
                },
                {
                    "title": "Contact",
                    "url": "contact",
                },
            ],
        },
    ]
}
