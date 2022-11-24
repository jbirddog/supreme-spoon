from generated.parallel_gateway import ParallelGatewayWorkflow

if __name__ == "__main__":
    workflow = ParallelGatewayWorkflow()
    result = workflow.run()
    print(result)
