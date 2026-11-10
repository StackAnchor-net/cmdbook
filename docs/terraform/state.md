# State

Inspect and edit the state file that maps your configuration to real resources, and read the outputs. The same commands work with OpenTofu as `tofu`.

## Inspect

### List resources in the state

```bash
terraform state list
```

### Show one resource from the state

```bash
terraform state show <address>
```

### Show all output values

```bash
terraform output
```

### Print outputs as JSON

```bash
terraform output -json
```

## Change

### ⚠ Remove a resource from the state

```bash
terraform state rm <address>
```

!!! warning
    Terraform forgets the resource but does not delete it. The real object keeps running and is no longer managed, and the next apply may try to create a duplicate.

### Move or rename a resource in the state

```bash
terraform state mv <source-address> <destination-address>
```

### Import an existing resource

```bash
terraform import <address> <id>
```

The resource block for `address` must already exist in the configuration.

See also the official [Terraform CLI documentation](https://developer.hashicorp.com/terraform/cli/commands).
