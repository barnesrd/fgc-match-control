from .enum import SubmitMode

class Profile:
    _submit_mode: SubmitMode = SubmitMode.ON_EDIT
    debounce: float = 0.5
    
    @property
    def submit_mode() -> SubmitMode:
        return self._submit_mode