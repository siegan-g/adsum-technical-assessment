# adsum-technical-assessment

## Getting Started
- To run this project simply run the docker compose file 
    - `docker compose up -d`

- This should set you up with a basic instance. You will need further [configuration](#configuration) if you want to set up the ai chatbot feature

- The default ports are set to localhost:3000 and localhost:8000 for the Dashboard and APIs respectively

### Configuration
#### OpenTax Backend

The config file for the OpenTax Backend APIs are via `toml` files you may load it accordingly in the compose file via a volume binding
e.g. 
```
volumes:
- backend-config.toml:/app/config.toml
```
There are several customizable variables
```toml
[database]
protocol=""     #string      The protocol used in a database connection string e.g. postgressql, mysql
database=""     #string      Name of the database
host=""         #string      Host/Domain or IP of Database
port=0          #int         Database port
user=""         #string      Username
password=""     #string      Password 

[ai]
api_key=""          #string         Gemini API Key 
instructions=""     #string     Provide context to the LLM Client
```

## Development
- To run this projects locally refer to the README.md within the respective project