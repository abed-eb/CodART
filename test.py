"""

The main module of CodART

-changelog
-- Add C++ backend support

"""

__version__ = '0.2.0'
__author__ = 'Morteza'


import argparse

from antlr4 import *

# from refactorings.extract_class_migrated import ExtractClassRefactoringListener
from refactorings.extract_class_migrated import ExtractClassRefactoringListener
from gen.java.JavaLexer import JavaLexer
from gen.java.JavaParser import JavaParser


def main(args):
    stream = FileStream(args.file, encoding='utf8')
    lexer = JavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParser(token_stream)
    tree = parser.compilationUnit()
    my_listener = ExtractClassRefactoringListener(
        common_token_stream=token_stream, source_class='A', new_class='A_New',
        moved_fields=['h'], moved_methods=['printH']
    )

    walker = ParseTreeWalker()
    walker.walk(t=tree, listener=my_listener)

    with open('input.refactored.java', mode='w', newline='') as f:
        f.write(my_listener.token_stream_rewriter.getDefaultText())


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'./input.java')
    args = argparser.parse_args()
    main(args)
