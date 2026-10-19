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

## v0.7 Decision: Cloud AI or Local AI

Before adding natural-language understanding, choose where Void will run its AI
model. This is a design decision; neither option is implemented yet.

### A - Cloud AI

Void sends requests over the internet to a hosted AI service.

**Advantages**

- Easiest way to get a capable model working in an early prototype.
- No need to install or run a large model on the PC.
- Model upgrades and provider infrastructure are managed remotely.

**Disadvantages**

- Requires an internet connection and depends on the provider's availability.
- May have per-request or subscription costs, usage limits, and network latency.
- Prompts leave the PC, so privacy depends on the provider's terms and settings.
- API credentials must be stored and protected securely.

### B - Local AI

Void runs a model on the PC using a local model runtime.

**Advantages**

- Can work offline after the model is installed.
- Prompts can remain on the PC rather than being sent to a hosted service.
- No per-request provider charge; model and runtime can be chosen and controlled.

**Disadvantages**

- Requires downloading, configuring, and maintaining the model and runtime.
- Needs enough memory, storage, and processing power; performance varies by PC.
- A small local model may be slower or less capable than a hosted model.

### Choosing a Starting Point

Choose Cloud AI to get a capable first prototype running quickly if internet
access, provider cost, and sending prompts to a service are acceptable. Choose
Local AI when offline use and keeping prompts on the PC matter most, provided
the computer can run a suitable model. Record the selected provider or model,
expected costs or hardware needs, and how credentials or private data will be
handled before implementation.

## Before Launch

The project is still pre-launch. Continue development through the planned
milestones and verify the assistant's behavior before making a first release.