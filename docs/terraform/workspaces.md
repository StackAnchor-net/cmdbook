# Workspaces & modules

Keep several states for one configuration, and fetch modules and providers. The same commands work with OpenTofu as `tofu`.

## Workspaces

### List workspaces

```bash
terraform workspace list
```

### Create a workspace

```bash
terraform workspace new <workspace>
```

### Switch to a workspace

```bash
terraform workspace select <workspace>
```

## Modules and providers

### Download modules referenced by the configuration

```bash
terraform get
```

### Show the providers a configuration requires

```bash
terraform providers
```

See also the official [Terraform CLI documentation](https://developer.hashicorp.com/terraform/cli/commands).
