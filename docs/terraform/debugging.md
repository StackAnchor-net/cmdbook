# Debugging & formatting

Format and check code, inspect plans, detect drift and unstick a locked state. The same commands work with OpenTofu as `tofu`.

## Format and check

### Format all files recursively

```bash
terraform fmt -recursive
```

### Check the configuration for errors

```bash
terraform validate
```

## Inspect

### Open an interactive console

```bash
terraform console
```

Evaluate expressions against the current state and configuration.

### Print the dependency graph

```bash
terraform graph
```

Outputs DOT format, which Graphviz can render.

### Show a saved plan

```bash
terraform show <plan-file>
```

### Plan with verbose debug logging

```bash
TF_LOG=DEBUG terraform plan
```

## Variables and drift

### Plan with a variables file

```bash
terraform plan -var-file=<file.tfvars>
```

Use `-var 'name=value'` to set a single variable instead.

### Detect drift without changing infrastructure

```bash
terraform plan -refresh-only
```

### Accept drift into the state

```bash
terraform apply -refresh-only
```

## Locks

### ⚠ Release a stuck state lock

```bash
terraform force-unlock <lock-id>
```

!!! warning
    Unlocking while another run is still active can let two runs write the state at once and corrupt it. Confirm that no process holds the lock first.

See also the official [Terraform CLI documentation](https://developer.hashicorp.com/terraform/cli/commands).
