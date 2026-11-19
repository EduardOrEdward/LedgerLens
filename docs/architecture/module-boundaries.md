# Module boundaries

## Dependency direction
Entry points (API, CLI, Airflow) call Application use cases. Application depends on Domain and ports. Infrastructure adapters implement those ports.

```text
API / CLI / Airflow -> Application -> Domain
Infrastructure adapters implement Application-owned ports.
```

Domain must never import infrastructure, FastAPI, SQLAlchemy or Airflow.

## Control Plane
Owns workspace/source/pipeline configuration, metadata, component registry and run submission/monitoring. It does not perform heavy transformations.

## Data Plane
Owns source extraction, validation, transformations, storage interactions and reconciliation execution.

## Customs
Owns contract checks and validation gates at important data boundaries.

## Components
A component is a capability with a declared contract, not necessarily a microservice. Resolution considers operation, input format, schema compatibility, metadata, version policy and execution constraints.

## Storage
- Bronze: source-aligned, append-oriented and replayable raw data.
- Silver: validated and normalized canonical records.
- Gold: business-ready reconciliation and analytics outputs.
- Metadata Store: versioned passports, schemas, configurations and execution metadata.

## Orchestration
Airflow manages lifecycle, dependencies, scheduling, retries and execution visibility. DAGs must not contain source parsing or business transformation logic.

## Legacy scaffold
The original `modules/resorces` tree is retained for migration safety only. New code belongs in `src/ledgerlens`.
