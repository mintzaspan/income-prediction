# Income prediction

## How to use
### Set up environment
1. Download `uv` and install according to [guide](https://docs.astral.sh/uv/getting-started/installation/).
2. Clone repo
3. Install environment with `uv` by runnning `uv sync`.
4. Activate virtual environment `source .venv/bin/activate' or run commands by adding `uv run`. For example, `uv run pre-commit install`.
5. Install pre-commit hooks with `pre-commit install`.

### Train model
1. Clean data - `python src/clean_data.py`.
2. Train model (including evaluation) - `python src/train_model.py`.

### Test
1. Test model and app by executing `pytest`.
