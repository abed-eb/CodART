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
    os.renames("TestForCompiler/src/pk2", "TestForCompiler/src/pk2")
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


def main(args, bool, p1, p2):
    if bool == 1:
        print(args)
        print("welcome to the main")
        stream = FileStream(args.file, encoding='utf8')
        print("streamed")
        lexer = JavaLexer(stream)
        print("lexed")
        token_stream = CommonTokenStream(lexer)
        print("tokened")
        parser = JavaParser(token_stream)
        print("parsed")
        tree = parser.compilationUnit()
        print("running listener")
        my_listener = MergePackageRecognizerListener(
            common_token_stream=token_stream, pk1=p1, pk2=p2
        )

        walker = ParseTreeWalker()
        walker.walk(t=tree, listener=my_listener)

        with open('TestForCompiler/src/' + p1 + "/" + "input.java", mode='w', newline='') as f:
            f.write(my_listener.token_stream_rewriter.getDefaultText())
        # shutil.move(os.path.join('CodART', fileName), os.path.join(srcFolder + p1, fileName))
        # os.remove(srcFolder + fileName)

    if bool == 0:
        print("entered")
        stream = FileStream(args.file2, encoding='utf8')
        lexer = JavaLexer(stream)
        token_stream = CommonTokenStream(lexer)
        parser = JavaParser(token_stream)
        tree = parser.compilationUnit()
        my_listener = MergePackageRecognizerListener(
            common_token_stream=token_stream, pk1=p1, pk2=p2
        )

        walker = ParseTreeWalker()
        walker.walk(t=tree, listener=my_listener)

        with open('TestForCompiler/src/' + p2 + "/" + "input2.java", mode='w', newline='') as f:
            f.write(my_listener.token_stream_rewriter.getDefaultText())
        # shutil.move(os.path.join('CodART', fileName), os.path.join(srcFolder + p2, fileName))
        # os.remove(srcFolder + fileName)

    if bool == 2:
        print("entered2")
        stream = FileStream(args.file3, encoding='utf8')
        lexer = JavaLexer(stream)
        token_stream = CommonTokenStream(lexer)
        parser = JavaParser(token_stream)
        tree = parser.compilationUnit()
        my_listener = MergePackageRecognizerListener(
            common_token_stream=token_stream, pk1=p1, pk2=p2
        )

        walker = ParseTreeWalker()
        walker.walk(t=tree, listener=my_listener)
        with open('TestForCompiler/src/pk4/' + "input4.java", mode='w', newline='') as f:
            f.write(my_listener.token_stream_rewriter.getDefaultText())
        mergefolders('TestForCompiler/src/' + p1, 'TestForCompiler/src/' + p2)
        # else:
        #     lines_seen = set()  # holds lines already seen
        #     with open("p4.java", "w") as output_file:
        #         for each_line in open("p3.java", "r"):
        #             if each_line not in lines_seen or "class" in each_line or "{" in each_line or "}" in each_line:  # check if line is not duplicate
        #                 output_file.write(each_line)
        #                 lines_seen.add(each_line)
        #     i = i+1

if __name__ == '__main__':
    # srcDir = input("Please enter the address of project src folder :")
    package1 = input("Please enter the address of first package that you want to merge: ")
    package2 = input("Please enter the address of second package that you want to merge: ")
    # package 1 files
    file_names = os.listdir("TestForCompiler/src/" + package1)
    # package 2 files
    file_names2 = os.listdir("TestForCompiler/src/" + package2)
    # src files for fixing imports
    file_names3 = os.listdir("TestForCompiler/src")
    i = 0
    j = 0
    k = 0

    while i < len(file_names):
        argparser = argparse.ArgumentParser()
        argparser.add_argument(
            '-n', '--file',  help='Input source', default=r'TestForCompiler/src/' + package1 + "/" + file_names[i])
        args = argparser.parse_args()
        i = i+1
        main(args, bool=1, p1="pk1", p2="pk2")
    while j < len(file_names2):
        print("hi1")
        argparser = argparse.ArgumentParser()
        argparser.add_argument(
            '-n2', '--file2',  help='Input source', default=r'TestForCompiler/src/' + package2 + "/" + file_names2[j])
        args = argparser.parse_args()
        j = j+1
        main(args, bool=0, p1="pk1", p2="pk2")
    while k < len(file_names3):
        print("hi")
        fileNames = os.listdir("TestForCompiler/src/" + file_names3[k])

        for file in fileNames:
            argparser = argparse.ArgumentParser()
            argparser.add_argument(
                '-n3', '--file3',  help='Input source', default=r'TestForCompiler/src/' + file_names3[k] + "/" + file)
            args = argparser.parse_args()
            main(args, bool=2, p1="pk1", p2="pk2")
        k = k+1

