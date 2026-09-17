# confluentkafka-python

## Environment variables

Copy `.env.example` to `.env`, then set the value you need:

```text
APP_SETTING=your_value
```

Load it in Python with `python-dotenv`:

```powershell
pip install python-dotenv
```

```python
import os

from dotenv import load_dotenv

load_dotenv()
setting = os.environ["APP_SETTING"]
```

The real `.env` file is ignored by Git so values do not get committed.