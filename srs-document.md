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
#### POST `api/generate/projects`
#### POST `api/generate/summary`
#### POST `api/generate/ats-check`
