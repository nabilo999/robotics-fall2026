def decide(state, event):
    phase = state["phase"]
    kind = event["kind"]
    target = event["target"]
    active = phase in ("CLARIFY", "CONFIRM", "EXECUTING", "WAIT_READY")

    if kind == "CANCEL" and active:
        return "cancel"

    if kind == "REQUEST" and phase in ("IDLE", "CLARIFY", "CONFIRM", "RECOVERY", "CANCELLED"):
        if target in ("red", "blue"):
            return "select"
        if target is None:
            return "clarify"

    if kind == "CORRECT" and active and target in ("red", "blue"):
        return "select"

    if kind == "CONFIRM" and phase == "CONFIRM":
        return "begin"

    if kind == "TICK" and phase == "EXECUTING":
        return "advance"

    if phase == "WAIT_READY":
        if kind == "READY":
            return "release"
        if kind == "TIMEOUT":
            return "timeout"

    return "hold"