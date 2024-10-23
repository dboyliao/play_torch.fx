from typing import List

import torch
from torch import _dynamo as torchdynamo


def my_compiler(gm: torch.fx.GraphModule, example_inputs: List[torch.Tensor]):
    print(f"inputs: {[id(in_) for in_ in example_inputs]}")
    print("my_compiler() called with FX graph:")
    gm.graph.print_tabular()
    return gm.forward  # return a python callable


@torchdynamo.optimize(my_compiler)
def toy_example(a, b):
    x = a / (torch.abs(a) + 1)
    if b.sum() < 0:
        b = b * -1
    return x * b


for _ in range(100):
    a = torch.randn(10)
    b = torch.randn(10)
    toy_example(a, b)

from torch._dynamo.eval_frame import _debug_get_cache_entry_list, innermost_fn

cache_entries = _debug_get_cache_entry_list(innermost_fn(toy_example))
cache_entry = cache_entries[0]
guard, code = cache_entry.check_fn, cache_entry.code
# the guard takes the local variables of an input frame, and tells whether a re-compilation should be triggered.
import dis

dis.dis(guard)
dis.dis(code)

for code_part in guard.code_parts:
    print(code_part)

from depyf import decompile

print(decompile(code))
