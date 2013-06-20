__version__ = '0.1.dev'
__description__ = 'Social markups for Pelican Blog Generator'


def register():
    from social import plugin
    plugin.register()
