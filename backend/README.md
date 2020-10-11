# The plan

Supported language examples are stored in the `languages/<language_name>/<framework_name>` folder. The folder has a `config.py` file that derives from the abstract class from the `config/base.py` file, this specifies the needed framework dependencies, optional framework specific dependencies and the needed operations in the `Dockerfile`. The dependencies are stored in the `dependencies.json` file. Every framework folder has an `app` folder that contains the actual application that gets copied into the `tfw_base/solvable/src/webservice` folder.


## Config

There are two types of config classes, `FrameworkConfig` and `LanguageConfig`. A config manager initalizes and uses them to generate the end result.

The config files:
 * parses the `dependency.json` files (language + framework) to generate the list of supported modules sent to the frontend
 * generates commands that are used during the templating (module installation, running the application)

## LanguageConfig

 * language specific installation steps
 * language specific supported modules (with conflicts)
 * language specific connector (used to be called SDK)

## FrameworkConfig

 * framework specific installation steps
 * framework specific commands to run
 * framework specific supported modules (with conflicts)

## Dependencies

### Supported dependencies
Language specific dependencies: `languages/<language_name>/dependencies.json`

Framework specific dependencies: `languages/<language_name>/<framework_name>/dependencies.json`

The JSON structure will contain the possible conflicts and dependency categories (database, networking, etc.)

### Unsupported dependencies

The user can specify modules using the frontend, but we don't guarantee that they actually work.

## Templating
Frontend sends config -> template using jinja2 -> overwrite the original file (only Dockerfile for now).
