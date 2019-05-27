# Lambda scheduling with DynamoDB

This project is a proof of concept for scheduling lambda functions through DynamoDB ttl events and streams.

Note that this method is not reliable to a certain second nor minute, but it should hit the targeted hour.

Create a table called `lambda-scheduling`, activate the time to live attribute `ttl` and create a stream that you hook up with the lambda function `executor` in the `serverless.yml` (replace the ARN). See the [guide](tbd.com) for more details.

Use [serverless](https://serverless.com/) to deploy the stack to AWS and then trigger the `scheduler` function to create an entry. Wait for a few minutes and then you should see an execution of the `executor` function. Note that "a few minutes" could be up to 10, even if the ttl was only set for a few seconds into the future.

## Reliability

This approach is not a good fit if you want to hit a certain minute or second (or start of an hour). It works if you're ok with "somewhen during an hour" or "somewhen during a day".

I ran a test by creating 1000 entries with a ttl of 10 to 300 seconds into the future. Below you can find the delay *after* the specified ttl.

| Group  | Time in ms |
| ------------- | ------------- |
| Maximum  | 791  |
| Minimum  | 485  |
| Average  | 636  |
| Median  | 633 |
| Percentile 0.99  | 784  |
| Percentile 0.95  | 772  |
| Percentile 0.90  | 757  |
| Percentile 0.50  | 633  |
