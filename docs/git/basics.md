# Basics

The everyday loop: look at what changed, stage it, commit it, review history.

### Show changed and untracked files

```bash
git status
```

### Stage all changes under the current directory

```bash
git add .
```

`git add .` stages the current directory and everything below it, not changes elsewhere in the repository. Use `git add -A` to stage the whole working tree.

### Stage a single file

```bash
git add <file>
```

### Commit the staged changes

```bash
git commit -m "<message>"
```

### Show recent history as a compact graph

```bash
git log --oneline --graph --decorate
```

Add `-n 20` to limit the output, or `--all` to include every branch.
