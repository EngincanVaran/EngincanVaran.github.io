#!/usr/bin/env python3
"""Build CV PDF from main.tex using tectonic."""

import shutil
import subprocess
import sys
from pathlib import Path

INSTALL_HINT = """
tectonic is not installed. To fix this:

  brew install tectonic
"""

OUTPUT_NAME = "engincan_varan_cv.pdf"
SOURCE = "main.tex"


def main() -> None:
    if not shutil.which("tectonic"):
        print(INSTALL_HINT)
        sys.exit(1)

    repo_root = Path(__file__).parent
    tex_file = repo_root / SOURCE
    if not tex_file.exists():
        print(f"Error: {SOURCE} not found in {repo_root}")
        sys.exit(1)

    print("Building CV...")
    result = subprocess.run(
        ["tectonic", str(tex_file)],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print("tectonic failed:")
        print(result.stderr)
        sys.exit(1)

    # tectonic outputs <stem>.pdf next to the .tex file
    built = repo_root / "main.pdf"
    built.replace(repo_root / OUTPUT_NAME)
    print(f"Done → {OUTPUT_NAME}")


if __name__ == "__main__":
    main()
