pip install pandas
python gematree_to_codona.py

---

#### 🔹 `gematree_to_codona.py`
Create another file and paste:

```python
import json

def get_gematria_value(word):
    # Placeholder using Ordinal cipher: A=1, B=2, ..., Z=26
    return sum([ord(c) - 64 for c in word.upper() if c.isalpha()])

def reduce_to_root(n):
    steps = [n]
    while n > 9:
        n = sum(int(d) for d in str(n))
        steps.append(n)
    return steps

def generate_codona_capsule(phrase):
    val = get_gematria_value(phrase)
    reduction_steps = reduce_to_root(val)
    root = reduction_steps[-1]
    tone_map = {
        3: [432, 384, 432],
        9: [324, 384, 432]
    }
    capsule = {
        "phrase": phrase,
        "digitalRoot": root,
        "toneArc": tone_map.get(root, [root * 100]),
        "vowelArc": ["A", "I", "A"],
        "cipherTrail": {
            "Ordinal": val,
            "ReductionSteps": reduction_steps
        },
        "glyph": f"GlyphOverlay_{phrase}.svg",
        "mode": "SpiralBreath"
    }
    with open(f"CodonaCapsule_{phrase}.json", "w") as f:
        json.dump(capsule, f, indent=2)
    print(f"✅ Codona capsule created for {phrase}.")

if __name__ == "__main__":
    generate_codona_capsule("AMRITA")
{
  "phrase": "AMRITA",
  "digitalRoot": 3,
  "toneArc": [432, 384, 432],
  "vowelArc": ["A", "I", "A"],
  "cipherTrail": {
    "Ordinal": 84,
    "ReductionSteps": [84, 12, 3]
  },
  "glyph": "GlyphOverlay_Amrita.svg",
  "mode": "SpiralBreath"
}

