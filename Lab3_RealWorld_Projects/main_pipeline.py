# main_pipeline.py

import telemetry_core

# Student Inputs
LAST_NAME = "ALCANTARA"  #[cite: 11]
SEED_NUM = 0  #[cite: 11] (Last digit of 1830)
FAVORITE_ARTIST = "ADIE"  #[cite: 11]


# Decorator to monitor processing
def monitor_execution(func):
  def wrapper(*args, **kwargs):
    print("[MONITOR] Pipeline execution started.")
    res = func(*args, **kwargs)
    print("[MONITOR] Pipeline execution completed.")
    return res

  return wrapper


@monitor_execution
def run_pipeline():
  # Generate student-specific telemetry stream using generator
  def telemetry_generator(limit):
    for i in range(limit):
      yield (i * 10) + (SEED_NUM * 5) - len(LAST_NAME)

  limit = len(FAVORITE_ARTIST) + 5
  raw_stream = list(telemetry_generator(limit))

  # Validation and analysis via custom module
  valid_readings, invalid_count = telemetry_core.analyze_stream(raw_stream)

  # Lambda function to filter/transform valid readings above threshold
  filtered_readings = list(filter(lambda x: x >= 0, valid_readings))
  avg_val = (
      sum(filtered_readings) / len(filtered_readings)
      if filtered_readings
      else 0
  )

  # Recursive fault trace based on artist name length
  trace_logs, call_count = telemetry_core.recursive_fault_trace(
      len(FAVORITE_ARTIST)
  )

  status = (
      "Optimal"
      if avg_val >= 20
      else ("Moderate" if avg_val >= 10 else "Critical")
  )

  return {
      "raw": raw_stream,
      "valid": valid_readings,
      "invalid_count": invalid_count,
      "avg": avg_val,
      "status": status,
      "trace_logs": trace_logs,
      "call_count": call_count,
  }


if __name__ == "__main__":
  results = run_pipeline()
  print("=" * 50)
  print(f"Student: {LAST_NAME} | Artist: {FAVORITE_ARTIST}")
  print(f"Generated Telemetry: {results['raw']}")
  print(f"Valid/Invalid Results: {results['valid']} ({results['invalid_count']} invalid)")
  print(f"Processed Average: {round(results['avg'], 2)}")
  print(f"Recursive Analysis Calls: {results['call_count']}")
  print(f"Final Diagnostic Summary: {results['status']}")
  print("=" * 50)