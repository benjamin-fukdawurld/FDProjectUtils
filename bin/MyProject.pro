#-------------------------------------------------
#
# Project created by FDProjectUtils on 11/09/2019, 01:44:22
#
#-------------------------------------------------

TARGET = MyProject
TEMPLATE = app
CONFIG += console c++17 


CONFIG -= app_bundle
CONFIG -= qt

DESTDIR = ../build/lib
MAKEFILE = ../build/makefiles/$${TARGET}
OBJECTS_DIR = ../build/.obj/$${TARGET}

LIBS += \
    -L../dir1 \
    -Lanother_dir \
    -L/dir/subdir \

LIBS += \
    -pthread \
    -lMylib \
    -lsomeotherlib \

DEPENDPATH += \
    include \
    any_directory \
    some/include/dir \

INCLUDEPATH += \
    include \
    any_directory \
    some/include/dir \

SOURCES += \

HEADERS += \

