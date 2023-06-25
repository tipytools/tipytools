Tipytools

Tipytools is a Python library that provides a collection of command-line tool templates and utilities to streamline command-line tool development. It simplifies the process of generating a project structure for new tools and offers features such as logging, template-based file generation, and integration with the fire library for creating user-friendly command-line interfaces.

Features:

- Project setup made easy: Use the `setup` command to quickly set up your project with the necessary files and directory structure.
- Template-based project structure: Tipytools provides a standardized project structure including essential files like README.md, setup.py, and template files for your tool's implementation.
- Logging utility: The library includes a logging module that allows easy printing of information, warnings, errors, and success messages with customizable colors.
- Cross-platform compatibility: Tipytools is designed to work seamlessly on Windows, Linux, and macOS, ensuring compatibility across different platforms.
- Integration with fire library: Tipytools integrates with the fire library to provide a user-friendly and intuitive command-line interface for your generated tools.

Installation:
You can install Tipytools directly from the GitHub repository:

```shell
pip install git+https://github.com/tipytools/tipytools.git
```

Usage:

<!-- -. Install Tipytools using pip: `pip install tipytools` -->

-. Set up your project: `tipy setup tool=[toolname] [optional: env=[venvname]]`
-. Implement your tool's logic within the generated files and customize as needed.
-. Run your tool from the command line: `[toolname] [arguments]`

Please refer to the documentation available in the repository for more detailed information, usage examples, and customization options.

Contributions, bug reports, and feature requests are welcome! Feel free to submit issues and pull requests on GitHub to help improve Tipytools.
