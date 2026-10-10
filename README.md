# VeriForm

Ensure legal consistency and completeness of high-stakes visa applications.

# Risk Analyzer MVP

A simple FastAPI service that checks if form fields appear in raw text.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run server: `uvicorn main:app --reload`
3. Test: `pytest -q`

## Architecture

![Architecture](docs/architecture.png)

<details>
<summary>Mermaid source</summary>

```mermaid
flowchart LR
    A[Client] --> B[FastAPI /analyze]
    B --> C{Iterate Fields}
    C --> D[Case-Insensitive Match]
    D --> E{Match Found?}
    E -->|Yes| F[Add to Matched]
    E -->|No| G[Skip]
    F --> H[Return Status]
```

</details>
