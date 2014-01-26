import ply.lex as lex

class Lexer(object):
    def __init__(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    #   TOKENS:
    #       LIST OF POSSIBLE TOKEN TYPES

    tokens = (
        "NUMBER",
        "PLUS",
        "MINUS",
        "TIMES",
        "DIVIDE",
        "LPAREN",
        "RPAREN",
    )

    #   SIMPLE TOKEN SPECIFICATION:
    #       REGEX RULE ASSOCIATED WITH EACH SIMPLE TOKEN TYPE IN TOKENS
    #       PREFIXED BY t_

    t_PLUS    = r"\+"
    t_MINUS   = r"\-"
    t_TIMES   = r"\*"
    t_DIVIDE  = r"/"
    t_LPAREN  = r"\("
    t_RPAREN  = r"\)"

    #   OTHER TOKEN SPECIFICATION:
    #       FUNCTION TO NEEDED FOR SPECIAL TOKEN TYPES
    #       PREFIXED BY t_
    #       ARGUMENT t IS INSTANCE OF LEX.LEXTOKEN()
    #           LEXTOKEN():
    #               TYPE = NAME FOLLOWING t_ PREFIX
    #               VALUE
    #               LINENO = LINE NUMBER
    #               LEXPOS = POSITION RELATIVE TO BEGINNING OF INPUT STRING

    def t_NUMBER(self, t):
        r"[-+]?[0-9]*\.?[0-9]+"
        t.value = float(t.value)    
        return t

    def t_COMMENT(self, t):
        r"\#.*"
        pass

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(t.value)

    t_ignore  = " \t"

    def t_error(self, t):
        print "Illegal character '%s' % t.value[0]"
        t.lexer.skip(1)      