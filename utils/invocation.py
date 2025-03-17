import time
from typing import Dict, Any, Callable

def invoke_with_retry(app: Any, messages: Dict[str, Any], config: Dict[str, Any], max_retries: int = 3) -> Dict[str, Any]:
    for attempt in range(max_retries):
        try:
            return app.invoke(messages, config)
        except ValueError as e:
            if attempt == max_retries - 1:
                print(f"Failed after {max_retries} attempts: {str(e)}")
                raise
            print(f"Attempt {attempt + 1} failed, retrying...")
            time.sleep(1) 