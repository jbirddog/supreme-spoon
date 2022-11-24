from generated.parallel_gateway_manual import ParallelGatewayManualWorkflow

if __name__ == "__main__":
    workflow = ParallelGatewayManualWorkflow()
    result = workflow.run()
    print(result)
