# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re
import unittest

from os.path import dirname, join

from pelican import readers


RESOURCES_PATH = join(dirname(__file__), 'test-resources')

RE_EXTRACT = re.compile(r'<p>(.*?)</p>')


class TestSocial(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        super(TestSocial, self).setUp()

        import social
        social.register()

    def assert_rst_equal(self, rstfile, expectations):
        filename = join(RESOURCES_PATH, rstfile)
        content, _ = readers.read_file(filename)
        content = content.strip().replace('\n', '')
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

        match = RE_GITHUB.match('username')

        self.assertIsNotNone(match)
        self.assertEqual(match.group('username'), 'username')
        self.assertIsNone(match.group('repository'))
        self.assertIsNone(match.group('issue'))

    def test_github_regex_issue(self):
        from social.plugin import RE_GITHUB

        match = RE_GITHUB.match('username/repository')

        self.assertIsNotNone(match)
        self.assertEqual(match.group('username'), 'username')
        self.assertEqual(match.group('repository'), 'repository')
        self.assertIsNone(match.group('issue'))

    def test_github_regex_issue(self):
        from social.plugin import RE_GITHUB

        match = RE_GITHUB.match('username/repository#21')

        self.assertIsNotNone(match)
        self.assertEqual(match.group('username'), 'username')
        self.assertEqual(match.group('repository'), 'repository')
        self.assertEqual(match.group('issue'), '21')

    def test_github(self):
        expected = (
            '<a href="https://github.com/username">username</a>',
            '<a href="https://github.com/username">User</a>',
            '<a href="https://github.com/username">username</a>',
            '<a href="https://github.com/username">User</a>',
        )
        self.assert_rst_equal('github.rst', expected)

    def test_github_repository(self):
        expected = (
            '<a href="https://github.com/username/repository">repository</a>',
            '<a href="https://github.com/username/repository">Repository</a>',
            '<a href="https://github.com/username/repository">repository</a>',
            '<a href="https://github.com/username/repository">Repository</a>',
        )
        self.assert_rst_equal('github-repository.rst', expected)

    def test_github_issue(self):
        expected = (
            '<a href="https://github.com/username/repository/issues/2">#2</a>',
            '<a href="https://github.com/username/repository/issues/2">Issue #2</a>',
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
