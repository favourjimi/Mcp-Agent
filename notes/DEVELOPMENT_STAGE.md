# Pre-Launch Development Stage

- **Release stage:** Pre-launch, in development
- **Current version:** v0.6
- **Current focus:** Organizing commands into reusable tools

| Version | Capability | Status |
| --- | --- | --- |
| v0.1 | Basic command-line assistant | Built |
| v0.2 | Launch Windows applications | Built |
| v0.3 | Flexible command recognition | Built |
| v0.4 | Persistent local memory | Built |
| v0.5 | Remember and retrieve custom facts | Built |
| v0.6 | Organize commands into reusable tools | Building now |
| v0.7 | Connect an AI model for natural-language understanding | Planned |
| Later | Voice, vision, and more advanced PC control | Planned |

## Current Milestone: v0.6

The current work is moving commands into reusable tools. Application launching
is handled by `open_application` in `void/void_tools.py`, which supports Notepad,
Calculator, and Paint.

## Completed Milestones

The v0.4 memory system persists the user's name and saved facts in a local JSON
file. In v0.5, Void can save facts with `remember <fact>` and retrieve matching
facts with `what is <topic>` or `what are <topic>`.

## Before Launch

The project is still pre-launch. Continue development through the planned
milestones and verify the assistant's behavior before making a first release.