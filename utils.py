from pathlib import Path

def get_input(fname):
    p = Path()/'input'/fname
    return p.read_text()