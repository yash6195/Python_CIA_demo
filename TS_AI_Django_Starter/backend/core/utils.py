import random, string, time

def random_value(kind: str):
    if kind == "string":
        return "".join(random.choices(string.ascii_letters, k=10))
    if kind == "number":
        return random.randint(1, 1000)
    if kind == "boolean":
        return random.choice([True, False])
    if kind == "array":
        return [random.randint(0, 9) for _ in range(5)]
    if kind == "object":
        return {"key": "value", "n": random.randint(1, 99)}
    return None

def simulate_delay(ms: int):
    time.sleep(ms / 1000.0)
