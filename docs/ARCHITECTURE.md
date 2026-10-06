# ContribRadar Architecture

## Overview

ContribRadar is a lightweight tool for discovering meaningful opportunities to improve open-source repositories.

The project currently has three main layers:

1. CLI
2. Scanning engine
3. Report generation

## CLI

The command-line interface is implemented in contribradar/cli.py.

It accepts commands such as "contribradar scan ."

The CLI passes the repository path to the scanning engine.

## Scanning engine

The scanning engine is implemented in contribradar/core.py.

It analyzes repositories for signals such as:

- Missing documentation
- Missing tests
- Missing CI
- Missing community files
- Missing security policy
- TODO, FIXME, and HACK markers
- Missing project metadata

Each detected opportunity receives a priority and score.

## Reports

The scanner can produce:

- Human-readable reports
- JSON output

JSON output makes ContribRadar easier to integrate with other tools and automation.

## Future architecture

Future versions may add:

- GitHub API integration
- Dependency analysis
- More programming-language analyzers
- Plugin support
- Web dashboard
- Contributor recommendations
- Organization-wide scanning

The architecture should remain modular so new analyzers can be added without rewriting the core scanning engine.
