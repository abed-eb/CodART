"""

The main module of CodART

-changelog
-- Add C++ backend support

"""

__version__ = '0.2.0'
__author__ = 'Morteza'


import argparse
import sys
import glob, os

from antlr4 import *

# from refactorings.extract_class_migrated import ExtractClassRefactoringListener
from refactorings.merge_package import MergePackageRecognizerListener
from gen.java.JavaLexer import JavaLexer
from gen.java.JavaParser import JavaParser


def mergefolders(p1=None, p2=None):

    # Python program to
    # demonstrate merging
    # of two files

    data = data2 = None

    # Reading data from file1
    with open(p1) as fp:
        data = fp.read()
    with open(p2) as fp:
        data2 = fp.read()
    data += "\n"
    data += data2
    with open('p3.java', 'w') as fp:
        fp.write(data)


def main(args):

    i = 0
    while i < 4:
        if i == 0:
            stream = FileStream(args.file2, encoding='utf8')
            lexer = JavaLexer(stream)
            token_stream = CommonTokenStream(lexer)
            parser = JavaParser(token_stream)
            tree = parser.compilationUnit()
            my_listener = MergePackageRecognizerListener(
                common_token_stream=token_stream, p1='p1', p2='p2'
            )

            walker = ParseTreeWalker()
            walker.walk(t=tree, listener=my_listener)

            with open('input.refactored.java', mode='w', newline='') as f:
                f.write(my_listener.token_stream_rewriter.getDefaultText())
            i = i+1
        elif i == 1:
            stream = FileStream(args.file, encoding='utf8')
            lexer = JavaLexer(stream)
            token_stream = CommonTokenStream(lexer)
            parser = JavaParser(token_stream)
            tree = parser.compilationUnit()
            my_listener = MergePackageRecognizerListener(
                common_token_stream=token_stream, p1='p1', p2='p2'
            )

            walker = ParseTreeWalker()
            walker.walk(t=tree, listener=my_listener)

            with open('input.refactored2.java', mode='w', newline='') as f:
                f.write(my_listener.token_stream_rewriter.getDefaultText())
            i = i+1

        elif i == 2:
            mergefolders("input.refactored.java", "input.refactored2.java")
            i = i+1

        else :
            lines_seen = set()  # holds lines already seen
            with open("p4.java", "w") as output_file:
                for each_line in open("p3.java", "r"):
                    if each_line not in lines_seen or "class" in each_line or "{" in each_line or "}" in each_line:  # check if line is not duplicate
                        output_file.write(each_line)
                        lines_seen.add(each_line)
            i = i+1

if __name__ == '__main__':

    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        '-n', '--file',
        help='Input source', default=r'input.java')
    argparser.add_argument(
        '-n2', '--file2',
        help='Input source', default=r'input2.java')
    args = argparser.parse_args()
    main(args)

