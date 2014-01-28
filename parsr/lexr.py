# -*- coding: utf-8 -*-

import ply.lex as lex

#   RESERVED:
#       LIST OF RESERVED TOKEN TYPES

class Lexer(object):
    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    #   TOKENS:
    #       LIST OF TOKEN TYPES

    tokens = [
        "NUMBER",
        "EQUALS",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "EXPONENT",
        "LPAREN",
        "RPAREN",
        "FUNCTION",
        "IDENTIFIER",     
    ]

    #   SIMPLE TOKEN SPECIFICATION:
    #       REGEX RULE ASSOCIATED WITH EACH SIMPLE TOKEN TYPE IN TOKENS
    #       PREFIXED BY t_

    t_EQUALS    = r"="
    t_PLUS      = r"\+"
    t_MINUS     = r"\-"
    t_TIMES     = r"\*"
    t_DIVIDE    = r"/"
    t_EXPONENT  = r"\^"
    t_LPAREN    = r"\("
    t_RPAREN    = r"\)"

    #   OTHER TOKEN SPECIFICATION:
    #       FUNCTION TO NEEDED FOR SPECIAL TOKEN TYPES
    #       PREFIXED BY t_
    #       ARGUMENT t IS INSTANCE OF LEX.LEXTOKEN()
    #           LEXTOKEN():
    #               TYPE = NAME FOLLOWING t_ PREFIX
    #               VALUE = VALUE
    #               LINENO = LINE NUMBER
    #               LEXPOS = POSITION RELATIVE TO BEGINNING OF INPUT STRING

    def t_NUMBER(self, t):
        r"[0-9]*\.?[0-9]+"
        t.value = float(t.value)    
        return t

    def t_COMMENT(self, t):
        r"\#.*"
        pass

    def t_FUNCTION(self, t):
        r"[a-zA-Z_][a-zA-Z_0-9]*(?=\()"
        t.value = t.value.lower()
        t.type = "FUNCTION"
        return t

    def t_IDENTIFIER(self, t):
        r"[a-zA-Z_][a-zA-Z_0-9]*"
        t.value = t.value.lower()
        t.type = "IDENTIFIER"
        return t

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    t_ignore  = " \t"

    def t_error(self, t):
        print "Illegal character '%s'" % t.value[0]
        t.lexer.skip(1)      