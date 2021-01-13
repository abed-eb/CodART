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
from refactorings.merge_package import MergePackageRecognizerListener
from gen.java.JavaLexer import JavaLexer
from gen.java.JavaParser import JavaParser


def main(args):
    stream = FileStream(args.file, encoding='utf8')
    lexer = JavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParser(token_stream)
    tree = parser.compilationUnit()
    my_listener = MergePackageRecognizerListener(
        common_token_stream=token_stream, p1 = 'p1'  , p2 = 'p2'
    )

    walker = ParseTreeWalker()
    walker.walk(t=tree, listener=my_listener)

    # with open('input.refactored.java', mode='w', newline='') as f:
    #     f.write(my_listener.token_stream_rewriter.getDefaultText())


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'./input2.java')
    args = argparser.parse_args()
    main(args)
