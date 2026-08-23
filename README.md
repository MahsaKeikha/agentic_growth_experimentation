# F129 | Agentic Growth Experimentation | L3 Gold Standard | v1.0

A governed five-agent reference architecture for growth experimentation across hypothesis formation, experiment design, measurement, risk review, causal inference, evidence provenance, fairness, privacy, guardrails, and qualified human approval.

F129 is decision-support only. It can structure hypotheses, design experiments, analyze measurements, identify risks, and prepare reviewed experiment packages, but it cannot autonomously activate experiments, change production experiences, alter pricing or offers, change eligibility, terminate experiments early, or write to external production systems.

## Growth experimentation lifecycle

```text
Problem and Evidence
        -> Hypothesis Formation
        -> Experiment Design
        -> Measurement and Guardrails
        -> Risk, Fairness, Privacy, and Integrity Review
        -> Qualified Human Experiment Approval
        -> Human-Controlled Activation
        -> Analysis and Learning
```

The workflow fails closed when required reviews are missing or when dark-pattern, privacy, fairness, sample-integrity, metric-integrity, safety, premature-stopping, or provenance risks remain unresolved.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Hypothesis Agent | Frames evidence-backed growth hypotheses and expected mechanisms | What causal change is being proposed, for whom, and why? |
| Experiment Agent | Designs assignments, treatments, control conditions, duration, sample logic, and guardrails | Is the experiment capable of answering the question responsibly? |
| Measurement Agent | Defines primary metrics, secondary metrics, guardrails, instrumentation, and analysis methods | How will success, harm, uncertainty, and causal impact be measured? |
| Risk Agent | Reviews privacy, fairness, manipulation, customer harm, operational risk, and experiment integrity | What could invalidate the result or harm users? |
| Review Agent | Integrates evidence, methodology, risk, provenance, and human approval state | Is the experiment package ready for qualified human review? |

Agents support experimentation judgment. They do not replace product owners, statisticians, data scientists, legal counsel, privacy teams, ethics reviewers, safety teams, engineers, executives, or authorized production operators.

## Repository structure

```text
AGENTS/
├── hypothesis_agent.py
├── experiment_agent.py
├── measurement_agent.py
├── risk_agent.py
└── review_agent.py

SKILLS/
├── hypothesis_reasoning.py
├── experiment_design.py
├── measurement.py
├── risk_reasoning.py
└── review_reasoning.py

TOOLS/
├── hypothesis_registry.py
├── experiment_registry.py
├── metric_registry.py
├── risk_register.py
└── review_gate.py

orchestration/
memory/
observability/
evals/
benchmarks/
examples/
docs/
prompts/
config/
safety/
tests/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

## Hypothesis quality

The policy requires `hypothesis_reviewed`.

A useful hypothesis should identify:

```text
observed_problem
population
proposed_change
causal_mechanism
primary_metric
expected_direction
risk_assumptions
supporting_evidence
falsification_condition
```

A hypothesis is not simply a desired outcome. F129 should distinguish prior evidence from speculation and avoid writing hypotheses that cannot be meaningfully falsified.

## Problem framing

Growth experimentation should begin with a real user, product, or business problem rather than an arbitrary request to maximize a metric. Relevant inputs can include funnel evidence, user research, support themes, product telemetry, market evidence, retention patterns, behavioral data, and operational constraints.

Metric movement without a meaningful problem definition can lead to local optimization and user harm.

## Causal mechanism

A strong experiment should explain why a treatment is expected to affect an outcome. Mechanism reasoning helps separate genuine product learning from random variant generation.

The system should preserve competing mechanisms and alternative explanations where relevant.

## Experiment design

The policy requires `experiment_design_reviewed`.

A governed design can preserve:

- experiment identifier
- hypothesis
- population
- eligibility
- exclusion rules
- control condition
- treatment variants
- randomization unit
- allocation ratio
- sample target
- duration
- primary metric
- guardrail metrics
- stopping rule
- power assumptions
- instrumentation requirements
- analysis plan
- review owner

`TOOLS/experiment_registry.py` provides a deterministic surface for these records.

## Control groups

A valid control should reflect the appropriate counterfactual for the decision being tested. F129 should not choose a weak or artificial control merely to increase the apparent treatment effect.

## Randomization

Randomization reduces systematic differences between groups when implemented correctly. Relevant review can include assignment unit, randomization method, stratification, cluster effects, persistent assignment, bucketing, and contamination.

`sample_integrity_gap` blocks release when randomization, assignment, or sample integrity is unresolved.

## Unit of randomization

The correct randomization unit may be a user, account, household, store, region, device, team, marketplace, or another entity. A mismatch between analysis unit and assignment unit can invalidate uncertainty estimates.

## Eligibility

Eligibility criteria should be defined before activation and should not be changed mid-experiment merely to improve results.

`change_eligibility` is a protected action.

Eligibility logic can also create fairness or representativeness concerns and therefore requires review.

## Sample size and power

Experiment planning should consider minimum detectable effect, baseline rate, variance, significance level, desired power, attrition, clustering, multiple variants, and practical business relevance.

A statistically detectable effect is not automatically a meaningful effect.

## Duration

Duration should account for traffic, conversion lag, weekly cycles, seasonality, novelty, learning effects, and operational constraints. Running until a preferred result appears is not valid experiment design.

## Primary metrics

The policy requires `measurement_reviewed`.

A primary metric should be chosen before results are observed and should reflect the core hypothesis. Examples can include activation, qualified conversion, retention, successful task completion, revenue quality, or another outcome aligned with actual user and business value.

## Secondary metrics

Secondary metrics can help explain mechanism, heterogeneity, or downstream effects, but should not be opportunistically promoted to primary status after the fact without transparent post-hoc labeling.

## Guardrail metrics

Guardrails protect against harmful local optimization. They can include:

- safety events
- complaints
- refunds
- support contacts
- latency
- crashes
- churn
- accessibility degradation
- trust indicators
- spam reports
- quality defects
- downstream conversion quality

`unsafe_guardrail` blocks release when safety, quality, or customer-harm guardrails are unresolved.

## Instrumentation integrity

Metrics depend on valid instrumentation. Review should consider event definitions, duplicate events, missing events, timestamp integrity, logging changes, bot traffic, test traffic, delayed events, schema drift, and experiment assignment logging.

`metric_integrity_gap` blocks release when measurement is not trustworthy enough for the intended decision.

## Metric definitions

`TOOLS/metric_registry.py` can preserve:

```text
metric_name
definition
numerator
denominator
population
window
source
owner
version
guardrail_status
```

Metric definitions should be versioned because seemingly small changes can alter conclusions.

## Novelty effects

A treatment may initially perform differently because it is new. F129 should consider novelty and adaptation before generalizing short-run effects into long-term conclusions.

## Primacy effects

Prior exposure to an existing design can also influence treatment response. Long-term users and new users may react differently.

## Seasonality

Day-of-week patterns, holidays, promotions, market events, weather, academic calendars, payroll cycles, and other timing effects can influence experimental outcomes.

## Network effects and interference

Standard experiment assumptions can fail when one participant's treatment affects another participant. This can occur in marketplaces, social networks, collaboration tools, pricing, referral systems, and supply-constrained environments.

Interference should be considered before interpreting user-level randomization as independent.

## Cluster randomization

Cluster or geo experiments may be more appropriate where interference is strong. Analysis should account for the number of clusters and intracluster correlation rather than treating every user as independent.

## Multiple testing

Running many metrics, segments, variants, or experiments increases false-positive risk. F129 should preserve the distinction between predeclared analyses and exploratory analyses.

## Sequential monitoring

Repeatedly checking results and stopping when significance appears can inflate false positives.

`premature_stopping_risk` blocks release when peeking or early-stopping logic is unresolved.

`terminate_experiment_early` is protected and requires qualified human authority.

## Stopping rules

Stopping can be based on planned duration, information thresholds, sequential methods, safety triggers, futility, operational necessity, or other reviewed criteria.

The reason for stopping should be recorded and should not be rewritten after results are known.

## Bayesian analysis

Bayesian methods can support experiment analysis when priors, likelihoods, decision thresholds, and interpretation are explicitly defined. Bayesian probability statements should not be mixed casually with frequentist significance language.

## Frequentist analysis

Frequentist methods should preserve test choice, assumptions, alpha, confidence intervals, variance estimation, clustering, multiple testing, and pre-specified analysis plans.

A p-value should not be presented as the probability that a hypothesis is true.

## Confidence intervals

Confidence intervals provide information about plausible effect magnitude and uncertainty. Decisions should consider whether the interval includes practically harmful or negligible effects, not only whether it excludes zero.

## Practical significance

A statistically significant effect can be too small to justify engineering cost, customer disruption, operational complexity, or long-term maintenance. Practical significance should be considered alongside statistical significance.

## Heterogeneous treatment effects

Subgroup analysis can reveal meaningful variation but also creates false-discovery risk. Subgroups should be pre-specified where possible and should not be used to construct unsupported discriminatory targeting.

## Fairness

The policy requires `fairness_reviewed`.

`fairness_risk` blocks release when discrimination, disparate impact, exclusion, or inequitable treatment risk is unresolved.

Review can consider protected characteristics, proxies, accessibility, geographic effects, economic vulnerability, language, device access, and differential exposure.

## Privacy and consent

The policy requires `privacy_consent_reviewed`.

`privacy_consent_gap` blocks release when data use, consent, notice, retention, or privacy obligations are unresolved.

Experimentation should collect only data necessary for the legitimate test and should avoid silently expanding data use simply because additional signals are available.

## Sensitive experiments

Experiments involving health, finance, credit, employment, education, housing, children, public safety, emotional vulnerability, or other high-impact contexts may require specialized review beyond ordinary growth processes.

F129 should escalate such experiments rather than relying only on generic experimentation approval.

## Dark patterns

`dark_pattern_risk` blocks release.

Examples include hidden cancellation, forced continuity, misleading scarcity, disguised ads, confirm-shaming, obstructive opt-out, deceptive defaults, hidden costs, false urgency, coercive consent, and intentionally confusing interfaces.

Growth goals do not justify manipulating users into choices they would not otherwise make.

## Deceptive experimentation

F129 should not design experiments whose mechanism depends on false claims, fabricated social proof, impersonation, fake scarcity, undisclosed material conditions, or other deception.

## Pricing experiments

Pricing experiments can affect fairness, trust, regulation, contracts, taxation, revenue recognition, and customer expectations.

`change_pricing_or_offer` is protected. F129 can design and analyze pricing tests but cannot autonomously alter live pricing or offers.

## Offer experiments

Promotions, discounts, trials, bundles, credits, or incentives should preserve eligibility, duration, economics, legal terms, and customer expectations.

## Eligibility experiments

Changing eligibility can affect access to products, features, benefits, or services. Such experiments require fairness and legal review when high-impact outcomes are involved.

## Product experiments

Product experiments can alter navigation, onboarding, features, ranking, recommendations, notifications, defaults, or workflows. Production activation remains under authorized product and engineering control.

`change_production_experience` is protected.

## Messaging experiments

Copy and creative tests should remain truthful, substantiated, and consistent with product reality. The experiment framework should not create an exception to normal claims governance.

## Notification experiments

Notification frequency, urgency, timing, and channel can affect user attention and well-being. F129 should consider opt-out, quiet hours, fatigue, accessibility, and coercive pressure.

## Retention experiments

Retention should not be increased through deliberate friction that traps users or makes cancellation, export, deletion, or switching unnecessarily difficult.

## Referral experiments

Referral programs can create spam, fraud, incentive gaming, privacy exposure, and misaligned behavior. Metrics should include quality and abuse guardrails rather than invitation volume alone.

## Marketplace experiments

Marketplace tests can affect buyers, sellers, supply, pricing, matching, congestion, and cross-side behavior. Network effects and interference should be explicit in design.

## Ranking and recommendation experiments

Ranking changes can affect visibility, opportunity, creator or seller economics, diversity, safety, and feedback loops. Guardrails should include ecosystem effects where relevant.

## Experiment collisions

Concurrent experiments can interact. F129 should preserve exposure information and identify mutually exclusive or interacting tests where possible.

## Holdouts

Long-term holdouts can help estimate cumulative effects but can create operational complexity and user-experience divergence. Their purpose and duration should be explicit.

## Sample ratio mismatch

Unexpected allocation ratios can indicate assignment bugs, logging failures, exclusions, bot traffic, or treatment-induced sample loss. Sample ratio mismatch should trigger investigation before outcome interpretation.

## Attrition

Differential dropout can bias results. F129 should examine whether treatment affects observability or eligibility for the outcome itself.

## Missing data

Missingness can be random or treatment-related. The system should preserve assumptions and avoid silently dropping observations in ways that favor a preferred result.

## Outliers

Outlier handling should be specified before analysis where practical. Removing inconvenient values after seeing results can introduce bias.

## Revenue metrics

Revenue experiments should consider refunds, returns, margin, delayed conversion, recurring revenue, cannibalization, payment failure, taxes, and downstream retention where relevant.

## Long-term effects

Short-term conversion gains can reduce trust, retention, product quality, or brand value later. F129 should preserve long-term guardrails when the mechanism could create delayed harm.

## Experiment ethics

Experimentation should respect autonomy, proportionality, privacy, fairness, transparency requirements, and participant welfare. Not every measurable behavior should be optimized.

## Risk register

`TOOLS/risk_register.py` supports deterministic recording of risks, evidence, severity, mitigation, owner, escalation, and status.

Risk review should not disappear from the final package simply because expected upside is large.

## Evidence provenance

The policy requires `evidence_provenance_reviewed`.

Material evidence should preserve source, period, version, metric definition, experiment identifier, assignment logic, analysis code reference, exclusions, and reviewer.

`evidence_provenance_gap` blocks release.

F129 must never fabricate experiment results, sample sizes, significance, confidence intervals, lift, guardrail performance, assignments, user research, or approvals.

## Reproducibility

A reproducible experiment package should preserve:

- hypothesis version
- experiment configuration
- code/config version
- allocation
- eligibility
- metric definitions
- analysis plan
- data window
- exclusions
- stopping reason
- results
- uncertainty
- reviewer decision

## Decision states

Useful result states include:

```text
ship candidate
iterate
inconclusive
harm detected
instrumentation invalid
sample invalid
stop for safety
needs follow-up
```

The system should not force every experiment into winner or loser language.

## Inconclusive results

An inconclusive experiment can still provide useful learning about variance, instrumentation, effect bounds, or mechanism. F129 should not manufacture certainty to justify prior investment.

## Negative results

Negative findings should be preserved rather than hidden. A failed hypothesis can prevent future waste and improve the knowledge base.

## Replication

Important surprising results may warrant replication, especially when effect size is large, prior plausibility is low, sample is small, or operational consequences are substantial.

## Experiment learning repository

The memory layer can preserve structured learnings across experiments while separating observed evidence from interpretation. Historical results should not be generalized to new populations or products without checking context.

## Production activation boundary

`activate_experiment` is protected.

F129 can prepare an experiment-ready package, but cannot activate flags, enroll users, change traffic allocation, or start production exposure.

## External platform writes

`external_platform_write` is protected.

Any integration capable of changing feature flags, experimentation platforms, pricing systems, notification systems, ad platforms, websites, or production configuration must remain behind explicit human-controlled authorization.

## Human authority boundaries

F129 must not autonomously:

- activate experiments
- change production experiences
- alter live pricing or offers
- modify eligibility
- terminate experiments early
- change traffic allocation
- write to experimentation platforms
- waive privacy or fairness review
- remove guardrails to improve apparent results
- fabricate experimental evidence

Final experiment activation, stopping, shipping, pricing, eligibility, and production-change decisions remain with qualified humans.

## Required reviews

The executable policy requires all eight conditions:

```text
hypothesis_reviewed
experiment_design_reviewed
measurement_reviewed
risk_reviewed
privacy_consent_reviewed
fairness_reviewed
evidence_provenance_reviewed
qualified_experiment_approval
```

Missing any condition fails closed.

## Fail-closed governance

The implemented policy blocks release when:

- a dark pattern or manipulative treatment is detected
- privacy, consent, or data-use review is incomplete
- fairness, discrimination, or disparate-impact risk remains unresolved
- randomization, assignment, or sample integrity is unresolved
- metric definition, instrumentation, or analysis integrity is unresolved
- safety, quality, or customer-harm guardrails are unresolved
- early stopping or peeking risk remains unresolved
- experiment evidence provenance is incomplete
- any required review is missing
- qualified experiment approval is missing

## Protected actions

The safety policy permanently protects:

```text
activate_experiment
change_production_experience
change_pricing_or_offer
change_eligibility
terminate_experiment_early
external_platform_write
```

These remain outside autonomous authority even when all review conditions are satisfied.

## Explicit failure states

```text
HYPOTHESIS REVIEW REQUIRED
EXPERIMENT DESIGN REVIEW REQUIRED
MEASUREMENT REVIEW REQUIRED
RISK REVIEW REQUIRED
PRIVACY OR CONSENT GAP
FAIRNESS RISK
DARK PATTERN DETECTED
SAMPLE INTEGRITY GAP
METRIC INTEGRITY GAP
UNSAFE GUARDRAIL
PREMATURE STOPPING RISK
EVIDENCE PROVENANCE GAP
QUALIFIED EXPERIMENT APPROVAL REQUIRED
EXPERIMENT ACTIVATION PROHIBITED
PRODUCTION CHANGE PROHIBITED
PRICING OR OFFER CHANGE PROHIBITED
ELIGIBILITY CHANGE PROHIBITED
EARLY TERMINATION PROHIBITED
EXTERNAL PLATFORM WRITE PROHIBITED
```

## End-to-end reference workflow

1. Define the problem and gather supporting evidence.
2. Form a falsifiable hypothesis with a proposed causal mechanism.
3. Define population, eligibility, exclusion, control, and treatment.
4. Choose randomization unit, allocation, sample target, and duration.
5. Predefine primary, secondary, and guardrail metrics.
6. Review instrumentation and metric definitions.
7. Review privacy, fairness, manipulation, safety, and customer-harm risks.
8. Define analysis and stopping rules before activation.
9. Preserve evidence provenance and experiment versions.
10. Apply fail-closed governance.
11. Require explicit qualified-human experiment approval.
12. Keep activation, pricing, eligibility, production changes, early stopping, and platform writes outside autonomous authority.
13. Analyze results with uncertainty and integrity checks.
14. Preserve inconclusive and negative findings alongside positive findings.

## Evaluation and held-out governance suite

The repository contains evaluation logic under `evals/` and benchmark cases under `benchmarks/`.

Evaluation should test hypothesis quality, causal design, randomization integrity, measurement quality, guardrail discipline, fairness, privacy, stopping behavior, evidence provenance, and protected-action enforcement.

The behavioral verification layer includes direct governance tests and a 10-scenario held-out suite covering missing review, successful reviewed release, dark patterns, privacy gaps, fairness risks, sample-integrity gaps, metric-integrity gaps, unsafe guardrails, premature stopping, and provenance gaps.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

These gates verify syntax-critical linting, fail-closed behavior, held-out governance scenarios, and execution of the governed reference workflow.

## Observability

The `observability/` layer supports traceability across hypothesis, assignment, metrics, risks, approvals, and protected-action attempts.

Useful telemetry includes experiment version, allocation, eligibility, assignment health, sample ratio, metric status, guardrail state, analysis state, stopping state, fairness review, privacy review, and governance blockers.

## Extension points

Organization-specific implementations can add governed integrations for experimentation platforms, feature flags, analytics, data warehouses, product telemetry, survey systems, pricing systems, notification systems, and model evaluation infrastructure.

Any integration capable of changing production must remain behind explicit authorization, least privilege, audit logging, rollback capability, and human-controlled execution.

## Example applications

Potential governed uses include onboarding experiments, activation experiments, retention experiments, pricing-test planning, notification experiments, marketplace experiments, ranking experiments, referral experiments, landing-page tests, feature experiments, and experiment-review workflows.

F129 is not an autonomous growth hacker, production feature-flag controller, pricing authority, experimentation platform operator, or substitute for qualified statistical, product, legal, privacy, ethics, safety, or engineering judgment.

## Design principles

1. Start from a falsifiable hypothesis, not a preferred result.
2. Design for causal learning, not metric theater.
3. Predefine metrics, guardrails, and stopping logic.
4. Preserve sample, assignment, and instrumentation integrity.
5. Reject dark patterns and manipulative treatments.
6. Protect privacy, consent, fairness, and vulnerable users.
7. Preserve uncertainty, negative results, and inconclusive findings.
8. Fail closed when material evidence or review is incomplete.
9. Keep all production changes under qualified human authority.

## Scope statement

F129 demonstrates a governed multi-agent architecture for growth experimentation decision support. It combines specialized hypothesis, experiment, measurement, risk, and review agents with deterministic experiment records, observability, held-out evaluation, and fail-closed governance while preserving strict human authority over production activation and experiment execution.

Author: Mahsa Keikha
