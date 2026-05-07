# Example: Web CTF Workflow

## Challenge Type

JSON beautifier and preview file challenge.

## Known Information

The application accepts user input and creates a temporary preview file. The preview file can be accessed through a preview endpoint.

## Agent Workflow

1. Send normal JSON data and observe response.
2. Extract preview file name from API response.
3. Access preview endpoint.
4. Compare status codes for valid and invalid file names.
5. Test whether file parameter has filtering.
6. Summarize blocked paths and allowed paths.
7. Generate automation script for repeated testing.

## Useful Checks

- Whether the file name is predictable
- Whether path traversal is blocked
- Whether temporary files are stored in web-accessible directories
- Whether the preview endpoint reads arbitrary files
- Whether source code or backup files are exposed

## Result

This case is used as a training example for multi-step Web CTF analysis with AI assistance.
