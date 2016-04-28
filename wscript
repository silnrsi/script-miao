#! /usr/bin/python
# encoding: utf-8

import os

APPNAME="miao"
VERSION=0.6
TESTDIR='test'
OUTDIR='exes'
ZIPDIR='zips'
out='results'
LICENSE="fonts/MiaoUnicode/OFL.txt"
sourcedir='fonts/MiaoUnicode/source/'

langmap = {
   'hmd' : [['hmdUni'],['Shimenkan']],
   'lpo' : [['lpoUni'],['Taogu']]
}

for l in langmap.keys():
	fontname = langmap[l][1][0]
	keyboardname = langmap[l][0][0]
	p = package(
        appname = APPNAME[0].upper() + APPNAME[1:] + '-' + l,
        outdir = 'exes',
        zipdr = 'zips',
        version = VERSION,
        license = LICENSE
    )
	cmds = [cmd('ttfdeflang -d ' + l + ' ${DEP} ${TGT}'), name(fontname, lang='en-US')]
	if os.path.exists(os.path.join(sourcedir, l+'map.cfg')) :
        	cmds.append(cmd('ttfremap -c ${SRC} -r ${DEP} ${TGT}', [sourcedir + l + 'map.cfg']))
	font(
     target=process('fonts/' + fontname + '.ttf', *cmds),
	source=sourcedir + APPNAME + '.sfd',
    graphite=gdl('fonts/' + l + '.gdl', master=sourcedir + l + '.gdl', params="-d -q -w3521", make_params="-r"),
    script = 'plrd',
    package = p
    )
