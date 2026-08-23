from AGENTS import experiment_agent, hypothesis_agent, measurement_agent, review_agent, risk_agent
from safety.policy import authorize


def run(case: dict) -> dict:
    result = {
        "hypothesis": hypothesis_agent.run(case),
        "experiment": experiment_agent.run(case),
        "measurement": measurement_agent.run(case),
        "risk": risk_agent.run(case),
        "review": review_agent.run(case),
    }
    governance = authorize("release_support_package", case.get("governance", {}))
    result["governance"] = governance
    result["released"] = governance["allowed"]
    return result
