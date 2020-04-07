import getopt
import os
import sys

app_root = '/'.join(os.path.abspath(__file__).split('/')[:-2])
sys.path.append(app_root)

import sgr_ansi as echo


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
    echo.g(f'''USAGE: python {__file__} -s <style_color:Bg> -t <text> -k <search_key> -l <search_len>
    ''')
    echo.By('''two rules:
    - styles require alphabet order
    - styles go before colors
    ''')
    print()
    echo.Bg('<STYLES>: use with alphabet order')
    for k, v in echo.STYLE_HELPER.items():
        echo.g(f'\t{k} == {v}')
    print()
    echo.Bg('<COLORS>: <fg> on <bg>')
    for k, v in echo.COLOR_HELPER.items():
        echo.g(f'\t{k} == {v}')
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
    main(sys.argv[1:])
