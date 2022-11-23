from copybpmn import CopyBPMNFiles

def copy_bpmn_files():
    print("copy bpmn files")

if __name__ == "__main__":
    scripting_additions = {
        "copy_bpmn_files": copy_bpmn_files,
    }

    workflow = CopyBPMNFiles(
        scripting_additions=scripting_additions,
    )
    
    result = workflow.run()
    print(result)
