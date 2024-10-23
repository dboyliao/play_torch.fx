from typing import Type

import torch
import torch.fx


def simple_mul(a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    return torch.add(a, b) * b


simple_mul_fx = torch.fx.symbolic_trace(simple_mul)
print(simple_mul_fx.graph)
print(simple_mul_fx.code)


class MyModule(torch.nn.Module):
    def forward(self, a: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
        return simple_mul(a, b)


def transform(
    m: torch.nn.Module, tracer_class: Type[torch.fx.Tracer] = torch.fx.Tracer
) -> torch.fx.Graph:
    graph = tracer_class().trace(m)
    for node in graph.nodes:
        if node.op == "call_function":
            if node.target == torch.add:
                node.target = torch.mul
    graph.lint()
    return torch.fx.GraphModule(m, graph)


mm = MyModule()
print(torch.fx.symbolic_trace(transform(mm)).code)
