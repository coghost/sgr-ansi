import getopt
import os
import sys
import argparse

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

import sgr_ansi as echo
from sgr_ansi import Chain


def show_all() -> None:
    for k in echo.registered:
        getattr(echo, k)()


def print_demo() -> None:
    echo.w('[SGR-ANSI colorful terminal text Demo]')
    print()
    echo.with_paragraph(end=', ')
    echo.g('{0} single style {0}'.format('=' * 16), end='\n')

    echo.B()
    echo.D()
    echo.I()
    echo.S()
    echo.U(end='\n')

    echo.k()
    echo.r()
    echo.g()
    echo.y(end='\n')
    echo.b()
    echo.m()
    echo.c()
    echo.w(end='\n\n')
    echo.with_paragraph(on=False)

    echo.BIr('{0} combined styles {0}'.format('=' * 16), end='\n')

    echo.Bg()
    echo.BDg()
    echo.BDIg()
    echo.BDISg()
    echo.BDISUg()

    echo.Bgr()
    echo.BDrg()
    echo.BDIwg()
    echo.BDISwk()
    echo.BDISUkw(end='\n\n')


def search_styles(required_key='', required_len=None) -> None:
    required_len = required_len or len(required_key)
    for i, v in enumerate(echo.registered):
        if required_key not in v:
            continue
        if len(v) == required_len:
            getattr(echo, v)()


def prt_usg():
    # echo.g(f'''USAGE: python {sys.argv[0]} -s <style_color:Bg> -t <text> -k <search_key> -l <search_len>
    # ''')
    echo.w(f"Usage: {sys.argv[0]} [-{'|-'.join('chapVstkl')}]")
    Chain().w('\t[-a] show all styles').show()
    Chain().w('\t[-c] show chained demo').show()
    Chain().w('\t[-p] show demo styles').show()
    Chain().w('\t[-s <style_color:Bg>]').show()
    Chain().w('\t[-t <text>]').show()
    Chain().w('\t[-k <key>] search a style with key, usually paired with -l').show()
    Chain().w('\t[-l <showed_style_length>] show matched length styles').show()

    print()
    echo.Bg(f'<STYLES>: {list(echo.STYLE_HELPER.keys())}', end='\n\t')
    for k, v in echo.STYLE_HELPER.items():
        getattr(echo, k)(f'{k} == {v}', end=', ')
    print()
    echo.Bg(f'<COLORS>: {list(echo.COLOR_HELPER.keys())}', end='\n\t')
    for k, v in echo.COLOR_HELPER.items():
        getattr(echo, k)(f'{k} == {v}', end=', ')
    print()
    echo.By('''\ntwo rules:
        - styles require alphabet order
        - styles go before colors
        ''')
    sys.exit(0)


def main():
    opts = None
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            'chapVs:t:k:l:',
            ['styles=', 'text=', 'all', 'key=', 'len=', 'chain']
        )
    except getopt.GetoptError:
        prt_usg()

    if not opts:
        prt_usg()

    style = text = ''
    search_key = ''
    search_len = None
    for opt, arg in opts:
        if opt == '-h':
            prt_usg()
        elif opt == '-p':
            print_demo()
            sys.exit(0)
        elif opt in ('-c', '--chain'):
            Chain().BIy('Yep,').BIUb(
                'How do you like this?'
            ).Bm('\n\t[✔]').BUg('1.').Bg('Y: yes.').Bm('\n\t[✘]').BUr('2.').Br('N: not.').show()
            sys.exit(0)
        elif opt in ('-V', '--version'):
            echo.BI(f'sgr-ansi VERSION: {echo.VERSION}')
            sys.exit(0)
        elif opt in ('-a', '--all'):
            show_all()
            sys.exit(0)
        elif opt in ('-k', '--key'):
            search_key = arg
        elif opt in ('-l', '--len'):
            search_len = int(arg)
        elif opt in ('-s', '--styles'):
            style = arg
        elif opt in ('-t', '--text'):
            text = arg

    if search_key or search_len:
        search_styles(search_key, search_len)

    if style:
        getattr(echo, style)(text)


if __name__ == '__main__':
    main()
