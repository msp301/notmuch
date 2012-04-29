#!/usr/bin/env python

import os
from distutils.core import setup

# get the notmuch version number without importing the notmuch module
version_file = os.path.join(os.path.dirname(__file__),
                            'notmuch', 'version.py')
exec(compile(open(version_file).read(), version_file, 'exec'))
assert '__VERSION__' in globals(), \
    'Failed to read the notmuch binding version number'

setup(name='notmuch',
      version=__VERSION__,
      description='Python binding of the notmuch mail search and indexing library.',
      author='Sebastian Spaeth',
      author_email='Sebastian@SSpaeth.de',
      url='http://notmuchmail.org/',
      download_url='http://notmuchmail.org/releases/notmuch-%s.tar.gz' % __VERSION__,
      packages=['notmuch'],
      keywords=['library', 'email'],
      long_description='''Overview
========

The notmuch module provides an interface to the `notmuch
<http://notmuchmail.org>`_ functionality, directly interfacing with a
shared notmuch library. Notmuch provides a maildatabase that allows
for extremely quick searching and filtering of your email according to
various criteria.

The documentation for the latest notmuch release can be `viewed
online <http://notmuch.readthedocs.org/>`_.

Requirements
------------

You need to have notmuch installed (or rather libnotmuch.so.1). Also,
notmuch makes use of the ctypes library, and has only been tested with
python >= 2.5. It will not work on earlier python versions.
''',
      classifiers=['Development Status :: 3 - Alpha',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: GNU General Public License (GPL)',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 3',
                   'Topic :: Communications :: Email',
                   'Topic :: Software Development :: Libraries'
                   ],
      platforms='',
      license='http://www.gnu.org/licenses/gpl-3.0.txt',
     )
