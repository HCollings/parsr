import parsr
while True:
    try:
        s = raw_input("calc > ")
    except EOFError:
        break
    if not s: continue
    result = parsr.get_parser().parse(s)
    print result
