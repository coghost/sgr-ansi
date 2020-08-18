__description__ = '''
red.bold
\x1b[7;96m Bg-Sample \x1b[0m

bold.green_on_red
\x1b[1;32m\x1b[41m Hello World \x1b[0m
'''

from functools import partial
import itertools
from typing import List

__CSI__ = '\x1b['
__RESET__ = '0m'
__DEFAULT_FG__ = 39

STYLE_HELPER = dict(B='bold', D='dimmed', I='italic', S='strike_through', U='underlined')
COLOR_HELPER = dict(k='black', r='red', g='green', y='yellow', b='blue', m='magenta', c='cyan', w='white')
HELPER = dict(**STYLE_HELPER, **COLOR_HELPER)
_STYLES_ = dict(B=1, D=2, I=3, S=9, U=4)
_COLORS_ = dict(k=30, r=31, g=32, y=33, b=34, m=35, c=36, w=37)

registered = []

prt_style = dict(end='\n', sep=' ')


def with_paragraph(on: bool = True, end='', sep='') -> None:
    _end, _sep = '\n', ' '
    if on:
        _end = _sep = ''
    _end, _sep = _end or end, _sep or sep

    prt_style['end'] = _end
    prt_style['sep'] = _sep
    __register_styles()


def __register_styles(show=True) -> None:
    styles = __reg_styles(_STYLES_, len(_STYLES_), show=show)
    colors = __reg_styles(_COLORS_, 2, iter_type='permutations', show=show)

    for sc in itertools.product(styles, colors):
        sc = ''.join(sc)
        if not show:
            sc = sc.replace("_", "")
        fn = partial(__stylish, formatter=sc, show=show)
        if not show:
            sc = f'{sc}_'
        globals()[sc] = fn
        registered.append(sc)


def __reg_styles(styles, max_length, iter_type='combinations', show=True) -> List:
    _reg = []
    for i in range(max_length):
        for style in getattr(itertools, iter_type)(styles, i + 1):
            style = ''.join(style)
            fn = partial(__stylish, formatter=style, show=show)
            if not show:
                style = f'{style}_'
            globals()[style] = fn
            _reg.append(style)
            registered.append(style)
    return _reg


def __stylish(*args, formatter='B', sep='', end='', show=True):
    alias = '-'.join([HELPER.get(x, '') for x in formatter])

    # all colors are lowercase
    colors = [x for x in formatter if x > 'Z'][-2:]
    colors = f'{__CSI__}'.join(
        [
            f'{_COLORS_.get(color) + i * 10}m' for i, color in enumerate(colors)
        ] or [f'{__DEFAULT_FG__}m']
    )

    # all styles are uppercase
    styles = [x for x in formatter if x <= 'Z']
    styles = ';'.join([f'{_STYLES_.get(x, "")}' for x in styles] or [])

    _string = [*args]
    # if no args, or with args, but args[0] is empty, use auto-gen style-alias
    if not args or not args[0]:
        _string = [f'{formatter}: {alias}']

    sep = sep or prt_style['sep']
    end = end or prt_style['end']
    if not show:
        return ''.join([f'{__CSI__}{styles};{colors}', ''.join([str(x) for x in _string]), f'{__CSI__}{__RESET__}'])
    print(f'{__CSI__}{styles};{colors}', sep='', end='')
    print(*_string, sep=sep, end='')
    print(f'{__CSI__}{__RESET__}', sep='', end=end)


def __gen_static_exported_styles__():
    for i, v in enumerate(registered, start=1):
        print(f"'{v}'", end=',' if i % 5 else ',\n')


__register_styles()
__register_styles(False)

if __name__ == '__main__':
    __gen_static_exported_styles__()
