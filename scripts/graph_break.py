import torch


@torch.compile
def fn(a):
    b = a + 2
    print("Hi")
    return b + a


fn(torch.randn(4))
