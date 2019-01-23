#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.67.0@bincrafters/testing")

class BoostVariantConan(base.BoostBaseConan):
    name = "boost_variant"
    version = "1.67.0"
    url = "https://github.com/bincrafters/conan-boost_variant"
    lib_short_names = ["variant"]
    header_only_libs = ["variant"]
    b2_requires = [
        "boost_assert",
        "boost_bind",
        "boost_config",
        "boost_container_hash",
        "boost_core",
        "boost_detail",
        "boost_integer",
        "boost_move",
        "boost_mpl",
        "boost_preprocessor",
        "boost_static_assert",
        "boost_throw_exception",
        "boost_type_index",
        "boost_type_traits",
        "boost_utility"
    ]


