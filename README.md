# Supreme Spoon

`Supreme Spoon` leverages [SpiffWorkflow](https://github.com/sartography/SpiffWorkflow) to compile BPMN based 
workflows into a Python class which can be imported into any application. The aim is to reduce 
fricition during the integration, deployment and distribution of BPMN based applications. The compiler and 
generated class have a runtime dependency on `SpiffWorkflow`.

This is very much a work in progress. The current output supports basic CLI integration. `Manual Tasks` have basic support. `User Tasks` are missing.

Currently all BPMN files tested have been generated with the [spiffworkflow-frontend](https://github.com/sartography/spiff-arena/tree/main/spiffworkflow-frontend).

Lots to do, including making this README better.

## Install

`poetry install`

## Compile

To compile all examples, from the root run `./bin/build_examples`. To compile a single BPMN file to a standalone 
Python file:

`poetry run python supreme_spoon/compile.py [PROCESS_ID] [INPUT_FILE] [OUTPUT_FILE]`

For example, to compile the example parallel gateway + manual task workflow:

```
poetry run python supreme_spoon/compile.py "ParallelGatewayManualWorkflow" \
  examples/parallel_gateway_manual/bpmn/parallel_gateway_manual.bpmn \
  examples/parallel_gateway_manual/generated/parallel_gateway_manual.py
```

By convention in the `examples` directory, bpmn files and the generated output are in separate subdirectories.

## Integration

To run the compiled workflow from your application:

```
from generated.parallel_gateway_manual import ParallelGatewayManualWorkflow

if __name__ == "__main__":
    workflow = ParallelGatewayManualWorkflow()
    result = workflow.run()
    print(result)
```

Currently the generated class name matches the process id provided at compile time. This will be configurable 
in the future. More options to configure the execution of `SpiffWorkflow` are also planned (`scripting_additions` 
are the only option supported at this time).

## Execute

Each example has a `run.py` in its directory:

`poetry run python examples/parallel_gateway_manual/run.py`

## Future Plans

In rough order:

1. User Tasks
2. More SpiffWorkflow configuration support
3. Scaffolding support
4. More emitters
5. Single step execution support
