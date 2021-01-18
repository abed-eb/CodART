import networkx as nx

from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from gen.java9.Java9_v2Parser import Java9_v2Parser
from gen.java9 import Java9_v2Listener
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled

from gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener
import os
import shutil

import visualization.graph_visualization


class MergePackageRecognizerListener(JavaParserLabeledListener):
    """
    To implement the extract class refactoring
    Encapsulate field: Make a public field private and provide accessors
    a stream of tokens is sent to the listener, to build an object token_stream_rewriter
    field addresses the field of the class, tobe encapsulated.
    """

    def mergefolders(self, p1 = "input.java", p2 = "input2.java"):
        # Python program to
        # demonstrate merging
        # of two files

        data = data2 = None

        # Reading data from file1
        with open(self.p1) as fp:
            data = fp.read()

            # Reading data from file2
        with open(self.p2) as fp:
            data2 = fp.read()

        # Merging 2 files
        # To add the data of file2
        # from next line
        data += "\n"
        data += data2

        with open('p3', 'w') as fp:
            fp.write(data)

    def enterPackageDeclaration(self, ctx: JavaParserLabeled.PackageDeclarationContext):
        package_name = ctx.getText().split("package")[1].replace(';', '')
        # self.mergefolders(self.p1, self.p2)
        if package_name == self.p1 or package_name == self.p2:
            self.token_stream_rewriter.replaceRange(from_idx=ctx.start.tokenIndex,
                                                    to_idx=ctx.stop.tokenIndex,
                                                    text='package p3;')
            # x = self.token_stream_rewriter.getText(start= ctx.start.tokenIndex,
            #                                         stop= ctx.stop.tokenIndex,
            #                                         program_name=self.token_stream_rewriter.DEFAULT_PROGRAM_NAME)
            print(package_name)

    def enterImportDeclaration(self, ctx: JavaParserLabeled.ImportDeclarationContext):
        import_name = ctx.getText().split("import")[1].replace(';', '')
        if import_name == 'p1' or import_name == 'p2':
            self.token_stream_rewriter.replaceRange(from_idx=ctx.start.tokenIndex,
                                                    to_idx=ctx.stop.tokenIndex,
                                                    text='p3')
            print(import_name)


    def __init__(self, common_token_stream: CommonTokenStream = None,
                 p1 : str = None,
                 p2 : str = None,):
        """
        :param common_token_stream:
        """
        self.token_stream = common_token_stream
        self.p1 = p1
        self.p2 = p2
        self.p3 = None
        # Move all the tokens in the source code in a buffer, token_stream_rewriter.
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

