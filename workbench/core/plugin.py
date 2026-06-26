from abc import ABC, abstractmethod


class Plugin(ABC):
    """
    Base class for every Workbench capability.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """Plugin name."""

    @abstractmethod
    def install(self):
        """Install the capability."""

    @abstractmethod
    def configure(self):
        """Configure the capability."""

    @abstractmethod
    def start(self):
        """Start the capability."""

    @abstractmethod
    def stop(self):
        """Stop the capability."""

    @abstractmethod
    def status(self):
        """Return current status."""

    @abstractmethod
    def health_check(self):
        """Check whether the capability is healthy."""

    @abstractmethod
    def update(self):
        """Update the capability."""

    @abstractmethod
    def uninstall(self):
        """Remove the capability."""