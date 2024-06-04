AUTHOR = 'Samuel Hulme'
SITENAME = 'Miners Online'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Path overrides

PATH = 'content'
ARTICLE_PATHS = ['blog']
ARTICLE_EXCLUDES = ['authors', 'categories', 'tags']
PAGE_PATHS = ['']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARCHIVES_URL = 'blog/'
ARCHIVES_SAVE_AS = 'blog/index.html'
ARTICLE_URL = '{slug}/' # category is part of the slug (i.e., examples)
ARTICLE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

AUTHORS_SAVE_AS = None # Not used
CATEGORIES_SAVE_AS = None # Not used
TAGS_SAVE_AS = None # Not used

PATH_METADATA = '(?P<slug>.+).rst'

M_BLOG_URL = 'blog/'

# Theme
THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['archives']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               'static/m-dark.css']
M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = ['m.css/plugins']
PLUGINS = [
    'm.abbr',
    'm.alias',
    'm.code',
    'm.components',
    'm.dox',
    'm.dot',
    'm.filesize',
    'm.gl',
    'm.gh',
    'm.htmlsanity',
    'm.images',
    'm.link',
    'm.math',
    'm.metadata',
    'm.plots',
    'm.sphinx',
    'm.qr',
    'm.vk'
]

# Theme settings

M_SITE_LOGO_TEXT = 'Miners Online'

M_LINKS_NAVBAR1 = [
    ('Blog', 'blog/', 'blog', []),
    ('Projects', '#', '[projects]', [
        ('Net Bits', 'https://netbits.minersonline.uk/en/latest/', ''),
    ]),
    ('GitHub', 'https://github.com/miners-online', 'github', [])
]

M_NEWS_ON_INDEX = ("Latest news on our blog", 3)


FORMATTED_FIELDS = ['summery', 'landing']