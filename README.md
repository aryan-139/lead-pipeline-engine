# 📦 Lead Pipeline Engine
A FastAPI-based backend integrated with a Chrome extension to streamline the process of collecting, curating, and triggering outreach to leads — primarily from LinkedIn. This project helps automate lead ingestion, formatting, and email generation based on predefined strategies and intent types (like referrals or job opening enquiries).

## 🚀 Features
✅ Chrome extension to capture selected text (names) on LinkedIn.

✅ In-memory stack to manage and view leads before final submission.

✅ UI with options for intent, company name, job description, custom email domain, and email format.

✅ Multiple email generation strategies (first_last, first.initial.last, etc.).

✅ FastAPI backend for handling the stack, trigger logic, and email generation.

✅ Writes all generated emails into a .txt file in the user's Downloads folder.

✅ Option to delete/edit stack items from the extension popup before sending.

## Architecture 
<img width="995" height="534" alt="image" src="https://github.com/user-attachments/assets/64facd3e-3ded-4f92-8575-783ef00f2b5e" />


## Installation 
```java 
pip install fastapi uvicorn pydantic
```
## Run the server 
```
python run.py
```
## Link to Chrome Extension 
https://github.com/aryan-139/leadscale

### Pending Implementations 
- Implement the retry worker 
- Implement any other Ingestion Module 
- Give cover letter as per the job description
- Name Validator module 
- Company Email Validator module based on current company 
- Persist memory in DB
- Integrate RabbitMQ for async message queue.

