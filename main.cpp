#include <pybind11/pybind11.h>

//i just pasted the example thing to make sure this works
namespace py = pybind11;

int add(int i, int j) {
    return i + j;
}

PYBIND11_MODULE(VSHACKERS, m) {
    m.doc() = "pybind11 example plugin"; // optional module docstring

    m.def("add", &add, "A function that adds two numbers");
}
