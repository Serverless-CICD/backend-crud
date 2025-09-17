# Backend CRUD - SAM Test Application

This is a simple serverless CRUD API built with AWS SAM to **test SAM infrastructure deployment** through CI/CD pipelines.

## Purpose

This project serves as a **test application** to validate that SAM infrastructure can be properly:
- Built and packaged by CodeBuild
- Deployed via CloudFormation
- Integrated with CI/CD pipelines

## Architecture

- **API Gateway**: REST API endpoints
- **Lambda Functions**: Python runtime for CRUD operations
- **DynamoDB**: NoSQL database for data storage
- **SAM Template**: Infrastructure as Code

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/items` | Create new item |
| GET | `/items/{id}` | Get item by ID |
| PUT | `/items/{id}` | Update item |
| DELETE | `/items/{id}` | Delete item |

## Local Development

```bash
# Build SAM application
sam build

# Deploy locally
sam local start-api

# Test locally
curl http://localhost:3000/items
```

## CI/CD Integration

This repository is designed to work with automated CI/CD pipelines that:

1. **Source**: Pull code from this repository
2. **Build**: Run `sam build` and `sam package`
3. **Deploy**: Deploy via CloudFormation

## Testing the Deployment

After deployment through CI/CD:

```bash
# Get API URL from CloudFormation outputs
aws cloudformation describe-stacks \
  --stack-name your-stack-name \
  --query 'Stacks[0].Outputs[?OutputKey==`ApiUrl`].OutputValue' \
  --output text

# Test CRUD operations
API_URL="your-api-url"

# Create item
curl -X POST $API_URL/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Item", "description": "Testing SAM deployment"}'

# Read item
curl -X GET $API_URL/items/{id}

# Update item  
curl -X PUT $API_URL/items/{id} \
  -H "Content-Type: application/json" \
  -d '{"name": "Updated", "description": "Updated via API"}'

# Delete item
curl -X DELETE $API_URL/items/{id}
```

## Files Structure

```
backend-crud/
├── template.yaml          # SAM template
├── src/
│   └── app.py            # Lambda function code
└── README.md             # This file
```

## Note

This is a **test application** for validating SAM infrastructure deployment. The CRUD functionality is simple and intended for testing purposes only.
