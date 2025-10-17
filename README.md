# adsum-technical-assessment

## Getting Started
- To run this project simply run the docker compose file 
    - `docker compose up -d`

- This should set you up with a basic instance. You will need further [configuration](#configuration) if you want to set up the ai chatbot feature

- The default ports are set to `localhost:3000` and `localhost:8000` for the Dashboard and APIs respectively
  
### Troubleshooting
- If the container throws a segmentation fault while `pip` is installing packages, simply retry running the docker compose file
- Likewise npm may through errors while installing dependencies, rerun the compose file
### Configuration
#### OpenTax Backend

The config file for the OpenTax Backend APIs are via `toml` files you may load it accordingly in the compose file via a volume binding
e.g. 
```
volumes:
- ./backend-config.toml:/app/config.toml
```
There are several customizable variables
```toml
[app]
title="OpenTax Backend API"
version="1.0"
debug="True"
prefix="/api"
max_limit="100"
sink="database"
origins=["http://localhost:3000"]
[database]
protocol="postgresql"     
database="postgres"     
host="localhost"         
port=5432          
user="postgres"
password="postgres"
[ai]
api_key=""          # A Google Studio AI Gemini API Key 
instructions=""     # Provide context to the LLM Client
```

## Development
- To run this projects locally refer to the README.md within the respective project
  - [Backend](backend/README.md)
  - [Frontend](frontend/README.md)