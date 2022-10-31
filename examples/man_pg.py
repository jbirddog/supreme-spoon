
# GENERATED BY supreme-spoon

#
# This is an early POC to demonstrate compiling BPMN diagrams to a static Python file.
#

#
# Example runtime
#

def configs_named(config, name):
    return list(filter(lambda c: c[0] == name, config))

def config_named(config, name):
    return configs_named(config, name)[0]

def config_value_named(config, name):
    return config_named(config, name)[2]

def ext_named(config, ext_name):
    ext_elems = config_named(config, 'extensionElements')
    return configs_named(ext_elems[2], ext_name)[0]

def ext_value_named(config, ext_name):
    return ext_named(config, ext_name)[2]

def fan_out(ks):
    def impl(data):
        results = [k(data) for k in ks]
        for result in results:
            if result is not None:
                return result
    return impl

def end_k(data):
    print("Complete!")
    print(f"data: {data}")


#
# Example bpmn element implementations
#

def end_event(id, config, k):
    def impl(data):
        print(f"In end_event: {id}")
        k(data)
    return impl

def manual_task(id, config, k):
    import os
    prompt = ext_value_named(config, 'instructionsForEndUser')
    def impl(data):
        print(f"In manual_task: {id}")
        input(prompt)
        print(config)
        k(data)
    return impl

pg_instances = {}
def parallel_gateway(id, config, k):
    def make():
        expected_in = len(configs_named(config, 'incoming'))
        conds = {"let_in": 0}

        def impl(data):
            assert conds["let_in"] < expected_in
            conds["let_in"] += 1
            if conds["let_in"] == expected_in:
                print(f"In parallel_gateway: {id}")
                k(data)
        return impl
    if id not in pg_instances:
        pg_instances[id] = make()
    return pg_instances[id]

def script_task(id, config, k):
    script = config_value_named(config, 'script')
    def impl(data):
        print(f"In script_task: {id} - {script}")
        data[f"result_{id}"] = f"TODO_EVAL({script})"
        k(data)
    return impl

def start_event(id, config, k):
    def impl(data):
        print(f"In start_event: {id}")
        k(data)
    return impl


steps = {}
__k = lambda id: steps[id]

steps["Event_1kj6hcj"] = end_event("Event_1kj6hcj", [('incoming', {}, 'Activity_0kapn49')], end_k)
steps["Activity_0kapn49"] = script_task("Activity_0kapn49", [('incoming', {}, 'Gateway_0chrwmq'), ('outgoing', {}, 'Event_1kj6hcj'), ('script', {}, 'result = var1 + xyz_var')], __k("Event_1kj6hcj"))
steps["Gateway_0chrwmq"] = parallel_gateway("Gateway_0chrwmq", [('incoming', {}, 'Activity_115woll'), ('incoming', {}, 'Activity_1g1cdox'), ('incoming', {}, 'Activity_1ewv0kb'), ('outgoing', {}, 'Activity_0kapn49')], __k("Activity_0kapn49"))
steps["Activity_1ewv0kb"] = script_task("Activity_1ewv0kb", [('incoming', {}, 'Gateway_017jnp6'), ('outgoing', {}, 'Gateway_0chrwmq'), ('script', {}, 'var1=4')], __k("Gateway_0chrwmq"))
steps["Activity_115woll"] = script_task("Activity_115woll", [('incoming', {}, 'Gateway_017jnp6'), ('outgoing', {}, 'Gateway_0chrwmq'), ('script', {}, 'var1=6')], __k("Gateway_0chrwmq"))
steps["Activity_1g1cdox"] = script_task("Activity_1g1cdox", [('incoming', {}, 'Gateway_017jnp6'), ('outgoing', {}, 'Gateway_0chrwmq'), ('script', {}, 'var1=7')], __k("Gateway_0chrwmq"))
steps["Gateway_017jnp6"] = parallel_gateway("Gateway_017jnp6", [('incoming', {}, 'Activity_0e2pojh'), ('outgoing', {}, 'Activity_1ewv0kb'), ('outgoing', {}, 'Activity_115woll'), ('outgoing', {}, 'Activity_1g1cdox')], fan_out([__k("Activity_1ewv0kb"), __k("Activity_115woll"), __k("Activity_1g1cdox")]))
steps["Activity_0e2pojh"] = manual_task("Activity_0e2pojh", [('extensionElements', {}, [('instructionsForEndUser', {}, 'Press any key to continue the demo....')]), ('incoming', {}, 'Event_056euq0'), ('outgoing', {}, 'Gateway_017jnp6')], __k("Gateway_017jnp6"))
steps["Event_056euq0"] = start_event("Event_056euq0", [('outgoing', {}, 'Activity_0e2pojh')], __k("Activity_0e2pojh"))



#
# Workflow expressed in CPS style. Would allow starting from/resuming at any point
#
workflow = steps["Event_056euq0"]

if __name__ == "__main__":
    print("Running 'Proccess_3qizfj5'...")
    
    workflow({})
