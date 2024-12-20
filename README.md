# Build
```bash
$ mkdir build
$ cd build
$ cmake ..
$ make
```

[slides](https://dboyliao.github.io/play_torch.fx/#/)

# References
- https://peps.python.org/pep-0523/
    - https://github.com/python/cpython/issues/80067
- https://github.com/pytorch/examples/tree/cdef4d43fb1a2c6c4349daa5080e4e8731c34569/fx
- https://pytorch.org/docs/stable/torch.compiler_dynamo_overview.html
- https://www.youtube.com/watch?v=5FNHwPIyHr8
- https://www.youtube.com/watch?v=TexdGMdQya4
- https://www.youtube.com/watch?v=egZB5Uxki0I
- https://fkong.tech/posts/2023-05-20-dynamo/
- https://dev-discuss.pytorch.org/t/torchinductor-a-pytorch-native-compiler-with-define-by-run-ir-and-symbolic-shapes/747
- https://pytorch.org/TensorRT/contributors/writing_dynamo_aten_lowering_passes.html
- https://jysh1214.github.io/pytorch/2024/10/08/A-Walkthrough-Example-of-torch.compile-with-IREE-Turbine.html
- https://jysh1214.github.io/pytorch/2024/10/19/Graph-Break-in-TorchDynamo.html
- PyTorch Custom Backends: https://pytorch.org/docs/stable/torch.compiler_custom_backends.html#overview
- What is Continuation: https://www.youtube.com/watch?v=zB5LTkaJaqk&ab_channel=EricNormand
- `set_eval_frame` in TorchDynamo: https://dev-discuss.pytorch.org/t/a-minimal-working-example-of-standalone-usage-for-dynamo-eval-frame/1525
- https://fkong.tech/posts/2023-05-14-dynamo-01/
    -  `InstructionTranslator`: https://fkong.tech/posts/2023-05-14-dynamo-02/
