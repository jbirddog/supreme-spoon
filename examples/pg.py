
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

def parallel_gateway(id, config, k):
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

def script_task(id, config, k):
    def impl(data):
        print(f"In script_task: {id}")
        return k(data)
    return impl

def start_event(id, config, k):
    def impl(data):
        print(f"In start_event: {id}")
        return k(data)
    return impl


if __name__ == "__main__":
    print("Running 'Proccess_3qizfj5'...")
    workflow = start_event("Event_056euq0", [('outgoing', {}, 'Gateway_017jnp6')], parallel_gateway("Gateway_017jnp6", [('incoming', {}, 'Event_056euq0'), ('outgoing', {}, 'Activity_1ewv0kb'), ('outgoing', {}, 'Activity_115woll'), ('outgoing', {}, 'Activity_1g1cdox')], fan_out([script_task("Activity_1ewv0kb", [('incoming', {}, 'Gateway_017jnp6'), ('outgoing', {}, 'Gateway_0chrwmq'), ('script', {}, 'var1=4')], parallel_gateway("Gateway_0chrwmq", [('incoming', {}, 'Activity_115woll'), ('incoming', {}, 'Activity_1g1cdox'), ('incoming', {}, 'Activity_1ewv0kb'), ('outgoing', {}, 'Activity_0kapn49')], script_task("Activity_0kapn49", [('incoming', {}, 'Gateway_0chrwmq'), ('outgoing', {}, 'Event_1kj6hcj'), ('script', {}, 'result = var1 + 3')], end_event("Event_1kj6hcj", [('incoming', {}, 'Activity_0kapn49')], identity)))), script_task("Activity_115woll", [('incoming', {}, 'Gateway_017jnp6'), ('outgoing', {}, 'Gateway_0chrwmq'), ('script', {}, 'var1=6')], parallel_gateway("Gateway_0chrwmq", [('incoming', {}, 'Activity_115woll'), ('incoming', {}, 'Activity_1g1cdox'), ('incoming', {}, 'Activity_1ewv0kb'), ('outgoing', {}, 'Activity_0kapn49')], script_task("Activity_0kapn49", [('incoming', {}, 'Gateway_0chrwmq'), ('outgoing', {}, 'Event_1kj6hcj'), ('script', {}, 'result = var1 + 3')], end_event("Event_1kj6hcj", [('incoming', {}, 'Activity_0kapn49')], identity)))), script_task("Activity_1g1cdox", [('incoming', {}, 'Gateway_017jnp6'), ('outgoing', {}, 'Gateway_0chrwmq'), ('script', {}, 'var1=7')], parallel_gateway("Gateway_0chrwmq", [('incoming', {}, 'Activity_115woll'), ('incoming', {}, 'Activity_1g1cdox'), ('incoming', {}, 'Activity_1ewv0kb'), ('outgoing', {}, 'Activity_0kapn49')], script_task("Activity_0kapn49", [('incoming', {}, 'Gateway_0chrwmq'), ('outgoing', {}, 'Event_1kj6hcj'), ('script', {}, 'result = var1 + 3')], end_event("Event_1kj6hcj", [('incoming', {}, 'Activity_0kapn49')], identity))))])))
    result = workflow({})
    print(f"result: {result}")
