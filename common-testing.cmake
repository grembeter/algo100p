enable_testing()

file(GLOB tfiles "${CMAKE_SOURCE_DIR}/test/*.json")

foreach(filename ${tfiles})
    cmake_path(GET filename STEM basename)
    add_test(NAME "${filename}"
             COMMAND env "PYTHONDONTWRITEBYTECODE=1" pytest --verbose
             "--rootdir=${CMAKE_SOURCE_DIR}"
             -o "log_file=${basename}.log" -o "cache_dir=${CMAKE_CURRENT_BINARY_DIR}/pycache"
             --data "${filename}" --lib "$<TARGET_FILE:${CMAKE_PROJECT_NAME}-1>"
             "${CMAKE_SOURCE_DIR}/test/test_solution.py")
endforeach()
