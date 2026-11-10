# Remotes

Connect a repository to a remote and exchange commits with it.

### List remotes with their URLs

```bash
git remote -v
```

To change the URL of an existing remote, use `git remote set-url origin <new-url>`.

### Add a remote named origin

```bash
git remote add origin <repo-url>
```

### Push a new branch and set its upstream

```bash
git push -u origin <branch>
```

`-u` is short for `--set-upstream`; afterwards a plain `git push` and `git pull` on this branch know where to go. To push a branch without setting the upstream, use `git push origin <branch>`.

### Fetch and merge changes from the upstream branch

```bash
git pull
```

To pull a specific branch, use `git pull origin <branch>`.

### ⚠ Force-push after rewriting history, but only if the remote is unchanged

```bash
git push --force-with-lease
```

!!! warning
    This overwrites the remote branch with your local history, so any commits on the remote that you do not have locally are lost. It is safer than `--force` because it refuses to push if someone else has pushed since your last fetch.
