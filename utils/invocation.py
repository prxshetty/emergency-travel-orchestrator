import time
from typing import Dict, Any, Callable

def invoke_with_retry(app: Any, messages: Dict[str, Any], config: Dict[str, Any], max_retries: int = 5) -> Dict[str, Any]:
    for attempt in range(max_retries):
        try:
            return app.invoke(messages, config)
        except Exception as e:
            if "model produced invalid content" in str(e):
                print(f"Attempt {attempt + 1} failed due to model output error, simplifying request...")
            if attempt == max_retries - 1:
                print(f"Failed after {max_retries} attempts: {str(e)}")
                raise
            print(f"Retrying in 1 second...")
            time.sleep(1) 