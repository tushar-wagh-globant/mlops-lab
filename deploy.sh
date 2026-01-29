#!/bin/bash
set -e

# --- CONFIGURATION ---
AWS_ACCOUNT_ID="887540997367"
REGION="us-east-1"
REPO_WRITER="simple-writer"
REPO_READER="simple-reader"

ECR_REGISTRY="$AWS_ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com"

echo "🚀 Starting Deployment for Account: $AWS_ACCOUNT_ID"

# 1. Create Repositories (Ignore error if they exist)
echo "--- Ensuring Repositories Exist ---"
aws ecr create-repository --repository-name $REPO_WRITER --region $REGION 2>/dev/null || true
aws ecr create-repository --repository-name $REPO_READER --region $REGION 2>/dev/null || true

# 2. Login to ECR
echo "--- Logging into AWS ECR ---"
aws ecr get-login-password --region $REGION \
  | docker login --username AWS --password-stdin $ECR_REGISTRY

# 3. Build, Tag, and Push WRITER
echo "--- Processing Writer ---"
docker build -t $REPO_WRITER ./writer
docker tag $REPO_WRITER:latest $ECR_REGISTRY/$REPO_WRITER:latest
docker push $ECR_REGISTRY/$REPO_WRITER:latest

# 4. Build, Tag, and Push READER
echo "--- Processing Reader ---"
docker build -t $REPO_READER ./reader
docker tag $REPO_READER:latest $ECR_REGISTRY/$REPO_READER:latest
docker push $ECR_REGISTRY/$REPO_READER:latest

echo "✅ DONE! Images are live in ECR."
