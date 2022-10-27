
identity = lambda x: x

def end_event(id, k):
    def impl(data):
        print(f"In end_event: {id}")
        return k(data)
    return impl

def start_event(id, k):
    def impl(data):
        print(f"In start_event: {id}")
        return k(data)
    return impl


if __name__ == "__main__":
    print("Running 'empty_workflow'...")
    workflow = start_event("StartEvent_1", end_event("EndEvent_0q4qzl9", identity))
    result = workflow({})
    print(f"result: {result}")
