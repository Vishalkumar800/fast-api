from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / ".env")

class Settings(BaseSettings):
    DATABASE_URL : str
    SECRET_KEY :str
    ALGORITHM : str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30

    class config:
        env_file = ".env"


settings = Settings()


'''

Bilkul simple language me samjho 👇

`BaseSettings` ka main kaam hai **`.env` file ke variables ko Python ke andar safely/configuration ke form me lana**.

### 1. Maan lo `.env` me hai

```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=abc123
```

Normally tumhe manually environment variable read karna padta:

```python
import os

database_url = os.getenv("DATABASE_URL")
```

Lekin `BaseSettings` se tum ek **configuration class** bana sakte ho:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env")
```

Ab:

```python
settings = Settings()
```

Pydantic `.env` se values uthakar automatically class ke andar daal dega.

So:

```python
settings.DATABASE_URL
```

gives:

```text
sqlite:///./test.db
```

and:

```python
settings.SECRET_KEY
```

gives:

```text
abc123
```

### 2. Iska fayda kya hai?

Sabse bada fayda **validation** hai.

Maan lo:

```python
class Settings(BaseSettings):
    PORT: int
```

Aur `.env` me:

```env
PORT=8000
```

Pydantic automatically `8000` ko integer me convert karega.

Agar galat value:

```env
PORT=hello
```

to Pydantic error dega. 🔥

### 3. Real FastAPI project me

Tumhare project me maan lo database, secret key, API key hain:

```env
DATABASE_URL=...
SECRET_KEY=...
API_KEY=...
```

To code me baar-baar:

```python
os.getenv(...)
```

karne ke bajay:

```python
settings.DATABASE_URL
settings.SECRET_KEY
settings.API_KEY
```

use kar sakte ho.

**Short me:**

> `BaseSettings` = `.env` / environment variables ko ek structured, validated Python configuration object me convert karne ka convenient way.

Aur **`.env` ka purpose** ye hai ki secret/config values ko directly Python code me hardcode na karna pade.


'''