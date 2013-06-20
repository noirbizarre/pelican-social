__version__ = '0.1'
__description__ = 'Social directives for Pelican Blog Generator'


def register():
    from social import plugin
    plugin.register()
