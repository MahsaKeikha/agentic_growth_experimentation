"""Fail-closed governance for F129 Agentic Growth Experimentation."""

PROTECTED_ACTIONS = {
    "activate_experiment",
    "change_production_experience",
    "change_pricing_or_offer",
    "change_eligibility",
    "terminate_experiment_early",
    "external_platform_write",
}

REQUIRED_REVIEWS = (
    "hypothesis_reviewed",
    "experiment_design_reviewed",
    "measurement_reviewed",
    "risk_reviewed",
    "privacy_consent_reviewed",
    "fairness_reviewed",
    "evidence_provenance_reviewed",
    "qualified_experiment_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding experiment action is outside reference-system scope"}
    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required experiment review", "missing": missing}
    checks = {
        "dark_pattern_risk": "dark pattern or manipulative treatment detected",
        "privacy_consent_gap": "privacy, consent, or data-use gap unresolved",
        "fairness_risk": "fairness, discrimination, or disparate-impact risk unresolved",
        "sample_integrity_gap": "randomization, assignment, or sample-integrity gap unresolved",
        "metric_integrity_gap": "metric definition, instrumentation, or analysis gap unresolved",
        "unsafe_guardrail": "safety, quality, or customer-harm guardrail unresolved",
        "premature_stopping_risk": "early stopping or peeking risk unresolved",
        "evidence_provenance_gap": "experiment evidence provenance incomplete",
    }
    blockers = [message for key, message in checks.items() if context.get(key)]
    if blockers:
        return {"allowed": False, "reason": "growth-experiment governance blocker", "blockers": blockers}
    return {"allowed": True, "reason": "experiment support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS
