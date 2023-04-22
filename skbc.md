# Features over classic Scikit-build:

- Better warnings, errors, and logging
- Automatically adds Ninja and/or CMake only as required
- No dependency on setuptools, distutils, or wheel
- Powerful config system
- Automatic inclusion of site-packages in `CMAKE_PREFIX_PATH`
- FindPython backport CMake < 3.26.1
    - supports PyPY SOABI & Limited API / Stable ABI
- Limited API / Stable ABI and pythonless tags
- No slow generator search
- SDists are reproducible by default (UNIX, Python 3.9+)
- Support for caching between builds (opt-in `build-dir`)
- Support for writing out to extra wheel folders (scripts, headers, data)
- Dedicated entrypoints for module and prefix directories
- Several integrated dynamic metadata plugins
- Experimental editable mode support
    - Also optional experimental auto rebuilds on import.

Some known missing features that will be developed soon:

- No support for other targets besides install
- Wheels are not fully reproducible yet
- Several editable mode caveats (mentioned in the docs)
