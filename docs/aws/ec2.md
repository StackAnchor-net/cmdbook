# EC2

Find, start, stop and connect to instances, and inspect their security groups. Most commands use `--query` (JMESPath) with `--output table` to keep results readable.

## Finding instances

### Find instances by Name tag

```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=<name>" --query "Reservations[].Instances[].[InstanceId,State.Name,PrivateIpAddress]" --output table
```

### List running instances

```bash
aws ec2 describe-instances --filters "Name=instance-state-name,Values=running" --query "Reservations[].Instances[].[InstanceId,InstanceType,PublicIpAddress]" --output table
```

Change the state value to `stopped` or `pending` to see instances in other states.

### Show the rules of a security group

```bash
aws ec2 describe-security-groups --group-ids <group-id>
```

## Power and access

### Start an instance

```bash
aws ec2 start-instances --instance-ids <instance-id>
```

### Stop an instance

```bash
aws ec2 stop-instances --instance-ids <instance-id>
```

### Open a shell on an instance with Session Manager

```bash
aws ssm start-session --target <instance-id>
```

Needs the Session Manager plugin installed locally, plus the SSM agent and an instance profile permitting Systems Manager on the instance. No inbound SSH port is required.

### ⚠ Terminate an instance

```bash
aws ec2 terminate-instances --instance-ids <instance-id>
```

!!! warning
    Termination is permanent. The instance is deleted, and its instance-store data and any EBS volumes set to delete on termination are lost. Stop the instance instead if you may need it again.

See also the official [AWS CLI v2 command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).
