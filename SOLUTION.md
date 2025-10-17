# OpenTax Backend
## Architecture
A Layered Architecture approach was used to structure the project with each layer structured as follows:
### Models
  The business domains and entities which wereidentified e.g. Payments, Invoices, Agent Logs, AI Assistant Prompts and Summary

  Each model implements a Base class `OpenTaxEntity` which all models can implement.

  The idea of abstracting a base entity enables reusability of certain functionality and applies best practices such as DRY; for example a method to write to a database can take `OpenTaxEntity` as a parameter instead of creating a method for every domain.

  ### Infrastructure

  Includes of the data access layer which makes use of a repository pattern to interact with various data stores.

  Also serves as the layer to include any ports and adapters e.g. The `ai` directory includes a Port `llm.py` to which the adapters `mock_llm.py` or `gemini_llm.py` can implement. This implementation allows the AI Service layer to have hotswapable functionality via dependency injection. This also makes the system loosely coupled should you want to decouple the service layer later onwards e.g. microservice. See Alistair Cockburn's paper on this [architecture](https://alistair.cockburn.us/hexagonal-architecture)

### Application
Contains functionality related to services and core utilities of the application (logging,configurator, dependency container)


### Presentation
The layer that handle's end-user I/O. This would include API endpoints, webpages or a CLI. The FastAPI HTTP webserver sits on this layer

#### On Routing
- You will experience a Cross-origin resource sharing (CORS) error when fetching API data from your browser, including the OpenTax Frontend as it is listening on a different port. As a result FastAPI needs to have a middleware handler applying CORS, supported origins are passed in the application settings

## Design Patterns

### Repository Pattern

Purpose:

### Unit of Work

  Guarantees transactional boundaries (`commit`/`rollback`) and groups repository operations per request/use case.

  #### Notes and Trade-Offs
  The serialization between SQLModel and FastAPI objects under the hood strictly require a transaction to be committed otherwise the `rollback()` that is called on the UOWs exit will result a return of empty data.

#### Purpose

### Dependency Injection Containers
- `dependency_container.py`

#### Purpose
  - Centralized factory module `application/dependency_container.py` acts as a lightweight Service Locator.
  - Provides constructors for settings, logger, database engine, AI clients, and application services. This decouples route handlers from concrete implementations and eases testing.

- **Database and ORM**:

  - SQLModel + SQLAlchemy engine management in `infrastructure/database/session.py` with `create_sqlmodel_engine` and `session_factory` abstractions.
  - Metadata creation happens during engine provisioning in the DI container to ensure schema availability in local/dev contexts.

## Testing
- A few simple unit tests with pytest to showcase the use of testing. 


## DevOps
- Each project has a Dockerfile compiled
- Some processes to note when creating a Dockerfile: 
    - Always use specified version of an image, the `latest` tag may cause unexpected breaks if dependencies change.

## The Future
Much can be done to make this project far more production ready to name a few changes that I would make if I was allocated additional time:
- SSL certificate for HTTPS requests
- Session Authentication with [Redis](https://redis.io/blog/json-web-tokens-jwt-are-dangerous-for-user-sessions/)
- Create a message queue for Database Reads/Writes
- Abstract Service Layers to allow DI of Ports. You can then for example read and write invoices to a separate data store, make mocks of the service layer easier and so on

 # OpenTax Frontend
 A Next.js application application using Material UI components to quickly bootstrap a user interface.
 React Query was used to fetch data from the server side
 and Zastund for client side state management (store current page and filters, chatbot history in Browsers local storage)


 ## Trade Offs and Future
 Most of my design and attention went more into the backend so the front end could use some more attention namely:
 - Create a react component for tabular data rather violating DRY principle
 - Better validation of API schema validation
 - Next.js environment variables - The API URL should not be hard coded
 - More advanced use of React Query