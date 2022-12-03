import dis
import os

def exists(filename: str) -> bool:
     return os.path.exists(filename)

dis.dis(exists)