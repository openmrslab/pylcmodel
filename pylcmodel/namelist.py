import parsley

grammar = r"""
namelist = '$' name:n pairlist:p ws '$END'? -> (n, dict(p))

pairlist = (pair:first (pair)*:rest -> [first] + rest) | -> []
pair = ws name:k ws '=' ws valuelist:v ws ','? -> (k.upper(), v)

name = <letter (letter | digit | '_')*>
valuelist = ws (stringlist | numberlist | truth | falsehood):v -> v

numberlist = (number:first (ws number)+:rest -> [first] + rest) | number
number = ('-' | -> ''):sign (intPart:ds (floatPart(sign ds) | -> int(sign + ds)))
intPart = (digit:first digits:rest -> first + rest) | digit
digit1_9 = :x ?(x in '123456789') -> x
digits = <digit*>
floatPart :sign :ds = <('.' digits exponent?) | exponent>:tail -> float(sign + ds + tail)
exponent = ('e' | 'E') ('+' | '-')? digits

stringlist = (string:first (ws string)+:rest -> [first] + rest) | string
string = '\'' (~'\'' anything)*:c '\'' -> ''.join(c)

truth = 'T' -> True
falsehood = 'F' -> False
"""

parser = parsley.makeGrammar(grammar, {})


def reads(text):
    return parser(text).namelist()
