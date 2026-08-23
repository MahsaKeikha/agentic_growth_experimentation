"""Held-out governance scenarios for F129."""
from safety.policy import REQUIRED_REVIEWS, authorize


def base():
    return {key: True for key in REQUIRED_REVIEWS}


SCENARIOS = [
    ({}, False),
    (base(), True),
    (base() | {"dark_pattern_risk": True}, False),
    (base() | {"privacy_consent_gap": True}, False),
    (base() | {"fairness_risk": True}, False),
    (base() | {"sample_integrity_gap": True}, False),
    (base() | {"metric_integrity_gap": True}, False),
    (base() | {"unsafe_guardrail": True}, False),
    (base() | {"premature_stopping_risk": True}, False),
    (base() | {"evidence_provenance_gap": True}, False),
]


def main():
    for index, (context, expected) in enumerate(SCENARIOS, 1):
        actual = authorize("release_support_package", context)["allowed"]
        assert actual is expected, f"scenario {index}: expected {expected}, got {actual}"
    print(f"F129 held-out governance: {len(SCENARIOS)}/{len(SCENARIOS)} passed")


if __name__ == "__main__":
    main()
