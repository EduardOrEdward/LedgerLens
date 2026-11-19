# ADR-001: Modular Monolith Architecture

- **Status:** Accepted
- **Date:** 2026-11-19

## Context
LedgerLens needs clear boundaries between Control Plane and Data Plane capabilities without prematurely introducing distributed-service operational complexity.

## Decision
Adopt a Modular Monolith for the initial implementation: one Python codebase and package, organized into modules with explicit responsibilities and dependency rules.

The logical architecture remains hybrid Control Plane / Data Plane. Modular Monolith describes the initial software/deployment organization; it does not collapse those logical responsibilities.

## Rules
1. Domain is framework- and infrastructure-independent.
2. Application owns use cases and ports/interfaces.
3. Infrastructure provides adapters for ports.
4. Cross-module interactions use public interfaces and contracts.
5. Circular dependencies are prohibited.
6. Airflow orchestrates execution; business transformations remain in application/data-plane components.
7. Workers may be deployed separately later without changing domain contracts.

## Consequences
Positive: lower operational complexity, easier local development/testing, explicit module ownership.
Trade-offs: boundaries require discipline, releases are initially coupled, independent scaling may later require separate workers.
