#!/usr/bin/env python3
"""
Advanced usage example for gotty-py client.

This example demonstrates real-time callbacks and more advanced features.
"""

import os
import sys
import time

# Add the parent directory to the path so we can import gotty_py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from gotty_client import GottyWebSocketClient


class AdvancedGottyClient:
    """Advanced gotty client with real-time callbacks."""

    def __init__(self, webui_url, username, password):
        """Initialize the advanced client."""
        self.client = GottyWebSocketClient(webui_url, username, password)
        self.output_buffer = []
        self.command_count = 0

        # Set up callbacks
        self.client.add_output_callback(self._on_output)
        self.client.add_command_callback(self._on_command)

    def _on_output(self, data):
        """Callback for real-time output."""
        timestamp = time.strftime("%H:%M:%S")
        self.output_buffer.append(f"[{timestamp}] {data.strip()}")

        # Keep only last 100 lines
        if len(self.output_buffer) > 100:
            self.output_buffer = self.output_buffer[-100:]

        # Print to console in real-time
        print(f"📤 {data.strip()}")

    def _on_command(self, command):
        """Callback for command completions."""
        self.command_count += 1
        timestamp = time.strftime("%H:%M:%S")
        print(f"🎯 [{timestamp}] Command #{self.command_count}: {command}")

    def connect(self):
        """Connect to the gotty server."""
        return self.client.connect()

    def execute_commands(self, commands, delay=1.0):
        """Execute multiple commands with delay."""
        for i, command in enumerate(commands):
            print(f"\n🚀 Executing command {i+1}/{len(commands)}: {command}")

            response = self.client.execute_command(command, timeout=10.0)

            if response.success:
                print(f"✅ Command '{command}' succeeded")
            else:
                print(f"❌ Command '{command}' failed: " f"{response.message}")

            # Wait before next command
            if i < len(commands) - 1:
                time.sleep(delay)

    def get_stats(self):
        """Get client statistics."""
        return {
            "commands_executed": self.command_count,
            "output_lines": len(self.output_buffer),
            "connected": self.client.connected,
            "terminal_output_lines": len(self.client.terminal_output),
            "command_history": len(self.client.command_history),
        }

    def close(self):
        """Close the connection."""
        self.client.close()


def main():
    """Main function demonstrating advanced usage."""
    print("Gotty Python Client - Advanced Usage Example")
    print("=" * 55)

    # Create advanced client
    client = AdvancedGottyClient(
        webui_url="http://192.168.0.113:8222",
        username="admin",
        password="admin",
    )

    try:
        print("Connecting to gotty server...")
        if client.connect():
            print("✓ Connected successfully!")

            # Execute multiple commands
            commands = ["ls", "pwd", "whoami", "date"]

            print(f"\nExecuting {len(commands)} commands...")
            client.execute_commands(commands, delay=0.5)

            # Show statistics
            print("\n" + "=" * 40)
            print("📊 CLIENT STATISTICS")
            print("=" * 40)
            stats = client.get_stats()
            for key, value in stats.items():
                print(f"{key.replace('_', ' ').title()}: {value}")

            # Show recent output
            print("\n" + "=" * 40)
            print("📝 RECENT OUTPUT")
            print("=" * 40)
            recent_output = client.output_buffer[-10:]  # Last 10 lines
            for line in recent_output:
                print(line)

            # Show command history
            print("\n" + "=" * 40)
            print("📚 COMMAND HISTORY")
            print("=" * 40)
            history = client.client.get_command_history()
            for i, cmd in enumerate(history[-5:], 1):  # Last 5 commands
                print(f"{i}. {cmd}")

        else:
            print("✗ Failed to connect to gotty server")
            return 1

    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"✗ Error: {e}")
        return 1

    finally:
        print("\nClosing connection...")
        client.close()
        print("✓ Connection closed")

    print("\nExample completed successfully!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
