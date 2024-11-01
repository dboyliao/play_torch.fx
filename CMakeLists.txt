cmake_minimum_required(VERSION 3.9)

project(custom_eval_frame)

execute_process(COMMAND python3-config --cflags
    OUTPUT_VARIABLE PYTHON_CFLAGS
    OUTPUT_STRIP_TRAILING_WHITESPACE)
execute_process(COMMAND python3-config --ldflags --embed
    OUTPUT_VARIABLE PYTHON_LDFLAGS
    OUTPUT_STRIP_TRAILING_WHITESPACE)
string(REPLACE "-lintl " "" PYTHON_LDFLAGS ${PYTHON_LDFLAGS})
separate_arguments(PYTHON_CFLAGS)
separate_arguments(PYTHON_LDFLAGS)

message(STATUS "PYTHON_CFLAGS: ${PYTHON_CFLAGS}")
message(STATUS "PYTHON_LDFLAGS: ${PYTHON_LDFLAGS}")

add_library(custom_eval_frame SHARED custom_eval_frame.c)
set_target_properties(custom_eval_frame PROPERTIES PREFIX "" SUFFIX ".so")
target_compile_options(custom_eval_frame PRIVATE ${PYTHON_CFLAGS})
target_link_options(custom_eval_frame PRIVATE ${PYTHON_LDFLAGS})
