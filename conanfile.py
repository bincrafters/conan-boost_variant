from conans import ConanFile, tools


class BoostVariantConan(ConanFile):
    name = "Boost.Variant"
    version = "1.65.1"
    url = "https://github.com/bincrafters/conan-boost-variant"
    description = "Please visit http://www.boost.org/doc/libs/1_65_1/libs/libraries.htm"
    license = "www.boost.org/users/license.html"

    requires = \
        "Boost.Assert/1.65.1@bincrafters/testing", \
        "Boost.Bind/1.65.1@bincrafters/testing", \
        "Boost.Config/1.65.1@bincrafters/testing", \
        "Boost.Core/1.65.1@bincrafters/testing", \
        "Boost.Detail/1.65.1@bincrafters/testing", \
        "Boost.Functional/1.65.1@bincrafters/testing", \
        "Boost.Math/1.65.1@bincrafters/testing", \
        "Boost.Mpl/1.65.1@bincrafters/testing", \
        "Boost.Preprocessor/1.65.1@bincrafters/testing", \
        "Boost.Static_Assert/1.65.1@bincrafters/testing", \
        "Boost.Throw_Exception/1.65.1@bincrafters/testing", \
        "Boost.Type_Index/1.65.1@bincrafters/testing", \
        "Boost.Type_Traits/1.65.1@bincrafters/testing", \
        "Boost.Utility/1.65.1@bincrafters/testing"

    lib_short_names = ["variant"]
    is_header_only = True

    # BEGIN

    short_paths = True
    build_requires = "Boost.Generator/1.65.1@bincrafters/testing"

    def package_id(self):
        if self.is_header_only:
            self.info.header_only()

    @property
    def env(self):
        try:
            with tools.pythonpath(super(self.__class__, self)):
                import boostgenerator # pylint: disable=F0401
                boostgenerator.BoostConanFile(self)
        except:
            pass
        return super(self.__class__, self).env

    # END
