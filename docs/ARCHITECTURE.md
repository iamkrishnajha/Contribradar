# ContribRadar Architecture

## Overview

ContribRadar is designed as a lightweight tool for discovering meaningful opportunities to improve open-source repositories.

The project currently has three main layers:

1. CLI
2. Scanning engine
3. Report generation

## CLI

The command-line interface is implemented in `contribradar/cli.py`.

It accepts commands such as:

```text
contribradar scan .
