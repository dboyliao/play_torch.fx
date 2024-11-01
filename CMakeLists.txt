cmake_minimum_required(VERSION 3.9)

project(custom_eval_frame)

# python3 configurations
execute_process(
    COMMAND python3-config --includes --embed
    OUTPUT_VARIABLE PYTHON_INCLUDES
    OUTPUT_STRIP_TRAILING_WHITESPACE)
execute_process(
    COMMAND python3-config --libs --embed
    OUTPUT_VARIABLE PYTHON_LIBS
    OUTPUT_STRIP_TRAILING_WHITESPACE)
execute_process(COMMAND python3-config --extension-suffix
    OUTPUT_VARIABLE PYTHON_LIB_SUFFIX
    OUTPUT_STRIP_TRAILING_WHITESPACE)
string(REPLACE "-lintl " "" PYTHON_LIBS ${PYTHON_LIBS})
separate_arguments(PYTHON_INCLUDES)
separate_arguments(PYTHON_LIBS)

message(STATUS "PYTHON_CFLAGS: ${PYTHON_INCLUDES}")
message(STATUS "PYTHON_LDFLAGS: ${PYTHON_LIBS}")

# Python3 interface
add_library(python3 INTERFACE)
target_compile_options(python3 INTERFACE ${PYTHON_INCLUDES})
target_link_options(python3 INTERFACE ${PYTHON_LIBS})

# custom_eval_frame
add_library(custom_eval_frame SHARED custom_eval_frame.c)
set_target_properties(
    custom_eval_frame PROPERTIES
    PREFIX ""
    SUFFIX ${PYTHON_LIB_SUFFIX}
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}
)
target_link_libraries(custom_eval_frame PRIVATE python3)
