#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(pycon, m) {
    py::print("Hello PyCon");
}
