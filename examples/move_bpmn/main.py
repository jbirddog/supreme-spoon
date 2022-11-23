from move_bpmn import MoveBPMNFiles

if __name__ == "__main__":
    workflow = MoveBPMNFiles()
    result = workflow.run()

    print(result)
    moved_files = result["move_targets"]

    if len(moved_files) == 0:
        print("No downloaded bpmn files found to move")
    
    for moved_file in moved_files:
        print(f"Moved: {moved_file[0]} -> {moved_file[1]}")

