# Setup

Identify yourself to Git and get a repository to work in. `git config --global` writes to your per-user config, so you only do it once per machine.

### Set the author name for your commits

```bash
git config --global user.name "<name>"
```

### Set the author email for your commits

```bash
git config --global user.email "<email>"
```

Use the same address as your hosting account so commits are linked to your profile.

### Create a new repository in the current directory

```bash
git init
```

### Clone a repository from a remote

```bash
git clone <repo-url>
```

Creates a directory named after the repository and sets up `origin` pointing at `<repo-url>`.
