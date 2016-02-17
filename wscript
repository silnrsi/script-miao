#! /usr/bin/python
# encoding: utf-8

import os

APPNAME="miao"
VERSION=1.1
TESTDIR='test'
OUTDIR='exes'
ZIPDIR='zips'
out='results'
LICENSE="fonts/shishan/OFL.txt"

langmap = {
   'LPO' : [['lpoUni']],
   'YCL' : [['yclUni']],
   'HMD' : [['hmdUni'],['HMD','HMDD', 'HMDN']],
   'YWQ' : [['ywqUni']],
   'YIG' : [['yigUni']]
}

font(
	target=process("fonts/ShiShan.ttf", name("ShiShan", lang="en-US"), name("ShiShan 狮山", lang="zh-CN")),
	source="fonts/shishan/source/ShiShan.sfd",
	ap="fonts/ShiShan.xml",
#	sfd_master="fonts/shishan/source/ShiShan.sfd",
    graphite=gdl("fonts/ShiShan.gdl", master="fonts/shishan/source/miao.gdl", params="-d -q -w3521", make_params="-r"),
#    opentype = internal(),
    opentype = fea("fonts/ShiShan.fea", master="fonts/shishan/source/ShiShan.fea", make_params="-z 8"),
    script = 'plrd'
    )
for l in langmap.keys() :
    p = package(
        appname = 'Miao-' + l[0] + l[1:].lower(),
        outdir = 'exes',
        zipdr = 'zips',
	    version = VERSION,
        license = LICENSE
    )
    if len(langmap[l]) > 1 :
        s = langmap[l][1]
    else :
        s = (l, )
    for k in s :
        cmds = [cmd('ttfdeflang -d ' + k + ' ${DEP} ${TGT}'), name("ShiShan " + k, lang='en-US')]
        if os.path.exists(os.path.join('fonts/shishan/source', l+'map.cfg')) :
            cmds.append(cmd('ttfremap -c ${SRC} -r ${DEP} ${TGT}', ['fonts/shishan/source/' + k + 'map.cfg']))
        font(target=process("fonts/ShiShan-"+k+".ttf", *cmds),
            source='fonts/ShiShan.ttf',
            package = p)
    for k in langmap[l][0] :
        sk = k.split('=')
        if len(sk) < 2 : sk.append(sk[0])
        kbd(target = 'keyboards/' + sk[0] + '.kmn',
            source = 'keyboards/' + l.lower() + "/" + sk[1] + '.kmn',
            font = 'fonts/ShiShan-' + s[0] + '.ttf',
            fontname = 'ShiShan ' + s[0],
            fontdir = 'kbdfont-' + s[0],
            package = p,
            mskbd = mskbd(langname = 'Miao', lidinstall = [0x0436])
            )

