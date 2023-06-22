import os
import pathlib
import subprocess
import sys


def main():
    repository_root = pathlib.Path(os.getcwd())
    project_root = pathlib.Path(sys.argv[1])
    # 相対パスの付け替え
    files = [
        x.relative_to(project_root)
        for path in sys.argv[2:]
        if (x := pathlib.Path(path)) and x.is_relative_to(project_root)
    ]

    if files:
        target_pwd = repository_root / sys.argv[1]
        proc = subprocess.run(
            ["poetry", "run", "pre-commit", "run", "--files", *[str(p) for p in files]],
            cwd=str(target_pwd),
        )
        exit(proc.returncode)
    else:
        exit(0)


if __name__ == "__main__":
    main()
