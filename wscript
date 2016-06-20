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
GIT_SUBTREES={
    'fonts/miaounicode' : {'origin' : 'https://github.com/silnrsi/MiaoUnicode',
                            'branch' : 'master',
                            'autoupdate' : True }
}

langmap = {
   'LPO' : {'name' : 'Taogu'},
   'YCL' : {},
   'HMD' : {'sublangs' : ['HMD','HMDD', 'HMDN'], 'name' : "Shimenkan"},
   'YWQ' : {},
   'YIG' : {}
}

subfonts = {}
g = package.global_package()
for s in ('fonts/shishan', 'fonts/miaounicode/fonts/MiaoUnicode') :
    subfonts[s] = []
    for p in subdir(s) :
        g.add_package(p, s)
        for f in p.fonts :
            subfonts[s] += [os.path.join(s, out, f.target)]

for l in langmap.keys() :
    p = package(
        appname = 'Miao-' + l[0] + l[1:].lower(),
        out = 'results',
        outdir = 'exes',
        zipdr = 'zips',
	    version = VERSION,
        license = LICENSE
    )
    s = langmap[l].get('sublangs', (l, ))
    for k in s :
        cmds = []
        cmds = [cmd('ttfdeflang -d ' + k + ' ${DEP} ${TGT}'), name("ShiShan " + k, lang='en-US')]
        if os.path.exists(os.path.join('fonts/shishan/source', l+'map.cfg')) :
            cmds.append(cmd('ttfremap -c ${SRC} -r ${DEP} ${TGT}', ['fonts/shishan/source/' + k + 'map.cfg']))
        font(target=process("fonts/ShiShan-"+k+".ttf", *cmds),
            source=subfonts['fonts/shishan'][0],
            package = p)
    miaoname = langmap[l].get('name', None)
    if miaoname :
	cmds = [cmd('ttfdeflang -d ' + l + ' ${DEP} ${TGT}'), name(miaoname, lang='en-US')]
	if os.path.exists(os.path.join('fonts/miaounicode/fonts/MiaoUnicode/source', l.lower()+'map.cfg')) :
	    cmds.append(cmd('ttfremap -c ${SRC} -r ${DEP} ${TGT}', ['fonts/miaounicode/fonts/MiaoUnicode/source/' + l.lower() + 'map.cfg']))
	gdlfile = 'fonts/miaounicode/fonts/MiaoUnicode/source/' + l.lower() + '.gdl'
	font(target=process('fonts/{}.ttf'.format(miaoname), *cmds),
	     source=subfonts['fonts/miaounicode/fonts/MiaoUnicode'][0],
	     graphite=gdl(l.lower() + '.gdl', master=gdlfile, params='-d -q -w3521', make_params='-r'),
	     package=p)
    langkbds = langmap[l].get('id', [l.lower() + "Uni", ])
    for k in langkbds :
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

def configure(ctx) :
# this code to be merged into waf, use this for testing
    from subprocess import call
    try :
        for s, r in GIT_SUBTREES.items() :
            if isinstance(r, dict) and r.get('autoupdate', False) :
                cmds = ['git', 'subtree', 'pull', '-P', s,
                        '-m', 'smith auto subtree pull to ' + s, '--squash',
                        r['origin']]
                if 'branch' in r : cmds += [r['branch']]
                call(cmds)
    except :
        pass

