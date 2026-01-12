from .base import BaseLLMProvider
from .providers import GeminiProvider
from .providers import NvidiaProvider

class LLMFactory:
    """Factory for creating LLM provider instances"""
    
    _providers = {
        "gemini": GeminiProvider,
        "nvidia": NvidiaProvider
    }
    
    @classmethod
    def create(cls, provider: str, model: str, temperature: float = 0.2, **kwargs) -> BaseLLMProvider:
        """
        Create an LLM provider instance
        
        Args:
            provider: Provider name ("nvidia", "ollama", "gemini")
            model: Model name/identifier
            temperature: Generation temperature
            **kwargs: Additional provider-specific arguments
        
        Returns:
            BaseLLMProvider instance
        """
        provider_lower = provider.lower()
        if provider_lower not in cls._providers:
            raise ValueError(f"Unknown provider: {provider}. Available: {list(cls._providers.keys())}")
        
        provider_class = cls._providers[provider_lower]
        return provider_class(model=model, temperature=temperature, **kwargs)
    
    @classmethod
    def register_provider(cls, name: str, provider_class: type):
        """Register a new provider"""
        cls._providers[name.lower()] = provider_class
