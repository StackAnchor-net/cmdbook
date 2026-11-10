# Core workflow

The everyday loop for Terraform: initialise, preview, apply. The same commands work with OpenTofu as `tofu`.

## Initialise

### Initialise the working directory

```bash
terraform init
```

Downloads providers and modules and configures the backend.

### Upgrade providers to the newest allowed versions

```bash
terraform init -upgrade
```

Ignores the versions pinned in the lock file and re-selects the newest ones that satisfy your constraints.

## Plan and apply

### Preview the changes

```bash
terraform plan
```

### Save a plan to a file

```bash
terraform plan -out=<plan-file>
```

### Apply a saved plan

```bash
terraform apply <plan-file>
```

Applies exactly what was reviewed, with no confirmation prompt.

### Apply a single resource only

```bash
terraform apply -target=<address>
```

Meant for exceptional cases such as recovering from an error; routine use leaves the rest of the configuration out of sync.

## Tear down

### ⚠ Destroy all managed infrastructure

```bash
terraform destroy
```

!!! warning
    Every resource tracked in the current state is deleted from the provider, along with any data stored in them. `terraform apply -destroy` does the same thing.

See also the official [Terraform CLI documentation](https://developer.hashicorp.com/terraform/cli/commands).
