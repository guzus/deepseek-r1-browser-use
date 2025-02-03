# Deepseek R1 brower-use

https://github.com/user-attachments/assets/08d8ac9d-4862-49a3-b42a-fe69c97240d5

## Quick start

1. Create .env file from .env.example and fill in the DEEPSEEK_API_KEY (get it from [Deepseek](https://platform.deepseek.com/api_keys))

```bash
cp .env.example .env
```

2. Install the dependencies and playwright

```bash
uv sync
pip install playwright
playwright install
```

3. Run

```bash
uv run simple.py
```

## Result Analysis

### Cost Breakdown

#### Prompt Example

**Prompt:** "Find hotels with the best reviews in Shanghai. Three men will stay for 4 nights from Feb 23th to Feb 27th, and the budget is $500."

#### Experiment Results

- **Total Cost:** $0.02
- **Processing Time:** 3 minutes

#### Initial Result

The agent returned the following output:

```
INFO     [agent] 📄 Result: Top budget options found (prices may vary):
1. Jinjiang MetroPolo Hotel Classiq - $73/night, 4/5 stars (314 reviews)
2. JinJiang Metropolo Bund Circle - Price not shown
*Note: Dates/guests not fully configured - verify directly with hotel for 3 adults Feb 23-27 availability
INFO     [agent] ✅ Task completed successfully
WARNING  [agent] No history or first screenshot to create GIF from
```

#### Accuracy Limitations

- Key Issue The result is inaccurate due to room occupancy constraints:
- The search assumes a single room for three men
- Most hotel rooms accommodate at most two people
- This would require booking two rooms, exceeding the $500 budget
