# tfw-starter

Features that could be added:
 * challenge creation on the platform

## Supported lanauages

Every supported language has to have a JSON file with the supported modules (TODO: categories and conflicts between modules). ??Framework specific packages??

## Backend

### API

 * GET /api/languages - sends back the list of supported languages
 * GET /api/languages/language_id - send back the language specific JSON
 * POST /create - post the config, generates and sends back the TFW starter

### Generating with tempaltes

Jinja2 templates should be used to generate the needed files.

A templated and cleaned-up copy of the test-tutorial-framework should be stored.

 * overwrite the webservice/ folder with the choosen language+framework starter app
 * generate the needed templates based on the config (Dockerfile, config.yml, etc.)
 * zip it
 * send back


## Frontend

The React frontend fetches the selected language from the backend and warns the user when conflicting packages are selected. The UX and UI has to be figured out soon.
Authorization trough Avatao is needed so we can verify the creators identity.

## Mandatory packages

Avatao SDK, language specific
