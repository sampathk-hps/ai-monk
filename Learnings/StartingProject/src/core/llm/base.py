from abc import ABC, abstractmethod
from typing import Optional, Iterator, List, Any
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import AnyMessage, AIMessage


class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    def __init__(self, model: str, temperature: float = 0.2, **kwargs):
        self.model = model
        self.temperature = temperature
        self.kwargs = kwargs
        self.tools: List[Any] = []
    
    @abstractmethod
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate a single response"""
        pass
    
    @abstractmethod
    def stream_generate(self, prompt: str, system_prompt: Optional[str] = None) -> Iterator[str]:
        """Generate streaming response"""
        pass
    
    @abstractmethod
    def invoke_with_messages(self, messages: List[AnyMessage]) -> AIMessage:
        """Invoke with message list (for agent use)"""
        pass
    
    @abstractmethod
    async def ainvoke_with_messages(self, messages: List[AnyMessage]) -> AIMessage:
        """Async invoke with message list (for agent use)"""
        pass

    @abstractmethod
    def stream_with_messages(self, messages: List[AnyMessage]) -> Iterator[AIMessage]:
        """Stream with message list (for agent use)"""
        pass
    
    @abstractmethod
    def check_availability(self) -> bool:
        """Check if the model/service is available"""
        pass

    @abstractmethod
    def get_model(self) -> BaseChatModel:
        """Return the underlying LangChain model/client"""
        pass
    
    def bind_tools(self, tools: List[Any]) -> 'BaseLLMProvider':
        """Bind tools to the LLM for agent use"""
        self.tools = tools
        self.client = self.client.bind_tools(tools)
        return self
