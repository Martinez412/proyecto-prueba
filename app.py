import pandas as pd
from utils import is_prime

def f(event, contex):
    print("hola desde lambda con zappa")
    print(is_prime(5))
    return {}