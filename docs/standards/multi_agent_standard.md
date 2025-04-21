# Multi-Agent Repository Standard

## Headers
All documentation blocks must start with H1 (#) headers for primary concepts

## Node Interaction Model
- Click Node -> Open Collaborative Canvas
- Each node represents a concept/component
- Real-time discussion threads attached to nodes
- Git-style version control per node

## New Git Commands & Workflow
```bash
# Node-specific commands
git node create <node-name>
git node attach-canvas <node-name>
git node link <source-node> <target-node>

# Multi-agent collaboration
git agent register <agent-id>
git agent assign <node-name>
git agent sync --all

# Canvas operations
git canvas init <node-name>
git canvas commit -m "Update design"
git canvas merge <branch-name>
```

## Standard Canvas Elements
- Concept Map
- Discussion Thread
- Version History
- Agent Assignments
- Related Components
