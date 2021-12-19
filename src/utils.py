from pathlib import Path

def get_input(fname):
    p = Path()/'data'/fname
    return p.read_text()