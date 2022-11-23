from move_bpmn import MoveBPMNFiles

def copy_bpmn_files():
    print("copy bpmn files")

if __name__ == "__main__":
    scripting_additions = {
        "copy_bpmn_files": copy_bpmn_files,
    }

    workflow = MoveBPMNFiles(
        scripting_additions=scripting_additions,
    )
    
    result = workflow.run()
    print(result)
