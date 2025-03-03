from pathlib import Path
import json

numbers = [2,3,5,7,11,13]

p = Path(f"numbers.json")
c = json.dumps(numbers)
p.write_text(c)