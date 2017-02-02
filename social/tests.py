# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import unittest

from os.path import dirname, join

from pelican.readers import Readers
from pelican.settings import DEFAULT_CONFIG


RESOURCES_PATH = join(dirname(__file__), 'test-resources')

RE_EXTRACT = re.compile(r'<p>(.*?)</p>')


class TestSocial(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        super(TestSocial, self).setUp()

        import social
        social.register()

    def assert_rst_equal(self, rstfile, expectations):
        reader = Readers(DEFAULT_CONFIG)
        content = reader.read_file(base_path=RESOURCES_PATH, path=rstfile).content
        extracted_parts = RE_EXTRACT.findall(content)
        self.assertEqual(len(extracted_parts), len(expectations))
        for expected, extracted in zip(expectations, extracted_parts):
            self.assertEqual(extracted, expected)

    def test_twitter(self):
        expected = (
            '<a href="https://twitter.com/username">username</a>',
            '<a href="https://twitter.com/username">&#64;username</a>',
            '<a href="https://twitter.com/username">User</a>',
            '<a href="https://twitter.com/username">User</a>',
            '<a href="https://twitter.com/username">username</a>',
            '<a href="https://twitter.com/username">&#64;username</a>',
            '<a href="https://twitter.com/username">User</a>',
            '<a href="https://twitter.com/username">User</a>',
        )
        self.assert_rst_equal('twitter.rst', expected)

    def test_facebook(self):
        expected = (
            '<a href="https://facebook.com/username">User</a>',
            '<a href="https://facebook.com/username">username</a>',
            '<a href="https://facebook.com/username">User</a>',
            '<a href="https://facebook.com/username">username</a>',
        )
        self.assert_rst_equal('facebook.rst', expected)

    def test_github_regex_user(self):
        from social.plugin import RE_GITHUB

        match = RE_GITHUB.match('username.me')

        self.assertIsNotNone(match)
        self.assertEqual(match.group('username'), 'username.me')
        self.assertIsNone(match.group('repository'))
        self.assertIsNone(match.group('issue'))

    def test_github_regex_repository(self):
        from social.plugin import RE_GITHUB

        match = RE_GITHUB.match('username.me/repository-js')

        self.assertIsNotNone(match)
        self.assertEqual(match.group('username'), 'username.me')
        self.assertEqual(match.group('repository'), 'repository-js')
        self.assertIsNone(match.group('issue'))

    def test_github_regex_issue(self):
        from social.plugin import RE_GITHUB

        match = RE_GITHUB.match('username.me/repository-js#21')

        self.assertIsNotNone(match)
        self.assertEqual(match.group('username'), 'username.me')
        self.assertEqual(match.group('repository'), 'repository-js')
        self.assertEqual(match.group('issue'), '21')

    def test_github(self):
        expected = (
            '<a href="https://github.com/username.me">username.me</a>',
            '<a href="https://github.com/username">User</a>',
            '<a href="https://github.com/username-me">username-me</a>',
            '<a href="https://github.com/username_me">User</a>',
        )
        self.assert_rst_equal('github.rst', expected)

    def test_github_repository(self):
        expected = (
            '<a href="https://github.com/username.me/repository.js">repository.js</a>',
            '<a href="https://github.com/username-me/repository-js">Repository</a>',
            '<a href="https://github.com/username/repository">repository</a>',
            '<a href="https://github.com/username/repository">Repository</a>',
        )
        self.assert_rst_equal('github-repository.rst', expected)

    def test_github_issue(self):
        expected = (
            '<a href="https://github.com/username.me/repository.js/issues/2">#2</a>',
            '<a href="https://github.com/username-me/repository-js/issues/2">Issue #2</a>',
            '<a href="https://github.com/username/repository/issues/2">#2</a>',
            '<a href="https://github.com/username/repository/issues/2">Issue #2</a>',
        )
        self.assert_rst_equal('github-issue.rst', expected)

    def test_google_plus(self):
        expected = (
            '<a href="https://plus.google.com/username">username</a>',
            '<a href="https://plus.google.com/username">User</a>',
        )
        self.assert_rst_equal('google_plus.rst', expected)
