# CloudWatch Logs

Find log groups, follow them live and search past events.

### List log groups

```bash
aws logs describe-log-groups --query "logGroups[].logGroupName" --output text
```

### Follow a log group live

```bash
aws logs tail <log-group> --follow --since 10m
```

`aws logs tail` is available in AWS CLI v2 only.

### Search a log group for a pattern

```bash
aws logs filter-log-events --log-group-name <log-group> --filter-pattern <pattern> --start-time <epoch-ms>
```

`--start-time` is in milliseconds since the Unix epoch. A pattern with spaces or quotes needs shell quoting, for example `'"connection refused"'`.

### Show the most recently active streams of a log group

```bash
aws logs describe-log-streams --log-group-name <log-group> --order-by LastEventTime --descending --max-items 5
```

See also the official [AWS CLI v2 command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html).
