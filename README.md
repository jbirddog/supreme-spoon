# Supreme Spoon

`Supreme Spoon` leverages [SpiffWorkflow](https://github.com/sartography/SpiffWorkflow) to translate BPMN based 
workflows into a standalone Python class which can be imported into any application. The aim is to reduce 
fricition during the integration, deployment and distribution of BPMN based applications.

This is very much a work in progress. The current output supports basic CLI integration. `Manual Tasks` have basic support. `User Tasks` are missing.

Lots to do, including making this README better.

## Install

`poetry install`

## Compile

TODO: This is out of date...

Any of the bpmn files in `examples` can be compiled. Currently the output is put in the same directory:

`poetry run python supreme_spoon/compile.py examples/man_pg.bpmn examples/man_pg.py`

## Execute

`python examples/man_pg.py`
