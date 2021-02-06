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



    def enterPackageDeclaration(self, ctx: JavaParserLabeled.PackageDeclarationContext):
        package_name = ctx.getText().split("package")[1].replace(';', '')
        if package_name == self.pk1 or package_name == self.pk2:
            self.token_stream_rewriter.replaceRange(from_idx=ctx.start.tokenIndex,
                                                    to_idx=ctx.stop.tokenIndex,
                                                    text='package result;')
            print(package_name)

    def enterImportDeclaration(self, ctx: JavaParserLabeled.ImportDeclarationContext):
        import_name = ctx.getText().split("import")[1].replace(';', '')
        if import_name == self.pk1 + ".*" or import_name == self.pk2 + ".*":
            self.token_stream_rewriter.replaceRange(from_idx=ctx.start.tokenIndex,
                                                    to_idx=ctx.stop.tokenIndex,
                                                    text='import result.*;')
            print(import_name)


    def __init__(self, common_token_stream: CommonTokenStream = None,
                 pk1 : str = None,
                 pk2 : str = None,):
        """
        :param common_token_stream:
        """
        self.token_stream = common_token_stream
        self.pk1 = pk1
        self.pk2 = pk2
        self.pk3 = None
        # Move all the tokens in the source code in a buffer, token_stream_rewriter.
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

