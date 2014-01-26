import ply.yacc as yacc
import lexr

class Parser(object):        
    lexer = lexr.Lexer()
    tokens = lexer.tokens

    def p_expression_plus(self, p):
        "expression : expression PLUS term"
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        "expression : expression MINUS term"
        p[0] = p[1] - p[3]

    def p_expression_term(self, p):
        "expression : term"
        p[0] = p[1]

    def p_term_times(self, p):
        "term : term TIMES factor"
        p[0] = p[1] * p[3]

    def p_term_div(self, p):
        "term : term DIVIDE factor"
        p[0] = p[1] / p[3]

    def p_term_factor(self, p):
        "term : factor"
        p[0] = p[1]

    def p_factor_num(self, p):
        "factor : NUMBER"
        p[0] = p[1]

    def p_factor_expr(self, p):
        "factor : LPAREN expression RPAREN"
        p[0] = p[2]

    def p_error(self, p):
        print "Syntax error in input!"

def get_parser():
    return yacc.yacc(module=Parser())
