from typing import Optional, Iterator, List, Any
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.language_models.chat_models import BaseChatModel
from ..base import BaseLLMProvider
import logging


class NvidiaProvider(BaseLLMProvider):
    """NVIDIA AI Endpoints provider"""
    
    def __init__(self, model: str, temperature: float = 0.2, **kwargs):
        super().__init__(model, temperature, **kwargs)
        self.client = ChatNVIDIA(
            model=self.model,
            temperature=self.temperature,
            **kwargs
        )
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        messages = []
        if system_prompt:
            messages.append(SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=prompt))
        
        try:
            response = self.client.invoke(messages)
            if isinstance(response.content, str):
                return response.content
            else:
                return ""
        except Exception as e:
            logging.error(f"NVIDIA generation error: {e}")
            raise
    
    def stream_generate(self, prompt: str, system_prompt: Optional[str] = None) -> Iterator[str]:
        messages = []
        if system_prompt:
            messages.append(SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=prompt))
        
        try:
            for chunk in self.client.stream(messages):
                if not isinstance(chunk.content, str):
                    continue
                yield chunk.content
        except Exception as e:
            logging.error(f"NVIDIA streaming error: {e}")
            raise
    
    def invoke_with_messages(self, messages: List[Any]) -> AIMessage:
        """Invoke with message list (for agent use)"""
        return self.client.invoke(messages)
    
    async def ainvoke_with_messages(self, messages: List[Any]) -> AIMessage:
        """Async invoke with message list (for agent use)"""
        return await self.client.ainvoke(messages)

    def stream_with_messages(self, messages: List[Any]) -> Iterator[AIMessage]:
        """Stream with message list (for agent use)"""
        return self.client.stream(messages)
    
    def check_availability(self) -> bool:
        try:
            self.client.invoke([HumanMessage(content="test")])
            return True
        except Exception as e:
            logging.warning(f"NVIDIA availability check failed: {e}")
            return False

    def get_model(self) -> BaseChatModel:
        """Return the underlying LangChain model"""
        return self.client