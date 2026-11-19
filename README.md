# LedgerLens

Financial data integration and reconciliation platform.

## Architecture

LedgerLens starts as a **Modular Monolith** with explicit Control Plane and Data Plane boundaries.

- **Control Plane**: workspace, source, pipeline and metadata configuration; component registry and run control.
- **Data Plane**: connectors, ingestion, validation, transformations and reconciliation.
- **Customs**: contract checks and validation gates at data boundaries.
- **Components**: component contracts, compatibility resolution and lifecycle.
- **Domain**: framework-independent business concepts.
- **Application**: use cases and ports.
- **Infrastructure**: persistence, storage, secrets and observability adapters.
- **Orchestration**: Airflow integration; DAGs coordinate work but do not contain business transformations.
- **Serving**: API entry points and read models.

## Development

Requires Python 3.12+ and uv.

```bash
uv sync --all-groups
uv run pytest
uv run ruff check .
uv run mypy src
```

Airflow is intentionally excluded from base dependencies until its runtime version and Python compatibility are pinned.

## Architecture rules

1. Domain must not import infrastructure, API frameworks or orchestration frameworks.
2. Application depends on domain and ports, not concrete adapters.
3. Infrastructure implements ports owned by inner layers.
4. Airflow DAGs orchestrate use cases; they do not implement business processing.
5. Data writes must be attributable to workspace, dataset and execution run.
6. Component resolution uses declared contracts and metadata.
7. Cross-module communication uses public interfaces; avoid circular imports.
8. Financial amounts use decimal-safe types, never binary floating-point.

The canonical Python package lives under `src/ledgerlens`. The existing `modules/resorces` scaffold is retained temporarily for migration safety; new production code must not be added there.

See `docs/adr/ADR-001-modular-monolith.md` and `docs/architecture/module-boundaries.md`.
