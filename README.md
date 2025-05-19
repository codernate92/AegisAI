# AegisAI v2

**Next-gen threat intelligence platform** powered by LLMs, real-time feed ingestion, and a sleek modern UI.

## Features

- **Multi-Source IOC Ingestion**
  - Pulls indicators from AlienVault OTX, Shodan, Censys, and VirusTotal
- **LLM Summarization**
  - GPT-4o generated threat summaries for SOC analysts
- **FastAPI Backend**
  - SQLModel + REST API with Docker support
- **React Frontend**
  - Built with Next.js, Chakra UI, and SWR
  - Live IOC feed and AI-generated summaries
- **Dockerized for Deployment**
  - Full stack deployable with Docker Compose

## Getting Started

### Prerequisites

- Docker
- OpenAI API key (for GPT-4o summaries)
- API keys for:
  - AlienVault OTX
  - Shodan
  - Censys
  - VirusTotal

### Setup

1. Clone the repo and unzip the project:

```bash
git clone <your_repo_url>
cd AegisAI_v2
```

2. Set environment variables inside `docker-compose.yml`:

```yaml
  environment:
    - OPENAI_API_KEY=your-key
    - OTX_API_KEY=your-key
    - SHODAN_API_KEY=your-key
    - CENSYS_UID=your-id
    - CENSYS_SECRET=your-secret
    - VT_API_KEY=your-key
```

3. Launch the app:

```bash
docker compose up --build
```

- Backend runs at: [http://localhost:8000/docs](http://localhost:8000/docs)  
- Frontend runs at: [http://localhost:3000](http://localhost:3000)

## Roadmap

- MITRE ATT&CK TTP mapping
- SIEM / SOAR integrations (Splunk, TheHive, SecureX)
- Federated threat learning
- Dark-web OSINT ingestion
- Mobile push alerts + AR threat map

## License

MIT License  
© 2025 AegisAI Contributors
