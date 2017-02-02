__version__ = '0.2.1.dev'
__description__ = 'Social directives for Pelican Blog Generator'


def register():
    from social import plugin
    plugin.register()
