
# GENERATED BY supreme-spoon

identity = lambda x: x

def fan_out(ks):
    def impl(data):
        results = [k(data) for k in ks]
        for result in results:
            if result is not None:
                return result
    return impl

def end_event(id, config, k):
    def impl(data):
        print(f"In end_event: {id}")
        return k(data)
    return impl

pg_instances = {}
def parallel_gateway(id, config, k):
    def make():
        expected_in = len(list(filter(lambda c: c[0] == 'incoming', config)))
        conds = {"let_in": 0}

        def impl(data):
            print(f"In parallel_gateway: {id}")
            assert conds["let_in"] < expected_in
            conds["let_in"] += 1
            print(f"  - expecting {expected_in}, seen {conds['let_in']}")
            if conds["let_in"] != expected_in:
                return None
            return k(data)
        return impl
    if id not in pg_instances:
        pg_instances[id] = make()
    return pg_instances[id]

def script_task(id, config, k):
    script = list(filter(lambda c: c[0] == 'script', config))[0][2]
    def impl(data):
        print(f"In script_task: {id} - {script}")
        data[f"result_{id}"] = f"TODO_EVAL({script})"
        return k(data)
    return impl

def start_event(id, config, k):
    def impl(data):
        print(f"In start_event: {id}")
        return k(data)
    return impl


if __name__ == "__main__":
    print("Running 'empty_workflow'...")
    workflow = start_event("StartEvent_1", [('outgoing', {}, 'EndEvent_0q4qzl9')], end_event("EndEvent_0q4qzl9", [('incoming', {}, 'StartEvent_1')], identity))
    result = workflow({})
    print(f"result: {result}")
