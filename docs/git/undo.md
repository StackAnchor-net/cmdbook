# Stash & undo

Set work aside and take changes back. Several commands here are destructive; read the warnings.

### Stash changes, including untracked files

```bash
git stash -u
```

`-u` (`--include-untracked`) also stashes new files that Git does not track yet. Without it they stay in the working tree.

### Restore the latest stash and remove it from the stash list

```bash
git stash pop
```

`git stash apply` restores the stash too but keeps it in the list, which is handy when applying to several branches. List stashes with `git stash list`.

### Unstage a file but keep your edits

```bash
git restore --staged <file>
```

The newer equivalent of `git reset <file>`.

### ⚠ Remove a file from the repository and delete it from disk

```bash
git rm <file>
```

!!! warning
    The working copy of the file is deleted as well. It stays in history once committed, but is lost if it has uncommitted changes (Git refuses unless you add `-f`). Use `git rm --cached <file>` to stop tracking it but keep the file.

### ⚠ Discard all uncommitted changes to tracked files

```bash
git reset --hard
```

!!! warning
    Staged and unstaged modifications to tracked files are lost and cannot be recovered. Untracked files are left alone.

### ⚠ Delete untracked files and directories

```bash
git clean -fd
```

!!! warning
    Untracked files and directories are permanently deleted (they are not in any commit or the trash). Preview first with `git clean -nd`. Files ignored via `.gitignore` are kept.
