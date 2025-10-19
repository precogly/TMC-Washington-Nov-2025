# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **TMC Washington Nov 2025** project - a vulnerability analysis framework for multi-agentic systems. The project demonstrates and analyzes emergent risks in a complex travel booking system that uses multiple AI agents communicating via four protocols: ANS (Agent Name Service), A2A (Agent-to-Agent), MCP (Model Context Protocol), and AP2 (Agent Payment Protocol).

## Environment Setup

### Virtual Environment

```bash
# Navigate to project root
cd ~/Documents/ERIMAS/TMC-Washington-Nov-2025

# Activate the virtual environment (required before all operations)
source erimas/bin/activate

# Launch Jupyter Lab for notebook work
jupyter lab
```

### Environment Variables

- API keys and sensitive config stored in `.env` (gitignored)
- Use `python-dotenv` to load environment variables: `load_dotenv(dotenv_path=".env", override=True)`
- ANTHROPIC_API_KEY is configured for Claude API access

## Repository Structure

### Core Directories

**`prompts/`** - Specialized vulnerability story generator (VSG) prompts

- `bvsg-prompt.md` - Behavioral Vulnerabilities Stories Generator
- `dcvsg-prompt.md` - Dependency Cascade Vulnerabilities Stories Generator
- `rvsg-prompt.md` - Resonant Vulnerabilities Stories Generator
- `tvsg-prompt.md` - Temporal Vulnerabilities Stories Generator
- Each prompt is a specialized agent definition for a 4-agent vulnerability analysis pipeline

**`meta-prompts/`** - Meta-prompts that guide the creation of VSG prompts

- Templates and instructions for building vulnerability story generators

**`protocols/`** - Protocol threat model documents

- `a2a-threat-model.md` - Agent-to-Agent communication protocol analysis
- `ans-threat-model.md` - Agent Name Service analysis
- `ap2-threat-model.md` - Agent Payment Protocol analysis
- `mcp_threat_model.md` - Model Context Protocol analysis

**`system/`** - System architecture documentation

- `tmc_booking_epic.md` - Complete epic describing multi-agent travel booking flow with 13 user stories, showing protocol interactions (ANS→A2A→MCP→AP2)

**`artifacts/`** - Pipeline outputs organized by run

- `runs/{run_id}/` - Each analysis run with timestamped or named ID
  - `01-vsg-outputs/` - Raw outputs from 4 VSGs (JSON + Markdown, 8 stories total)
  - `02-deduplicated/` - After deduplication stage
  - `03-plausibility/` - After plausibility filtering
  - `04-attack-stories/` - SCAMPER-generated attack scenarios
  - `05-jury/` - Jury evaluation and scoring
  - `06-reports/` - Final executive and technical reports
- `templates/` - JSON schemas for stories and metadata

**`tmc-2027-pre-mortems/`** - Legacy pre-mortem narratives (pre-pipeline)

**`old-prompts-long-unstandardized/`** - Archive of earlier prompt iterations

### Key Notebooks

**`tmc-dc-demo.ipynb`** - Main demonstration notebook for TMC system

- Visualizes multi-agent architecture using Graphviz
- Shows protocol flows and agent interactions

**`mini-tests.ipynb`** - Testing and experimentation notebook

- API connectivity tests (OpenAI, Anthropic)
- Graphviz visualization experiments

## Conceptual Architecture

### The 4-Agent Vulnerability Analysis Pipeline

This project implements a specialized pipeline where four AI agents analyze different types of emergent vulnerabilities:

1. **Behavioral Vulnerabilities (BVSG)** - Game-theoretic failures, incentive misalignment, adversarial dynamics, herding behaviors
2. **Dependency Cascade Vulnerabilities (DCVSG)** - Sequential failure propagation along dependency chains (A→B→C→D)
3. **Resonant Vulnerabilities (RVSG)** - Amplification through alignment (monoculture, feedback loops, thresholds, synchronization)
4. **Temporal Vulnerabilities (TVSG)** - Timing mismatches, race conditions, phase-locking, coordination failures across time scales

Each VSG agent generates exactly 2 pre-mortem failure narratives for a given multi-agentic system specification (8 stories total across all 4 VSGs).

### The TMC 2027 Travel Booking System

The reference system being analyzed is a multi-agent travel booking system with:

**Agents:**

- PersonalAssistantAgent (orchestrator)
- FlightBookingAgent, HotelReservationAgent, EventRegistrationAgent
- PaymentCoordinatorAgent, AccountingAgent
- CalendarAgent, NotificationAgent, TravelMonitoringAgent
- VenueInformationAgent, ItineraryGeneratorAgent
- ANS Registry, UserProfileAgent

**Protocols:**

- **ANS** - Agent discovery and identity verification
- **A2A** - Inter-agent communication (JSON-RPC over HTTP/HTTPS, SSE for streaming)
- **MCP** - Integration with LLMs and external APIs
- **AP2** - Payment authorization with mandate chains (Intent→Cart→Payment)

**Key Flow:** User request → ANS discovery → LLM parsing (MCP) → parallel booking agents (A2A) → payment coordination (AP2) → post-booking services (calendar, itinerary, monitoring)

## Vulnerability Analysis Pipeline

The complete analysis pipeline consists of 6 stages:

1. **VSG Generation** - Run 4 VSGs (BVSG, DCVSG, RVSG, TVSG) to produce 8 stories total (2 per VSG)
2. **Deduplication** - Remove duplicate or highly similar vulnerability stories
3. **Plausibility Check** - Score and filter stories based on feasibility
4. **Attack Story Generation** - Use SCAMPER framework to generate creative attack scenarios
5. **Jury Evaluation** - Judge stories for quality, impact, and actionability
6. **Report Generation** - Produce executive summary and technical report

### Vulnerability Story Format

Each vulnerability story generated follows this structure:

- **Title** - Concise descriptive name
- **Pattern Type** - Primary classification
- **Mechanism** - 2-3 sentences on specific dynamics
- **Narrative** - 200-300 word pre-mortem failure story
- **Key Factors** - Bulleted list of contributing elements
- **Impact Analysis** - Quantified consequences
- **Emergence Explanation** - Why this requires multi-agent interaction

Stories are stored in both JSON (structured, validated against `artifacts/templates/story-schema.json`) and Markdown (human-readable) formats.

## Working with Visualizations

The project uses **Graphviz** to visualize agent architectures and protocol flows:

```python
from graphviz import Digraph

dot = Digraph(comment='Architecture', format='png')
dot.attr(rankdir='TB', splines='ortho')
# Add nodes and edges
dot.render()  # Generates PNG
```

Key visualization patterns:

- Cluster subgraphs for logical layers (Discovery, Booking, Payment, Post-Booking)
- Color coding by protocol type (ANS=purple, A2A=orange, MCP=teal, AP2=green)
- Edge labels showing protocol and sequence numbers

## Important Concepts

### Emergence Requirement

All vulnerability stories MUST demonstrate emergence - the vulnerability must arise from multi-agent interactions and couldn't occur with a single agent. This is the critical discriminator.

### Protocol Boundaries

- **ANS** - Discovery only, not for ongoing communication
- **A2A** - Peer-to-peer agent collaboration with task lifecycle management
- **MCP** - Client-server for tools/resources, unidirectional
- **AP2** - Payment-specific with cryptographic mandate chains

### Vulnerability Distinctions

- **Dependency cascades** ≠ **Resonant failures** (sequential propagation vs. simultaneous amplification)
- **Temporal coordination failure** (agents fail to sync) ≠ **Resonant synchronization** (successful sync causes overload)
- **Behavioral** focuses on strategic/incentive dynamics, not implementation bugs

## Historical Examples Database

The VSG prompts contain extensive historical examples:

- **Behavioral**: 2008 Financial Crisis, Cobra Effect, Flash Crash, Goodhart's Law
- **Dependency**: AWS S3 Outage, Knight Capital, Target Canada, Fastly CDN
- **Resonant**: Y2K, Heartbleed, Log4j, Bank Runs, Flash Crash, Thundering Herd
- **Temporal**: Ariane 5, Therac-25, Knight Capital, Nest Thermostat, Air France 447

These ground the analysis in real-world failure patterns.

## Creating a New Analysis Run

```bash
# Create timestamped run directory
RUN_ID=$(date +%Y-%m-%d-%H%M%S)
mkdir -p "artifacts/runs/${RUN_ID}"/{inputs,01-vsg-outputs,02-deduplicated,03-plausibility,04-attack-stories,05-jury,06-reports}

# Or use a named run
mkdir -p "artifacts/runs/tmc-2027-run-001"/{inputs,01-vsg-outputs,02-deduplicated,03-plausibility,04-attack-stories,05-jury,06-reports}
```

## Development Notes

- This is primarily a **research and analysis** project, not a production software system
- The Jupyter notebooks are the main working environment
- Manual cell-by-cell testing approach for pipeline development
- Outputs: JSON (structured, validated), Markdown (narrative), PNG (diagrams), PDF (reports)
- The `erimas/` virtual environment directory is gitignored
- Generated artifacts go in `artifacts/runs/` (gitignored)
- API responses are cached in `.cache/` (gitignored)
