from generated.move_bpmn import MoveBPMNFiles

if __name__ == "__main__":
    workflow = MoveBPMNFiles()
    result = workflow.run()

    moved_files = result["move_targets"]

    print(f"Found {len(moved_files)} files to move.")
    
    for moved_file in moved_files:
        print(f"Moved: {moved_file[0]} -> {moved_file[1]}")

