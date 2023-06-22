# pre-commit-runner

```shell
root
├ .pre-commit-config.yaml
├─ sub-a
│ ├ pyproject.toml
│ └ .pre-commit-config.yaml
└─ sub-b
  ├ pyproject.toml
  └ .pre-commit-config.yaml
```

- root/pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/...
    hooks:
    - id: pre-commit-runner
      name: a
      args:
        - sub-a
      files: "sub-a/.*"
    - id: pre-commit-runner
      name: b
      args:
        - sub-b
      files: "sub-b/.*"
```
