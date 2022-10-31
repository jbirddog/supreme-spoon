# supreme-spoon

POC workflow compiler. Currently has a BPMN frontend and a Python CPS backend. Very early stages but does demonstrate compiling a bpmn file to a standalone python file for subsequent execution. Currently mock Start/End Events, Manual and Script Tasks and Parallel Gateways are implemented. Please note these are just mock imlementations - their only aim at this point is to prove the idea.

## Install

`poetry install`

## Compile

Any of the bpmn files in `examples` can be compiled. Currently the output is put in the same directory:

`poetry run python supreme_spoon/compile.py examples/man_pg.bpmn examples/man_pg.py`

## Execute

`python examples/man_pg.py`
