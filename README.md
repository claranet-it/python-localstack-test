# Python + Localstack + AWS SDK
This is a simple example of how to use the AWS SDK with Localstack.

## Pre-requisites
- Docker
- Python 3.12
- Terraform

## Services
- [x] S3
- [ ] S3 + Trigger
- [x] DynamoDB
- [x] Lambda
- [x] SQS
- [ ] SNS

## Python App
- Create a virtual environment
```bash
python3 -m venv .venv
```

- Install the requirements
```bash
pip install -r requirements.txt
```

- Run tester app
```bash
make tester
```

## Terraform
Copy the `terraform.tfvars.example` to `terraform.localstack.tfvars` and fill in the values.

Create infrastructure:
```bash
make tflocal-create
```