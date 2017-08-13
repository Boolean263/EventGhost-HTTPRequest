#!/bin/bash

SRCFILE="HTTPRequest/__init__.py"
sed -n -E \
    -e '1,/^eg\.RegisterPlugin/d' \
    -e '/^\)$/,$d' \
    -e 's/^ *//' \
    -e "s/ \"/ u'/" \
    -e "s/\",/'/" \
    -e '/^(name|author|version|url|guid|description)/p' \
    $SRCFILE > info.py
VERSION=`grep ^version info.py | cut -d\' -f2`

zip -r HTTPRequest-$VERSION.egplugin info.py HTTPRequest \
    -x '*.pyc' -x '.*.sw*'
