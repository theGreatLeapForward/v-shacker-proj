cmake_minimum_required(VERSION 3.4)
project(v_shacker_proj LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)

add_subdirectory(extern/pybind11)

pybind11_add_module(v_shacker_proj main.cpp)

target_compile_definitions(v_shacker_proj PRIVATE VERSION_INFO=0)


