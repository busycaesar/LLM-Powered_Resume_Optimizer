# SRS Document

## API List and Logic Overview

### Data Ingestion APIs

#### POST `api/data/job-description`

- **Purpose**: Stores the summarized version of the job description in the database.
- **Logic**:
  - Takes the document link from the request body.
  - Takes the job description from the document link.
  - Generates the summarized version of the job description, retaining the key skills, essentional keywords and important information about the company.
  - Stores the summarized version in the database and sends a positive response.

#### POST `api/data/master-data`

- **Purpose**: Stores the master data and its embeddings in the vector database.
- **Logic**:
  - Takes the document link from the request body.
  - Takes the master data from the document link.
  - Creates the embeddings of the master data.
  - Stores the embeddings and the master data in the vector database and sends a positive response.

#### POST `api/data/resume`

- **Purpose**: Stores the resume document's link in the database.
- **Logic**:
  - Takes the document link from the request body.
  - Stores the document link in the database and sends a positive response.

### Data Generation APIs

#### POST `api/generate/skills`

- **Purpose**: Suggests the technical skills for the resume.
- **Logic**:
  - Takes the stored job description.
  - Gets the content of the resume using the stored document link.
  - Adds the job description and resume content into the prompt template.
  - Sends the prompt template to the LLM to generate the response.
  - Returns a positive response along with the generated response.

#### POST `api/generate/projects`

- **Purpose**: Suggests projects for the resume along with the updated description.
- **Logic**:
  - Takes the stored job description.
  - Gets the relevant master data content chunk from the vector database.
  - Adds the job description and relevant content chunk into the prompt template.
  - Sends the prompt template to the LLM to generate the response.
  - Returns a positive response along with the generated response.

#### POST `api/generate/summary`

- **Purpose**: Suggests the professional summary for the resume.
- **Logic**:
  - Takes the stored job description.
  - Gets the content of the resume using the stored document link.
  - Adds the job description and resume content into the prompt template.
  - Sends the prompt template to the LLM to generate the response.
  - Returns a positive response along with the generated response.

#### POST `api/generate/ats-check`

- **Purpose**: Rates the resume's ATS score and suggests the updates for increasing the score.
- **Logic**:
  - Takes the stored job description.
  - Gets the content of the resume using the stored document link.
  - Adds the job description and resume content into the prompt template.
  - Sends the prompt template to the LLM to generate the response.
  - Returns a positive response along with the generated response.
