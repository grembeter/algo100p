cmake_minimum_required(VERSION 3.16)

project(solution C)

include("../common-problem.cmake")

include_directories("include")

add_library(${CMAKE_PROJECT_NAME}-1 SHARED "solution-1.c")

include("../common-testing.cmake")
