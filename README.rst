Social plugin for Pelican
=========================

.. image:: https://secure.travis-ci.org/noirbizarre/pelican-social.png
   :target: http://travis-ci.org/noirbizarre/pelican-social

Social directives for `Pelican`_ static blog generator.

Easy linking to social networks content through simple inline directives.

Compatibility
-------------

pelican-social is compatible with `Pelican`_ 3.2+ and Python 2.7.

Support for Python 3 will come in future releases.

Installation
------------

Install the plugin via ``pip``:

.. code-block:: bash

    ~$ pip install pelican-social

Or via ``easy_install``:

.. code-block:: bash

    ~$ easy_install pelican-social


Usage
-----

To load the plugin, you have to add it in your settings file.

.. code-block:: python

    PLUGINS = (
        'social',
    )

Once loaded you have access to social rst directives.

Each directive can be called in two forms:

.. code-block:: ReST

    :network:`target`

    :network:`Displayed text <target>`


As much as possible, the directive give a secure (``https``) link.


Twitter
~~~~~~~

You can use both ``:twitter:`` and ``:tw:`` directives to link to a `Twitter`_ profile,
they are equivalent.
Using an ``@`` in username will only change the displayed username
if a custom display is not specified.


**Exemple:**

.. code-block:: ReST

    :twitter:`username`
    :twitter:`@username`
    :twitter:`User <username>`
    :twitter:`User <@username>`

will result in:

.. code-block:: html

    <a href="https://twitter.com/username">username</a>
    <a href="https://twitter.com/username">&#64;username</a>
    <a href="https://twitter.com/username">User</a>
    <a href="https://twitter.com/username">User</a>


Google+
~~~~~~~

`Google+`_ is tricky with usernames.
If you are famous and lucky you can have a custom username in ``+MyUser`` form.
If not you will have a 21 digits identifier.


**Exemple:**

.. code-block:: ReST

    :gplus:`username`
    :gplus:`User <username>`

will result in:

.. code-block:: html

    <a href="https://plus.google.com/username">username</a>
    <a href="https://plus.google.com/username">User</a>


Github
~~~~~~

You can use both ``:github:`` and ``:gh:`` directive to link
to `github`_ profiles, repositories and issues/pull-requests
(github will autmatically redirect you to the pull-request if one is associated with the issue).

The following form are accepted:

===================  ==============================
      Target              Expected target form
===================  ==============================
profile              ``username``
repository           ``username/repository``
issue/pull-request   ``username/repository#issue``
===================  ==============================


**Exemple:**

.. code-block:: ReST

    :github:`username`
    :github:`User <username>`
    :github:`username/repository`
    :github:`Repository <username/repository>`
    :github:`username/repository#2`
    :github:`Issue #2 <username/repository#2>`


will result in:

.. code-block:: html

    <a href="https://github.com/username">username</a>
    <a href="https://github.com/username">User</a>
    <a href="https://github.com/username/repository">repository</a>
    <a href="https://github.com/username/repository">Repository</a>
    <a href="https://github.com/username/repository/issues/2">#2</a>
    <a href="https://github.com/username/repository/issues/2">Issue #2</a>


Facebook
~~~~~~~~

You can use both ``:facebook:`` and ``:fb:`` directives to link to a `Facebook`_ profile,
they are equivalent.


**Exemple:**

.. code-block:: ReST

    :facebook:`User <username>`
    :facebook:`username`


will result in:

.. code-block:: html

    <a href="https://facebook.com/username">User</a>
    <a href="https://facebook.com/username">username</a>


.. _Pelican: http://getpelican.com/
.. _Twitter: https://twitter.com/
.. _Google+: https://plus.google.com/
.. _Github: https://github.com/
.. _Facebook: https://facebook.com/
