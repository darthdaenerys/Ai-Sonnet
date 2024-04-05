import sys
from process import *

initial_seed=sys.argv[1]
temperature=float(sys.argv[2])
steps=int(sys.argv[3])

generate_sequence(
    initial_seed=initial_seed,
    steps=steps,
    temperature=temperature
)