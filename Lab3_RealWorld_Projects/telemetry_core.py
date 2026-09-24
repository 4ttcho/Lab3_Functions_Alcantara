# telemetry_core.py


def validate_reading(val):
  if val < 0:
    raise ValueError(f"Negative telemetry reading detected: {val}")
  return float(val)


def analyze_stream(readings):
  valid = []
  invalid_count = 0
  for r in readings:
    try:
      valid.append(validate_reading(r))
    except ValueError:
      invalid_count += 1
      valid.append(0.0)  # Safe default fallback
  return valid, invalid_count


def recursive_fault_trace(level):
  if level <= 0:
    return ["Base Reached: System Stable"], 0
  logs, count = recursive_fault_trace(level - 1)
  return [f"Tracing Anomaly Level {level}"] + logs, count + 1