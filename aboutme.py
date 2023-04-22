from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.align import Align


WEB = """
### [iscinumpy.dev](https://iscinumpy.dev) &bullet; [scikit-hep.org/developer](https://scikit-hep.org/developer)
"""

PROJECTS = """
### My projects

pybind11 (python_example, cmake_example, scikit_build_example) &bullet;
cibuildwheel &bullet;
build &bullet;
scikit-build (core, cmake, ninja, moderncmakedomain) &bullet;
boost-histogram &bullet;
Hist &bullet;
UHI &bullet;
Scikit-HEP/cookie &bullet;
Vector &bullet;
CLI11 &bullet;
Plumbum &bullet;
GooFit &bullet;
Particle &bullet;
DecayLanguage &bullet;
Conda-Forge&nbsp;ROOT &bullet;
POVM &bullet;
Jekyll-Indico &bullet;
pytest&nbsp;GHA&nbsp;annotate-failures &bullet;
uproot-browser &bullet;
Scikit-HEP-repo-review &bullet;
meson-python &bullet;
flake8-errmsg &bullet;
beautifulhugo &bullet;
check-sdist
"""

console = Console()

console.print(
    Panel(
        Align("[bold]Henry Schreiner", align="center"),
        title="@henryiii",
        title_align="left",
        subtitle="[bold]RSE[/bold] @ [dark_orange3]Princeton University[/dark_orange3]",
        subtitle_align="right",
        padding=1,
    )
)
console.print()
console.print(Markdown(WEB))
console.print()
console.print(Markdown(PROJECTS))

console.print(
    Align(
        "[red][bold]@henryiii[/bold] (GitHub, Fosstodon) / [bold]@henryschreiner3[/bold] (Twitter)",
        align="right",
    )
)
