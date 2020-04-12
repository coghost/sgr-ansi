from dataclasses import dataclass
from sgr_ansi import ansi8

__all__ = [
    'Chain',
]


@dataclass
class ChainSetting:
    sep: str = ' '
    end: str = ' '
    chain_sep: str = '|'


class Chain(object):
    def __init__(self, style=''):
        """
        Chain().BIy('Yep,').BIUb('How do you like this?').Bg('\n\t✔ 1. Y: yes.').Br('\n\t✘ 2. N: not').show()
        """
        self._style = style

    def __getattr__(self, item):
        if not self._style:
            return Chain(f'{item}')
        return Chain(f'{self._style}{ChainSetting.chain_sep}{item}')

    def __str__(self):
        return self._style

    def __call__(self, param):
        return Chain(f'{self._style}{ChainSetting.chain_sep}{param}')

    def show(self):
        ansi8.with_paragraph(sep=ChainSetting.sep, end=ChainSetting.end)
        chain_styles = str(self._style).split(ChainSetting.chain_sep)
        styles = chain_styles[::2]
        text = chain_styles[1::2]
        for i, style in enumerate(styles):
            getattr(ansi8, style)(text[i])

        print()
        ansi8.with_paragraph(on=False)
