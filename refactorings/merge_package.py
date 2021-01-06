import networkx as nx

from antlr4 import *
from antlr4.TokenStreamRewriter import TokenStreamRewriter

from gen.java9.Java9_v2Parser import Java9_v2Parser
from gen.java9 import Java9_v2Listener
from gen.javaLabeled.JavaParserLabeled import JavaParserLabeled

from gen.javaLabeled.JavaParserLabeledListener import JavaParserLabeledListener

import visualization.graph_visualization


class MergePackageRecognizerListener(JavaParserLabeledListener):
    """
    To implement the extract class refactoring
    Encapsulate field: Make a public field private and provide accessors
    a stream of tokens is sent to the listener, to build an object token_stream_rewriter
    field addresses the field of the class, tobe encapsulated.
    """
    def enterPackageDeclaration(self, ctx:JavaParserLabeled.PackageDeclarationContext):
        package_name = ctx.qualifiedName().IDENTIFIER().getText()
        if package_name == self.p1 or package_name == self.p2 :
            self.token_stream_rewriter.replaceRange(from_idx= ctx.qualifiedName().IDENTIFIER().getText().start.tokenIndex,
                                                    to_idx= ctx.qualifiedName().IDENTIFIER().getText().stop.tokenIndex,
                                                    text=self.p3)

    def enterImportDeclaration(self, ctx:JavaParserLabeled.ImportDeclarationContext):
        import_name = ctx.qualifiedName().IDENTIFIER().getText()
        if import_name == 'p1' or import_name == 'p2' :
            self.token_stream_rewriter.replaceRange(from_idx= ctx.qualifiedName().IDENTIFIER().getText().start.tokenIndex,
                                                    to_idx= ctx.qualifiedName().IDENTIFIER().getText().stop.tokenIndex,
                                                    text='p3')

    def __init__(self, common_token_stream: CommonTokenStream = None,
                 p1 : str = None,
                 p2 : str = None):
        """
        :param common_token_stream:
        """
        self.token_stream = common_token_stream
        self.p1 = p1
        self.p2 = p2
        # Move all the tokens in the source code in a buffer, token_stream_rewriter.
        if common_token_stream is not None:
            self.token_stream_rewriter = TokenStreamRewriter(common_token_stream)
        else:
            raise TypeError('common_token_stream is None')

