import ply.yacc as yacc
import lexr
import math

functions = {
    "acos"      : math.acos,
    "acosh"     : math.acosh,
    "asin"      : math.asin,
    "asinh"     : math.asinh,
    "atan"      : math.atan,
    "atanh"     : math.atanh,
    "cos"       : math.cos,
    "cosh"      : math.cosh,
    "degrees"   : math.degrees,
    "exp"       : math.exp,
    "ln"        : math.log,    
    "log"       : math.log10,
    "radians"   : math.radians,           
    "sin"       : math.sin,
    "sinh"      : math.sinh,
    "sqrt"      : math.sqrt,    
    "tan"       : math.tan,
    "tanh"      : math.tanh,
}

identifiers = {
    "pi"        : math.pi,
    "e"         : math.e,
}

class Parser(object):        
    lexer = lexr.Lexer()
    tokens = lexer.tokens

    precedence = (
        ("left", "PLUS", "MINUS"),
        ("left", "TIMES", "DIVIDE"),
        ("right", "UMINUS"),
        ("right", "EXPONENT"),        
    )

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

    def p_expression_uminus(self, p):
        "expression : MINUS expression %prec UMINUS"
        p[0] = -p[2]

    def p_expression_exponent(self, p):
        "expression : expression EXPONENT expression"
        p[0] = math.pow(p[1], p[3])        

    def p_expression_function(self, p):
        "expression : FUNCTION LPAREN expression RPAREN"
        p[0] = functions[p[1]](p[3])

    def p_expression_assignment(self, p):
        "expression : IDENTIFIER EQUALS expression"
        identifiers.update({p[1]: p[3]})
        p[1] = p[3]

    def p_assignment(self, p):
        "expression : IDENTIFIER"
        p[0] = identifiers[p[1]]   

    def p_error(self, p):
        print "Syntax error in input!"

def get_parser():
    return yacc.yacc(module=Parser())
