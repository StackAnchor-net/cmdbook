# Branches

Create, switch, merge and rebase branches. `git switch` and `git switch -c` are the newer equivalents of `git checkout <branch>` and `git checkout -b <branch>`; both still work.

### List local branches

```bash
git branch
```

The current branch is marked with `*`. Use `git branch <branch>` to create a branch without switching to it.

### Switch to an existing branch

```bash
git switch <branch>
```

### Create a branch and switch to it

```bash
git switch -c <branch>
```

### Merge a branch into the current branch

```bash
git merge <branch>
```

Run it on the branch that should receive the changes.

### Replay the current branch on top of another branch

```bash
git rebase <base-branch>
```

This rewrites the current branch's commits. Do not rebase commits that others have already pulled.
