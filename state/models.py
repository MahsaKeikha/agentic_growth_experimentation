from dataclasses import dataclass, field

@dataclass
class ExperimentState:
    hypotheses: list = field(default_factory=list)
    metrics: list = field(default_factory=list)
    risks: list = field(default_factory=list)
    human_approval: bool = False
