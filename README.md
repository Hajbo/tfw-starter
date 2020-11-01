# tfw-starter

## Supported modules example

The frontend will fetch the `supported_module.json` files for bot the language and the framework. Then it will remove duplicates and sort it. If a module is mandatory in one file, but optional in another, then it will be stored as mandatory.

```json
{
    "modules": {
        "mandatory": [
            {
                "name": "mandatory_module",
                "version": "1.0.0",
                "conflicts": "not_mandatory_module",
                "my_specific_key": "my_specific_value"
            },
            {
                "name": "mandatory_module_two",
                "version": "1.1.1"
            }
        ],
        "optional": [
            {
                "name": "not_mandatory_module",
                "version": "0.1.1"
            },
            {
                "name": "not_mandatory_module_two",
                "version": "5.1.1"
            }
        ]
    }
}
```