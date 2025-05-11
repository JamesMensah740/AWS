aws-learning-labs/
│
├── s3-lambda-dynamodb/
│   ├── lambda_function.py          # Lambda to process S3 file and write to DynamoDB
│   ├── event_trigger.json          # Example event that triggers the function
│   ├── sample_input_file.txt       # Example upload file for S3
│   └── README.md                   # Specific README for this folder
│
├── .gitignore
└── README.md                       # Main project overview


# AWS Learning Labs 🚀

This repository contains hands-on experiments and learning projects built using core AWS services such as S3, Lambda, and DynamoDB. It serves both as a personal reference and a portfolio of my cloud automation skills.

## 📚 Focus Areas
- Event-driven architecture (S3 triggers Lambda)
- Serverless functions
- DynamoDB integration
- Cloud best practices for beginners

## 🧰 Tools & Services
- AWS S3
- AWS Lambda (Python)
- AWS DynamoDB
- AWS CloudWatch (for logs)

## 📂 Structure
Each folder contains:
- Code samples
- Trigger/event examples
- Sample data
- Setup notes

---

## ⚙️ Running These Projects
All projects are intended to run within the **AWS Free Tier**. Please double-check your region and limits before deploying.

---

## 📈 Progress
This repo is updated regularly as I complete AWS Skill Builder labs, YouTube tutorials, or real-world demos.

# S3 + Lambda + DynamoDB Integration

This lab simulates a typical serverless data pipeline:
1. A file is uploaded to S3.
2. That triggers a Lambda function.
3. Lambda reads the file and writes parsed content to DynamoDB.

## 🛠️ Files
- `lambda_function.py`: Main function logic
- `event_trigger.json`: Simulated S3 event
- `sample_input_file.txt`: Dummy input file

## 🔧 To Do
- Add IAM role details
- Add deployment script (SAM or manual setup steps)
