# Artifacts Directory

This directory contains generated outputs from the vulnerability analysis pipeline.

## Structure

```
artifacts/
├── runs/
│   └── {run_id}/                          # Each analysis run (e.g., "2025-10-19-143022")
│       ├── metadata.json                  # Run configuration and statistics
│       ├── inputs/                        # Copies of input documents
│       ├── 01-vsg-outputs/                # Raw VSG outputs (JSON + Markdown)
│       ├── 02-deduplicated/               # After deduplication stage
│       ├── 03-plausibility/               # After plausibility filtering
│       ├── 04-attack-stories/             # SCAMPER-generated attack ideas
│       ├── 05-jury/                       # Jury evaluation results
│       └── 06-reports/                    # Final reports (exec + technical)
│
└── templates/
    ├── story-schema.json                  # JSON schema for vulnerability stories
    └── metadata-schema.json               # JSON schema for run metadata
```

## Pipeline Stages

1. **VSG Outputs** - Four vulnerability story generators each produce 2 stories (8 total)
2. **Deduplication** - Remove duplicate or highly similar stories
3. **Plausibility** - Score and filter stories based on feasibility
4. **Attack Stories** - Generate SCAMPER-based attack scenarios
5. **Jury** - Judge evaluation and consensus scoring
6. **Reports** - Generate executive and technical reports

## Creating a New Run

```bash
# Create run directory
RUN_ID=$(date +%Y-%m-%d-%H%M%S)
mkdir -p "artifacts/runs/${RUN_ID}"/{inputs,01-vsg-outputs,02-deduplicated,03-plausibility,04-attack-stories,05-jury,06-reports}
```

## File Formats

- **JSON** - Structured data for programmatic processing
- **Markdown** - Human-readable narratives and reports
- **PDF** - Final report deliverables (generated from Markdown)

## Validation

Use the JSON schemas in `templates/` to validate story and metadata structures.
