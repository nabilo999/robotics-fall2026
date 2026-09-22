def build_pattern(pattern_name: str) -> list[Segment]:
    if pattern_name != "l_path":
        raise ValueError(f"Unknown pattern: {pattern_name}")

    return [
        Segment(linear_x=0.20, angular_z=0.0, duration=2.0),
        Segment(linear_x=0.0, angular_z=0.50, duration=1.57 / 0.50),
        Segment(linear_x=0.20, angular_z=0.0, duration=2.0),
    ]