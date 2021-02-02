"""

The main module of CodART

-changelog
-- Add C++ backend support

"""

__version__ = '0.2.0'
__author__ = 'Morteza'


import argparse
import sys
import shutil
import glob, os

from antlr4 import *

# from refactorings.extract_class_migrated import ExtractClassRefactoringListener
from refactorings.merge_package import MergePackageRecognizerListener
from gen.java.JavaLexer import JavaLexer
from gen.java.JavaParser import JavaParser


def mergefolders(source_dir=None, target_dir=None):

    file_names = os.listdir(source_dir)
    for file_name in file_names:
        shutil.move(os.path.join(source_dir, file_name), target_dir)
    os.chdir(r"D:\frontEnd\CodART")
    os.rename("pk2", "pk2")
    # Python program to
    # demonstrate merging
    # of two files

    # data = data2 = None
    #
    # # Reading data from file1
    # with open(p1) as fp:
    #     data = fp.read()
    # with open(p2) as fp:
    #     data2 = fp.read()
    # data += "\n"
    # data += data2
    # with open('p3.java', 'w') as fp:
    #     fp.write(data)


def main(args, bool):
    stream = FileStream(args.file, encoding='utf8')
    lexer = JavaLexer(stream)
    token_stream = CommonTokenStream(lexer)
    parser = JavaParser(token_stream)
    tree = parser.compilationUnit()
    my_listener = MergePackageRecognizerListener(
        common_token_stream=token_stream, pk1='pk1', pk2='pk2'
    )

    walker = ParseTreeWalker()
    walker.walk(t=tree, listener=my_listener)

    with open("pk1/input.java", mode='w', newline='') as f:
        f.write(my_listener.token_stream_rewriter.getDefaultText())

    if bool == 0:
        print("entered")
        stream = FileStream(args.file2, encoding='utf8')
        lexer = JavaLexer(stream)
        token_stream = CommonTokenStream(lexer)
        parser = JavaParser(token_stream)
        tree = parser.compilationUnit()
        my_listener = MergePackageRecognizerListener(
            common_token_stream=token_stream, pk1='pk1', pk2='pk2'
        )

        walker = ParseTreeWalker()
        walker.walk(t=tree, listener=my_listener)

        with open("pk2/input2.java", mode='w', newline='') as f:
            f.write(my_listener.token_stream_rewriter.getDefaultText())

    if bool == 2:
        print("entered2")
        stream = FileStream(args.file3, encoding='utf8')
        lexer = JavaLexer(stream)
        token_stream = CommonTokenStream(lexer)
        parser = JavaParser(token_stream)
        tree = parser.compilationUnit()
        my_listener = MergePackageRecognizerListener(
            common_token_stream=token_stream, pk1='pk1', pk2='pk2'
        )

        walker = ParseTreeWalker()
        walker.walk(t=tree, listener=my_listener)

        with open("pk4/input4.java", mode='w', newline='') as f:
            f.write(my_listener.token_stream_rewriter.getDefaultText())
        mergefolders("pk1", "pk2")
        # else:
        #     lines_seen = set()  # holds lines already seen
        #     with open("p4.java", "w") as output_file:
        #         for each_line in open("p3.java", "r"):
        #             if each_line not in lines_seen or "class" in each_line or "{" in each_line or "}" in each_line:  # check if line is not duplicate
        #                 output_file.write(each_line)
        #                 lines_seen.add(each_line)
        #     i = i+1

if __name__ == '__main__':
    package1 = input("Please enter address of package 1: ")
    package2 = input("Please enter address of package 2: ")
    srcAddress = input("Please enter address of package 2: ")
    file_names = os.listdir(package1)
    file_names2 = os.listdir(package2)
    file_names3 = os.listdir("pk4")
    i=0
    j=0
    k=0
    argparser = argparse.ArgumentParser()
    while i < len(file_names):
        argparser.add_argument(
            '-n', '--file',
            help='Input source', default=r'' + package1 + '/' + file_names[i])
        args = argparser.parse_args()
        i = i+1
        main(args, 1)
    while j < len(file_names2):
        argparser.add_argument(
            '-n2', '--file2',
            help='Input source', default=r'' + package2 + '/' + file_names2[j])
        args = argparser.parse_args()
        j = j+1
        main(args, 0)
    while k < len(file_names3):
        print("why?")
        argparser.add_argument(
            '-n3', '--file3',
            help='Input source', default=r'pk4/' + file_names3[k])
        args = argparser.parse_args()
        k = k+1
        main(args, 2)

