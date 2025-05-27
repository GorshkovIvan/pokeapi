
# PokeAPI SDK

## Overview

This is a Python SDK for the PokeAPI.


## Supported Endpoints

### Pokemon
- `GET /pokemon/{id or name}` - Get a specific Pokemon
- `GET /pokemon` - List all Pokemon (paginated)

### Generation
- `GET /generation/{id or name}` - Get a specific generation
- `GET /generation` - List all generations (paginated)

All endpoints are relative to `https://pokeapi.co/api/v2`

The project can be run in two modes:

1. Development mode
2. Production mode



## Development mode

Git clone the repository.

From the root directory, run:

```bash
pip install -e .[dev]
```

Allows to run tests and linting with pytest and flake8.

To run tests:

```bash
pytest
```


## Production mode:

Git clone the repository.

From the root directory, run:

```bash
pip install .
```


## Usage

```python
from pokeapi import PokeAPI

api = PokeAPI()
```

### Pokemon Methods

```python
# Get Pokemon by name
pokemon = api.get_pokemon(name="pikachu")  # Returns Pokemon object

# Get Pokemon by ID
pokemon = api.get_pokemon(pokemon_id=1)    # Returns Pokemon object

# List Pokemon (paginated)
pokemon_list = api.list_pokemon(limit=10, offset=0)  # Returns list of resources
```

### Generation Methods

```python
# Get Generation by name
gen = api.get_generation(name="generation-i")  # Returns Generation object

# Get Generation by ID
gen = api.get_generation(generation_id=1)      # Returns Generation object

# List Generations (paginated)
gen_list = api.list_generations(limit=10, offset=0)  # Returns list of resources
```

### Parameters
- `name`: str - Resource name
- `pokemon_id/generation_id`: int - Resource ID
- `limit`: int - Number of results per page
- `offset`: int - Page offset

## Official Documentation

For more information on the PokeAPI, please refer to the [official documentation](https://pokeapi.co/docs/v2).


## Project Structure

```
src/
├── pokeapi/                    # Main package directory
│   ├── api_clients/           # API client implementations
│   │   ├── __init__.py
│   │   ├── pokemon_client.py  # Pokemon endpoint client
│   │   └── generation_client.py # Generation endpoint client
│   ├── connection/            # HTTP client implementations
│   │   ├── __init__.py
│   │   ├── base.py           # Base HTTP client class
│   │   └── get.py            # GET request implementation
│   ├── models/               # Data models
│   │   ├── __init__.py
│   │   ├── pokemon.py        # Pokemon data models
│   │   ├── generation.py     # Generation data models
│   │   ├── pagination.py     # Pagination response models
│   │   └── api_resource.py   # Common resource models
│   ├── sdk/                  # Main SDK interface
│   │   ├── __init__.py
│   │   └── pokeapi.py       # Main PokeAPI class
│   ├── __init__.py
│   ├── constants.py          # API constants and error messages
│   └── exceptions.py         # Custom exceptions
│
tests/                        # Test directory
├── integration/             # Integration tests
│   ├── test_pokeapi.py     # SDK interface tests
│   ├── test_pokemon_client.py    # Pokemon client tests
│   └── test_generation_client.py # Generation client tests
│
├── setup.py                # Package installation configuration
├── pyproject.toml         # Project build configuration
├── README.md              # Project documentation
└── LICENSE               # MIT License
```

### Directory Structure Explanation

- **src/pokeapi/**: Main package source code
  - **api_clients/**: Individual endpoint clients
  - **connection/**: HTTP client implementation
  - **models/**: Pydantic data models
  - **sdk/**: Main SDK interface

- **tests/**: Test suite
  - **integration/**: Integration tests with real API calls

### Key Design Decisions

- **PokeAPI**: Main class providing access to all functionality
- **PokemonClient**: Handles Pokemon endpoint requests
- **GenerationClient**: Handles Generation endpoint requests
- **HttpGetClient**: Implements HTTP GET requests
- **Models**: Pydantic models for type-safe responses


1. **Connection Layer Separation**
   - Base HTTP client (`base.py`) provides common functionality
   - GET client (`get.py`) implements specific HTTP method
   - This separation allows easy addition of new HTTP methods (POST, PUT, etc.)
   - Common error handling and request processing in base class
   - Allows for easy testing of the HTTP client

2. **API Client Separation**
   - Each API endpoint has its dedicated client class
   - `PokemonClient` and `GenerationClient` are independent
   - Ensures single responsibility principle
   - Makes maintenance and testing easier
   - Each client handles its own validation and error cases
   - Allows for easy testing of the API clients

3. **SDK Interface Design**
   - `pokeapi.py` serves as the main interface
   - Combines different API clients into a single entry point
   - Keeps implementation details hidden from end users
   - Provides a clean, intuitive API

4. **Extensibility Pattern**
   To add a new endpoint (e.g., "berries"):
   1. Create `BerryClient` in `api_clients/`
   2. Add berry models in `models/`
   3. Add client instance to `PokeAPI` class
   4. No changes needed in existing clients

5. **Data Validation**
   - Pydantic models are used for data validation
   - This ensures that the data returned from the API is valid and type-safe
   - It also allows for easy validation of the data in the tests

### Development Tools

1. **Testing - Pytest**
   - Framework for writing and running tests

2. **Linting - Flake8**
   - Code style enforcement

3. **Data Validation - Pydantic**
   - Type-safe data models

### Development Assistance

**Claude 3.5 Sonnet (AI)**
- Assisted with:
  - Code documentation and comments
  - Model structure suggestions
  - README documentation
  - Manual code completions in data models and tests

## Testing

The SDK is tested with integration tests that make real API calls:

### Test Coverage

1. **Generation Client Tests**
   - Fetching generation by ID and name
   - Pagination of generation lists
   - Error handling for invalid inputs
   - Type validation of returned objects
   - Response model validation

2. **Pokemon Client Tests**
   - Fetching Pokemon by ID and name
   - Pagination of Pokemon lists
   - Error handling for invalid inputs
   - Type validation of returned objects
   - Response model validation

3. **PokeAPI Interface Tests**
   - Integration of all client functionality
   - Proper delegation to specific clients
   - End-to-end request flow
   - Error propagation

## Limitations and Future Improvements

### Current Limitations

- Only GET requests supported
- Low test coverage
- No API versioning support
- No logging implementation
- No caching mechanism
- No user authentication
- No request retry mechanism

### Future Enhancements

- Add support for other HTTP methods
- Increase test coverage with unit tests
- Implement caching and logging
- Add API versioning support
- Add authentication and retry mechanisms