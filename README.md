# TMC 2027 Multi-Agent Vulnerability Analysis

A research framework for discovering and analyzing **emergent vulnerabilities** in multi-agent AI systems using specialized vulnerability story generators (VSGs) and attack scenario modeling.

## What This Project Does

This project demonstrates a novel approach to security analysis for multi-agent systems by focusing on **emergent vulnerabilities** - security failures that only arise from interactions between multiple AI agents and couldn't occur with a single agent.

**Target System**: TMC 2027 Multi-Agent Travel Booking System

- 13+ specialized AI agents (flight booking, hotel reservation, payment coordination, etc.)
- 4 communication protocols: ANS (discovery), A2A (agent-to-agent), MCP (LLM integration), AP2 (payments)
- Complex coordination workflows across distributed agents

**Key Innovation**: Rather than analyzing individual agent vulnerabilities, this framework identifies failure modes that emerge from multi-agent coordination, timing mismatches, dependency cascades, and behavioral dynamics.

## The 5-Stage Analysis Pipeline

### Stage 1: Vulnerability Story Generation (VSG)

Four specialized AI agents generate pre-mortem failure narratives from different perspectives:

- **BVSG (Behavioral)** - Game-theoretic failures, incentive misalignment, adversarial dynamics
- **DCVSG (Dependency Cascade)** - Sequential failure propagation along dependency chains
- **RVSG (Resonant)** - Amplification through alignment, feedback loops, synchronization failures
- **TVSG (Temporal)** - Timing mismatches, race conditions, phase-locking, coordination failures

**Output**: 8 vulnerability stories (2 per VSG) in JSON and Markdown formats

### Stage 2: Deduplication

Removes duplicate or highly similar vulnerability stories across the 4 generators.

**Output**: ~6-7 unique vulnerability stories

### Stage 3: Plausibility Check

Scores each vulnerability across 5 dimensions:

- Technical Feasibility
- Emergence Validity (does it truly require multi-agent interaction?)
- Impact Severity
- Detection Difficulty
- Exploit Complexity

**Output**: Scored and filtered vulnerabilities ready for attack modeling

### Stage 4: Attack Scenario Generation

Uses the SCAMPER framework to generate creative attack scenarios for each vulnerability:

- **S**ubstitute, **C**ombine, **A**dapt, **M**odify, **P**ut to another use, **E**liminate, **R**everse

**Output**: ~8-16 concrete attack scenarios demonstrating realistic exploitation paths

### Stage 5: Executive Summary Generation

LLM-powered synthesis that:

- Identifies remaining duplicates across vulnerability stories
- Assesses severity using both vulnerability narratives AND attack scenarios
- Prioritizes findings (CRITICAL/HIGH/MEDIUM/LOW) based on:
  - Business impact
  - Exploitability (validated by attack scenarios)
  - Emergence validity
  - Detection difficulty
- Produces business-focused 2-3 page report with strategic recommendations

**Output**: Executive summary report ready for leadership review

## Key Files

### Main Notebook

- **`tmc-dc-demo.ipynb`** - Complete 5-stage pipeline implementation

### Input Prompts

- **`prompts/bvsg-prompt.md`** - Behavioral vulnerability generator
- **`prompts/dcvsg-prompt.md`** - Dependency cascade generator
- **`prompts/rvsg-prompt.md`** - Resonant vulnerability generator
- **`prompts/tvsg-prompt.md`** - Temporal vulnerability generator
- **`prompts/attack-generator-prompt.md`** - SCAMPER attack scenario generator
- **`prompts/report-generator-executive-prompt.md`** - Executive summary generator

### System Documentation

- **`system/tmc_booking_epic.md`** - Complete TMC 2027 system specification with 13 user stories
- **`protocols/`** - Threat models for ANS, A2A, MCP, and AP2 protocols

### Outputs

- **`artifacts/runs/{run_id}/`** - Analysis outputs organized by run:
  - `01-vsg-outputs/` - Raw vulnerability stories
  - `02-deduplicated/` - Unique stories
  - `03-plausibility/` - Scored vulnerabilities
  - `04-attack-stories/` - Attack scenarios
  - `05-reports/` - Executive summary

## Quick Start

### Setup

```bash
cd ~/Documents/ERIMAS/TMC-Washington-Nov-2025
source erimas/bin/activate
jupyter lab
```

### Running the Pipeline

1. Open `tmc-dc-demo.ipynb` in Jupyter Lab
2. Set your `ANTHROPIC_API_KEY` in `.env` file
3. Run cells sequentially from Stage 1 through Stage 5
4. Review outputs in `artifacts/runs/{run_id}/`

### Expected Runtime

- Stage 1 (VSG): ~8-10 minutes (4 parallel LLM calls, 2 stories each)
- Stage 2 (Dedup): ~2 minutes
- Stage 3 (Plausibility): ~5-7 minutes (1 call per story)
- Stage 4 (Attacks): ~10-15 minutes (2-3 attacks per vulnerability)
- Stage 5 (Report): ~3-5 minutes (single synthesis call)

**Total**: ~30-40 minutes per complete analysis run

## Why This Approach Matters

Traditional security analysis focuses on individual component vulnerabilities. But in multi-agent systems, the most dangerous failures emerge from:

- **Cascade effects**: One agent's failure triggers failures in dependent agents
- **Timing mismatches**: Agents operating at different speeds create race conditions
- **Behavioral dynamics**: Agents optimizing locally create system-wide instability
- **Resonant failures**: Multiple agents amplifying the same pattern causes threshold breaches

These emergent vulnerabilities are **invisible to single-agent security testing** and require specialized analysis techniques.

## Example Findings

From our TMC 2027 analysis:

- **Dependency Cascade**: ANS registry failure → agent discovery fails → all booking agents stall → payment timeouts → financial reconciliation failures (5-agent cascade)
- **Temporal Mismatch**: Flight confirmation arrives after hotel cancellation deadline due to slow MCP LLM call (cross-agent timing failure)
- **Resonant Amplification**: All agents query same pricing API simultaneously after shared cache expiry → thundering herd → service degradation for all users
- **Behavioral Perverse Incentive**: Payment coordinator agent optimizes for transaction speed over verification depth when under load, creating fraud exposure

## Key Concepts

### Emergence

All vulnerability stories must demonstrate **emergence** - the failure only occurs through multi-agent interaction and couldn't happen with a single agent. This is the critical discriminator that makes this analysis valuable.

### Attack Scenario Validation

Vulnerabilities are paired with concrete attack scenarios to validate:

- The weakness is actually exploitable (not just theoretical)
- Multiple attack paths increase priority
- Sophisticated attacks require sophisticated defenses

### Business-Focused Output

The executive summary translates technical vulnerabilities into business impact:

- Financial losses
- Reputational damage
- Operational disruption
- Strategic recommendations with timelines (0-30 days, 30-90 days, 90+ days)

## Development Notes

- Research project, not production software
- Uses Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`) with temperature=0.0 for deterministic analysis
- Jupyter notebook environment for interactive exploration
- Outputs in JSON (structured), Markdown (narrative), and PNG (diagrams)
- See `CLAUDE.md` for detailed development guidance

## References

- Multi-agent coordination patterns from real-world systems (AWS, financial trading, IoT)
- Historical failure examples: Flash Crash, Knight Capital, Y2K, Heartbleed, Log4j
- Protocol specifications: ANS, A2A (JSON-RPC), MCP, AP2 (mandate chains)
