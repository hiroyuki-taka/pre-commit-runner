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

    # 実行ファイル検索
    path_items = os.environ.get("PATH", "").split(os.path.pathsep)
    run_with_shell = True
    for path_item in path_items:
        print(f"check-path: {path_item}")
        poetry_execute_file = [file for file in pathlib.Path(path_item).iterdir() if file.is_file() and file.name.startswith("poetry")]
        pre_commit_execute_file = [file for file in pathlib.Path(path_item).iterdir() if file.is_file() and file.name.startswith("pre-commit")]

        if poetry_execute_file and pre_commit_execute_file:
            print(f"find: {poetry_execute_file[0].name}")
            print(f"find: {pre_commit_execute_file[0].name}")
            run_with_shell = False
            break

    if files:
        target_pwd = repository_root / sys.argv[1]
        proc = subprocess.run(
            ["poetry", "run", "pre-commit", "run", "--files", *[str(p) for p in files]],
            cwd=str(target_pwd),
            shell=run_with_shell
        )
        exit(proc.returncode)
    else:
        exit(0)


if __name__ == "__main__":
    main()
