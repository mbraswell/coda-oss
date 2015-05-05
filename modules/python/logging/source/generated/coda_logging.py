# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.36
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _coda_logging
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


class Filterer(_object):
    """Proxy of C++ Filterer class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Filterer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Filterer, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """__init__(self) -> Filterer"""
        this = _coda_logging.new_Filterer(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _coda_logging.delete_Filterer
    __del__ = lambda self : None;
    def addFilter(*args):
        """addFilter(self, Filter filter)"""
        return _coda_logging.Filterer_addFilter(*args)

    def filter(*args):
        """filter(self, LogRecord record) -> bool"""
        return _coda_logging.Filterer_filter(*args)

    def removeFilter(*args):
        """removeFilter(self, Filter filter)"""
        return _coda_logging.Filterer_removeFilter(*args)

Filterer_swigregister = _coda_logging.Filterer_swigregister
Filterer_swigregister(Filterer)

class Handler(Filterer):
    """Proxy of C++ Handler class"""
    __swig_setmethods__ = {}
    for _s in [Filterer]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Handler, name, value)
    __swig_getmethods__ = {}
    for _s in [Filterer]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Handler, name)
    def __init__(self, *args, **kwargs): raise AttributeError, "No constructor defined"
    __repr__ = _swig_repr
    __swig_destroy__ = _coda_logging.delete_Handler
    __del__ = lambda self : None;
    def setFormatter(*args):
        """setFormatter(self, Formatter formatter)"""
        return _coda_logging.Handler_setFormatter(*args)

    def setLevel(*args):
        """setLevel(self, LogLevel level)"""
        return _coda_logging.Handler_setLevel(*args)

    def getLevel(*args):
        """getLevel(self) -> LogLevel"""
        return _coda_logging.Handler_getLevel(*args)

    def handle(*args):
        """handle(self, LogRecord record) -> bool"""
        return _coda_logging.Handler_handle(*args)

    def close(*args):
        """close(self)"""
        return _coda_logging.Handler_close(*args)

Handler_swigregister = _coda_logging.Handler_swigregister
Handler_swigregister(Handler)

class Filter(_object):
    """Proxy of C++ Filter class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Filter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Filter, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, std::string name="") -> Filter
        __init__(self) -> Filter
        """
        this = _coda_logging.new_Filter(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _coda_logging.delete_Filter
    __del__ = lambda self : None;
    def filter(*args):
        """filter(self, LogRecord record) -> bool"""
        return _coda_logging.Filter_filter(*args)

    def getName(*args):
        """getName(self) -> std::string"""
        return _coda_logging.Filter_getName(*args)

Filter_swigregister = _coda_logging.Filter_swigregister
Filter_swigregister(Filter)

class Logger(Filterer):
    """Proxy of C++ Logger class"""
    __swig_setmethods__ = {}
    for _s in [Filterer]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Logger, name, value)
    __swig_getmethods__ = {}
    for _s in [Filterer]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Logger, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, std::string name="") -> Logger
        __init__(self) -> Logger
        """
        this = _coda_logging.new_Logger(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _coda_logging.delete_Logger
    __del__ = lambda self : None;
    def log(*args):
        """
        log(self, LogLevel level, std::string msg)
        log(self, LogLevel level, except::Context ctxt)
        log(self, LogLevel level, except::Throwable t)
        """
        return _coda_logging.Logger_log(*args)

    def debug(*args):
        """
        debug(self, std::string msg)
        debug(self, except::Context ctxt)
        debug(self, except::Throwable t)
        """
        return _coda_logging.Logger_debug(*args)

    def info(*args):
        """
        info(self, std::string msg)
        info(self, except::Context ctxt)
        info(self, except::Throwable t)
        """
        return _coda_logging.Logger_info(*args)

    def warn(*args):
        """
        warn(self, std::string msg)
        warn(self, except::Context ctxt)
        warn(self, except::Throwable t)
        """
        return _coda_logging.Logger_warn(*args)

    def error(*args):
        """
        error(self, std::string msg)
        error(self, except::Context ctxt)
        error(self, except::Throwable t)
        """
        return _coda_logging.Logger_error(*args)

    def critical(*args):
        """
        critical(self, std::string msg)
        critical(self, except::Context ctxt)
        critical(self, except::Throwable t)
        """
        return _coda_logging.Logger_critical(*args)

    def addHandler(*args):
        """
        addHandler(self, Handler handler, bool own=False)
        addHandler(self, Handler handler)
        """
        return _coda_logging.Logger_addHandler(*args)

    def removeHandler(*args):
        """removeHandler(self, Handler handler)"""
        return _coda_logging.Logger_removeHandler(*args)

    def setLevel(*args):
        """setLevel(self, LogLevel level)"""
        return _coda_logging.Logger_setLevel(*args)

    def setName(*args):
        """setName(self, std::string name)"""
        return _coda_logging.Logger_setName(*args)

    def getName(*args):
        """getName(self) -> std::string"""
        return _coda_logging.Logger_getName(*args)

    def reset(*args):
        """reset(self)"""
        return _coda_logging.Logger_reset(*args)

Logger_swigregister = _coda_logging.Logger_swigregister
Logger_swigregister(Logger)

class NullHandler(Handler):
    """Proxy of C++ NullHandler class"""
    __swig_setmethods__ = {}
    for _s in [Handler]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NullHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [Handler]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, NullHandler, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, LogLevel level=LogLevel::LOG_NOTSET) -> NullHandler
        __init__(self) -> NullHandler
        """
        this = _coda_logging.new_NullHandler(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _coda_logging.delete_NullHandler
    __del__ = lambda self : None;
NullHandler_swigregister = _coda_logging.NullHandler_swigregister
NullHandler_swigregister(NullHandler)

class NullLogger(Logger):
    """Proxy of C++ NullLogger class"""
    __swig_setmethods__ = {}
    for _s in [Logger]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, NullLogger, name, value)
    __swig_getmethods__ = {}
    for _s in [Logger]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, NullLogger, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(self, std::string name="") -> NullLogger
        __init__(self) -> NullLogger
        """
        this = _coda_logging.new_NullLogger(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _coda_logging.delete_NullLogger
    __del__ = lambda self : None;
NullLogger_swigregister = _coda_logging.NullLogger_swigregister
NullLogger_swigregister(NullLogger)



