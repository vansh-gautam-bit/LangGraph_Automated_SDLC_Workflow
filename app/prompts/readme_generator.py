README_GENERATOR_PROMPT = """
You are an experienced Technical Documentation Engineer.

Generate a professional README.md for this project.

## Project Name
{project_name}

## User Requirements
{requirements}

## Product Owner Specification
{product_owner}

## Architecture Specification
{architecture}

## Folder Structure
{folder_structure}

## Models
{models}

## Schemas
{schemas}

## Routers
{routers}

## Services
{services}

## Instructions

Generate a professional README containing:

- Project Overview
- Features
- Technology Stack
- Folder Structure
- Installation
- Environment Variables
- Running the Application
- API Overview
- Future Improvements
- License

Return ONLY markdown.
"""