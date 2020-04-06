import getopt
import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

import ct


def show_all() -> None:
    for k in ct.registered:
        getattr(ct, k)()


def print_demo() -> None:
    ct.w('[SGR-ANSI colorful terminal text Demo]')
    print()
    ct.with_paragraph(end=', ')
    ct.g('{0} single style {0}'.format('=' * 16), end='\n')

    ct.B()
    ct.D()
    ct.I()
    ct.S()
    ct.U(end='\n')

    ct.k()
    ct.r()
    ct.g()
    ct.y(end='\n')
    ct.b()
    ct.m()
    ct.c()
    ct.w(end='\n\n')
    ct.with_paragraph(on=False)

    ct.BIr('{0} combined styles {0}'.format('=' * 16), end='\n')

    ct.Bg()
    ct.BDg()
    ct.BDIg()
    ct.BDISg()
    ct.BDISUg()

    ct.Bgr()
    ct.BDrg()
    ct.BDIwg()
    ct.BDISwk()
    ct.BDISUkw(end='\n\n')


def search_styles(required_key='', required_len=None) -> None:
    required_len = required_len or len(required_key)
    for i, v in enumerate(ct.registered):
        if required_key not in v:
            continue
        if len(v) == required_len:
            getattr(ct, v)()


def prt_usg():
    ct.g(f'''USAGE: python {__file__} -s <style_color:Bg> -t <text> -k <search_key> -l <search_len>
    ''')
    ct.By('''two rules:
    - styles require alphabet order
    - styles go before colors
    ''')
    print()
    ct.Bg('<STYLES>: use with alphabet order')
    for k, v in ct.STYLE_HELPER.items():
        ct.g(f'\t{k} == {v}')
    print()
    ct.Bg('<COLORS>: <fg> on <bg>')
    for k, v in ct.COLOR_HELPER.items():
        ct.g(f'\t{k} == {v}')
    sys.exit(0)


def main(argv):
    opts = None
    try:
        opts, args = getopt.getopt(argv, 'hapVs:t:k:l:', ['styles=', 'text=', 'all', 'key=', 'len='])
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
        elif opt in ('-V', '--version'):
            ct.BI(f'sgr-ansi VERSION: {ct.VERSION}')
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
        getattr(ct, style)(text)


if __name__ == '__main__':
    main(sys.argv[1:])
