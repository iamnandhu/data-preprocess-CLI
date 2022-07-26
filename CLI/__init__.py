""" High level package for Reflect - Data preprocessor CLI """
#CLI/__init__.py

__app_name__ = "Reflect"
__version__ = "0.1.0"


(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
)=range(3)

ERRORS = {
    DIR_ERROR     : "directory not found error",
    FILE_ERROR    : "innvalid file format error",
}