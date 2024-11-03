#include <stdio.h>

#include "Python.h"
#include "frameobject.h"
#if PY_VERSION_HEX >= 0x03080000
#define Py_BUILD_CORE
#define Py_CPYTHON_PYSTATE_H
#endif

#include "internal/pycore_interp.h"
#include "pystate.h"

#ifdef Py_BUILD_CORE
#undef Py_BUILD_CORE
#endif
#ifdef Py_CPYTHON_PYSTATE_H
#undef Py_CPYTHON_PYSTATE_H
#endif

static Py_tss_t _callback_key = Py_tss_NEEDS_INIT;

static PyObject *_custom_eval_frame(PyThreadState *tstate,
                                    struct _PyInterpreterFrame *frame,
                                    int throwflag) {
  PyObject *callback = PyThread_tss_get(&_callback_key);
  PyObject_CallObject(callback, NULL);
  Py_RETURN_NONE;
}

static PyObject *native_hello() {
  printf("Hello from CPython!\n");
  Py_RETURN_NONE;
}

static PyObject *set_eval_frame(PyObject *dummy, PyObject *args) {
  PyObject *callback = NULL;
  if (!PyArg_ParseTuple(args, "O:callback", &callback)) {
    return NULL;
  }
  if (!PyCallable_Check(callback)) {
    return NULL;
  }
  PyThread_tss_set(&_callback_key, callback);
  PyThreadState *tstate = PyThreadState_GET();
  tstate->interp->eval_frame = &_custom_eval_frame;
  Py_RETURN_NONE;
}

static PyMethodDef _methods[] = {
    {"set_eval_frame", (PyCFunction)set_eval_frame, METH_VARARGS, NULL},
    {"native_hello", (PyCFunction)native_hello, METH_NOARGS, NULL},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef _module = {
    PyModuleDef_HEAD_INIT, "custom_eval_frame",
    "experiment module for setting custom eval frame API", -1, _methods};

PyMODINIT_FUNC PyInit_custom_eval_frame(void) {
  return PyModule_Create(&_module);
}