# Identity & config

Check which account and role you are acting as, inspect where the CLI gets its settings, and switch between named profiles. Run these first whenever a command behaves unexpectedly.

### Show the identity you are using

```bash
aws sts get-caller-identity
```

Prints the account ID, user or role ARN and user ID of the active credentials. It needs no special permissions.

### Show where the CLI reads its settings from

```bash
aws configure list
```

The output lists the profile, access key, secret key and region, and says whether each one came from an environment variable, a config file or the instance role.

### List configured profiles

```bash
aws configure list-profiles
```

### Read one setting from a profile

```bash
aws configure get region --profile <profile>
```

### Use a profile for the rest of the shell session

```bash
export AWS_PROFILE=<profile>
```

Add `--profile <profile>` to a single command instead to override this for one call.

### Sign in to an SSO profile

```bash
aws sso login --profile <profile>
```

Opens a browser to authenticate. The profile must already be set up with `aws configure sso`.

See also the official [AWS CLI v2 command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).
