# AI-Powered Educational Image Captioning App for Kids

This project is an educational platform that uses AI to generate simple, kid-friendly captions for images, provides pronunciation audio, and gamified quizzes. It includes a parental dashboard and is fully containerized and deployable on AWS EKS.

## Main Features
- Upload or capture images
- AI-generated captions (BLIP model)
- Pronunciation audio (AWS Polly/gTTS)
- Gamified quiz based on captions
- Parental dashboard for progress tracking
- All data stored in AWS S3/DynamoDB
- CI/CD with GitHub Actions, Docker, Kubernetes (EKS)

## Folder Structure
- `frontend/` – React.js app
- `backend/` – FastAPI API
- `ml_service/` – BLIP model inference
- `infra/` – Docker, K8s, CI/CD, Terraform
- `storage/` – S3 & DynamoDB scripts
- `docs/` – Documentation

## Getting Started
See each folder for setup instructions.

---

## Architecture Diagram

![Architecture Diagram](docs/architecture.png)

---

## License
MIT License
