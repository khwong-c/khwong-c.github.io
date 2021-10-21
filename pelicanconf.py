AUTHOR = 'Kin Hin, Wong'
SITENAME = 'Now is better than never'
SITEURL = ''
THEME = 'themes/pelican-alchemy/alchemy'
PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'
DEFAULT_DATE = 'fs'
DATE_FORMATS = { 'en' : '%d-%m-%Y' }
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          )

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
ICONS = (
    ('github', 'https://github.com/khwong-c'),
)

DEFAULT_PAGINATION = 4

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Plugins 
PLUGIN_PATHS = [ 'plugins' ]
PLUGINS = ['pelican-bootstrapify']

# Bootstrap
BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
}
BOOTSTRAP_CSS = 'https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.1.3/darkly/bootstrap.min.css'
#BOOTSTRAP_CSS = 'https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.1.3/cyborg/bootstrap.min.css'

# Themes
SITESUBTITLE = 'Until it is too late.'
SITEIMAGE = 'images/MarisaFigure.png width=240 height=240'
# DESCRIPTION = ''

#THEME_CSS_OVERRIDES = ['theme/css/oldstyle.css']
PYGMENTS_STYLE = 'paraiso-dark'
HIDE_AUTHORS = True
# RFG_FAVICONS = True

