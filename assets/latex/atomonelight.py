"""
A custom Pygments style for Atom One Light.

To include this style:
- Place this file as
  <python-root>/dist-packages/pygments/styles/atomonelight.py
- Add the entry 'atomonelight': 'atomonelight::AtomOneLightStyle'
  into the STYLE_MAP dict of
  <python-root>/dist-packages/pygments/styles/__init__.py

Original syntax highlighting from:
https://github.com/atom/atom/blob/master/packages/one-light-syntax/
"""

from pygments.style import Style
from pygments.token import Text, Keyword, Name, Comment, Punctuation, String, Error, Literal, Number, Operator, Generic

MONO1 = '#383A42'  # hsl(230, 8%, 24%);
MONO2 = '#696C77'  # hsl(230, 6%, 44%);
MONO3 = '#A0A1A7'  # hsl(230, 4%, 64%);

HUE1 = '#0184BC'  # hsl(198, 99%, 37%); cyan
HUE2 = '#4078F2'  # hsl(221, 87%, 60%); blue
HUE3 = '#A626A4'  # hsl(301, 63%, 40%); purple
HUE4 = '#50A14F'  # hsl(119, 34%, 47%); green
HUE5 = '#E45649'  # hsl(  5, 74%, 59%); red 1
HUE52 = '#CA1243'  # hsl(344, 84%, 43%); red 2
HUE6 = '#B76B01'  # hsl(35, 99%, 36%); orange 1
HUE62 = '#CB7701'  # hsl(35, 99%, 40%);

FG = MONO1
BG = '#FAFAFA'  # hsl(230, 1%, 98%);

GUTTER = '#9D9D9F'
ACCENT = '#526EFF'  # hsl(230, 100%, 66%);


class AtomOneLightStyle(Style):
    background_color = BG
    default_style = FG

    styles = {
        Text: FG,

        Keyword: HUE3,
        Keyword.Constant: HUE6,
        # Keyword.Declaration: None,
        Keyword.Namespace: HUE3,
        # Keyword.Pseudo: None,
        # Keyword.Reserved: None,
        Keyword.Type: HUE1,

        Name: MONO1,
        Name.Attribute: HUE6,
        Name.Builtin: HUE2,
        Name.Builtin.Pseudo: HUE6,
        Name.Class: HUE62,
        Name.Constant: HUE6,
        Name.Decorator: HUE2,
        # Name.Entity: None,
        Name.Exception: HUE2,
        Name.Function: HUE2,
        Name.Function.Magic: HUE1,
        Name.Label: HUE6,
        # Name.Namespace: None,
        # Name.Other: None,
        Name.Tag: HUE5,
        Name.Variable: HUE5,

        Literal: HUE6,
        String: HUE4,
        # String.Affix: None,
        # String.Backtick: None,
        # String.Char: None,
        # String.Delimiter: None,
        # String.Doc: None,
        # String.Double: None,
        String.Escape: HUE1,
        # String.Heredoc: None,
        # String.Interpol: None,
        # String.Other: None,
        # String.Regex: None,
        # String.Single: None,
        # String.Symbol: None,

        Number: HUE6,
        # Number.Bin: None,
        # Number.Float: None,
        # Number.Hex: None,
        # Number.Integer: None,
        # Number.Integer.Long: None,
        # Number.Oct: None,

        Operator: MONO1,
        Operator.Word: HUE3,

        Punctuation: MONO1,

        Comment: f'italic {MONO3}',
        # Comment.Hashbang: None,
        # Comment.Multiline: None,
        # Comment.Preproc: None,
        # Comment.Single: None,
        Comment.Special: HUE3,

        Generic: FG,
        Generic.Deleted: MONO3,
        Generic.Emph: f'italic {FG}',
        Generic.Error: HUE5,
        Generic.Heading: f'bold {FG}',
        # Generic.Inserted: None,
        # Generic.Output: None,
        # Generic.Prompt: None,
        Generic.Strong: f'bold {FG}',
        # Generic.Subheading: None,
        Generic.Traceback: f'italic {HUE6}',
    }

