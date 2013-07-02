# -*- coding: utf-8 -*-
"""
Social markup for reStructuredText
==================================

Directives
----------

.. code-block:: ReST

    :network:`target`
    or
    :network:`Displayed test <target>`

"""
from __future__ import unicode_literals

import re
import six

from docutils import nodes
from docutils.parsers.rst import roles
from pelican.readers import PelicanHTMLTranslator
from types import MethodType


RE_DISPLAY = re.compile(r'^(?P<display>.+?)\s*\<(?P<target>.+)\>$')

RE_GITHUB = re.compile(r'^(?P<username>[\w.-]+)(?:/(?P<repository>[\w.-]+)(?:#(?P<issue>\d+))?)?$')

# Each social network directive should appears here.
# If no custom processor is defined, an URL should be associated.
NETWORKS = {
    'twitter': 'https://twitter.com/{target}',
    'tw': '',
    'facebook': 'https://facebook.com/{target}',
    'fb': 'https://facebook.com/{target}',
    'github': 'https://github.com/{target}',
    'gh': '',
    'gplus': 'https://plus.google.com/{target}',
}


class SocialNode(nodes.Inline, nodes.TextElement):
    tagname = 'a'


class CustomProcessors:
    @classmethod
    def tw(cls, target, display=None):
        return cls.twitter(target, display)

    @classmethod
    def twitter(cls, target, display=None):
        if target.startswith('@'):
            target = target[1:]
        return NETWORKS['twitter'].format(target=target), display

    @classmethod
    def gh(cls, target, display=None):
        return cls.github(target, display)

    @classmethod
    def github(cls, target, display=None):
        match = RE_GITHUB.match(target)
        if not match:
            raise ValueError('Unparseable github target: %s' % target)
        username, repository, issue = match.groups()
        url_parts = [NETWORKS['github'].format(target=username)]
        if repository:
            url_parts.append(repository)
        if issue:
            url_parts.extend(['issues', issue])
        if not display and issue:
            display = '#%s' % issue
        else:
            display = display or repository or username
        return '/'.join(url_parts), display


def social_role(role, rawtext, text, lineno, inliner, options={}, content=[]):
    match = RE_DISPLAY.match(text)
    if match:
        target = match.group('target')
        display = match.group('display')
    else:
        target = text
        display = None
    if hasattr(CustomProcessors, role):
        url, display = getattr(CustomProcessors, role)(target, display)
    else:
        url = NETWORKS[role].format(target=target)
    return [SocialNode('', display or target, href=url)], []


def visit_SocialNode(self, node):
    self.body.append(node.starttag())


def depart_SocialNode(self, node):
    self.body.append(node.endtag())


def as_method(func):
    if six.PY3:
        return MethodType(func, PelicanHTMLTranslator)
    else:
        return MethodType(func, None, PelicanHTMLTranslator)


def register():
    for role in NETWORKS.keys():
        roles.register_canonical_role(role, social_role)

    PelicanHTMLTranslator.visit_SocialNode = as_method(visit_SocialNode)
    PelicanHTMLTranslator.depart_SocialNode = as_method(depart_SocialNode)
